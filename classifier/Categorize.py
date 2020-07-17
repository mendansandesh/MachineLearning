#!/usr/bin/python3

import spacy
import math

import MeaningfulWordExtractor
from sentence2vecAna import Word, Sentence, sentence_to_vec

nlp = spacy.load('en_core_web_lg')

# euclidean distance between two vectors
def l2_dist(v1, v2):
    sum = 0.0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            delta = v1[i] - v2[i]
            sum += delta * delta
        return math.sqrt(sum)

from nltk.corpus import stopwords
stop_words = stopwords.words("english")

# initialize all categoriies key:value pairs
categoryMapping = dict()
def initializeCategoryMapping():
    switcher = {
        'health': 'health',
        'personally': 'pii',
        'purchase': 'purchase',
        'authentication': 'auth',
        'tracking': 'userTracking'
    }
    with open('categories.txt') as reader:
        for line in reader:
            if len(line.strip()) > 0:
                categoryMapping[line.split(' ')[0]] = switcher.get(line.split(' ')[0])


def detectCategory(input):
    # TODO initialize using class constructor
    initializeCategoryMapping()

    embedding_size = 300  # dimension of spacy word embeddings

    # load some simple sentences for testing similarities between
    sentences = []
    with open('categories.txt') as reader:
        for line in reader:
            if len(line.strip()) > 0:
                sentences.append(MeaningfulWordExtractor.cleanAndFetchEnglishWords(line))
        sentences.append(MeaningfulWordExtractor.cleanAndFetchEnglishWords(input))

    # convert the above sentences to vectors using spacy's large model vectors
    sentence_list = []
    for sentence in sentences:
        word_list = []
        for word in sentence:
            token = nlp.vocab[word]
            if token.has_vector:  # ignore OOVs
                word_list.append(Word(word, token.vector))
        if len(word_list) > 0:  # did we find any words (not an empty set)
            sentence_list.append(Sentence(word_list))

    # apply single sentence word embedding
    sentence_vector_lookup = dict()
    sentence_vectors = sentence_to_vec(sentence_list, embedding_size)  # all vectors converted together
    result = dict()
    if len(sentence_vectors) == len(sentence_list):
        for i in range(len(sentence_vectors)):
            # map: text of the sentence -> vector
            sentence_vector_lookup[sentence_list[i].__str__()] = sentence_vectors[i]

        for x in range(len(sentence_vectors) - 1):
            result[sentence_list[x].__str__()] = l2_dist(sentence_vectors[x],
                                                         sentence_vectors[len(sentence_vectors) - 1])

    print(result.items())
    return categoryMapping.get(list(result.keys())[list(result.values()).index(min(result.values()))].split(' ')[0])

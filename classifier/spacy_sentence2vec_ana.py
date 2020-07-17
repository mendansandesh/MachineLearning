#!/usr/bin/python3

#
#  Copyright 2016-2018 Peter de Vocht
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import spacy
import math

import MeaningfulWordExtractor
from sentence2vecAna import Word, Sentence, sentence_to_vec

# use the spacy large model's vectors for testing semantic relatedness
# this assumes you've already installed the large model, if not download it and pip install it:
# wget https://github.com/explosion/spacy-models/releases/tag/en_core_web_lg-2.0.0
# pip install en_core_web_lg-2.0.0.tar.gz
nlp = spacy.load('en_core_web_lg')

# euclidean distance between two vectors
def l2_dist(v1, v2):
    sum = 0.0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            delta = v1[i] - v2[i]
            sum += delta * delta
        return math.sqrt(sum)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words("english")
if __name__ == '__main__':

    embedding_size = 300   # dimension of spacy word embeddings

    # load some simple sentences for testing similarities between
    sentences = []
    with open('semantic_ana_text.txt') as reader:
        for line in reader:
            if len(line.strip()) > 0:
                sentences.append(MeaningfulWordExtractor.cleanAndFetchEnglishWords(line))

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
            #print( sentence_list[len(sentence_list) - 1].__str__() + ' :: ' + sentence_list[x].__str__() + ' => distance = ' + str(l2_dist(sentence_vectors[x], sentence_vectors[len(sentence_vectors) - 1])))
            #result.append(l2_dist(sentence_vectors[x], sentence_vectors[len(sentence_vectors) - 1]))
            result[sentence_list[x].__str__()] = l2_dist(sentence_vectors[x], sentence_vectors[len(sentence_vectors) - 1])

    #print(result)
    print(result.items())
    #print(result.values())
    #print(list(result.keys())[list(result.values()).index(min(result.values()))])
    print('Given Input --> ' + sentence_list[len(sentence_list) - 1].__str__())
    print('Result is ' + list(result.keys())[list(result.values()).index(min(result.values()))] )

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:38:32 2019

@author: inct-sandeshmendan
"""
import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet
# input = "select * from employee where pan_card = sdaassdad123 "
# input = "/../../../etc/password"
#input = "https://www.amazon.in/gp/product_ball/B07S6P5FQ3/ref=ox_sc_act_title_6?smid=A2VQOLRW0XTGMB&psc=1z"


def cleanAndFetchEnglishWords(input):
    # Convert to lowercase
    text = input.lower()

    # Remove punctuations
    text = re.sub('[^a-zA-Z]', ' ', text)

    # remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

    # remove special characters and digits
    text = re.sub("(\\d|\\W)+", " ", text)

    ##Convert to list from string
    text = text.split()

    ##Creating a list of stop words and adding custom stopwords
    stop_words = set(stopwords.words("english"))
    new_words = ["http", "https", "www", "select", "where", "from", "into", "delete", "insert", "group by", "order by",
                 "desc", "asc", "count", "distinct", "join", "inner", "outer", "left", "right"]
    stop_words = stop_words.union(new_words)
    text = [w for w in text if w not in stop_words]
    text = " ".join(text)

    # print(text)

    result = []
    for i in text.strip().split(' '):
        if (len(i) > 1):
            if wordnet.synsets(i):
                result.append(i)

    # print(result)
    return result


# Stemming
# ps = PorterStemmer()
# text1 = []
# for w in text:
#     text1.append(ps.stem(w))
# print(text1)

# Lemmatisation
# lem = WordNetLemmatizer()
# text = [lem.lemmatize(word) for word in text if not word in stop_words]
# text = " ".join(text)


# print(wordnet.synsets('health'))
# syn = wordnet.synsets('ox')
# print(syn)
# print(syn[0])
# print(syn[0].name())
# print(syn[0].lemmas()[0].name())
# print(syn[0].definition())
# print(wordnet.synset('b.n.01'))
# print(syn[0].wup_similarity(wordnet.synset('health.n.01')))

# syn1 = wordnet.synset('aids.n.01')
# w2 = wordnet.synset('disease.n.01')
# print(syn1.wup_similarity(w2))

# synonyms = []
# for syn in wordnet.synsets('health'):
#     # for l in syn.lemmas():
#     #     synonyms.append(l.name())
#     print(syn.lemma_names())
# print(set(synonyms))

# import spacy
# nlp = spacy.load('en_core_web_lg')
#
# result = []
# for i in text.strip().split(' '):
#     if i in list(nlp.vocab.strings):
#         result.append(i)
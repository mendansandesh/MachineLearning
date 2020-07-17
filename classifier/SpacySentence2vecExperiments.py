import spacy
#nlp = spacy.load('en_core_web_lg')
nlp = spacy.load('en')
# target = nlp('https://www.amazon.in/gp/product/B07S6P5FQ3/ref=ox_sc_act_title_6?smid=A2VQOLRW0XTGMB&psc=1')
#
# category1 = nlp('health disease hospital patient doctor ward')
# category2 = nlp('authentication login logout signin signout password username credentials')
# category3 = nlp('purchase buy sell pay cart transaction product')
#
# print(target.similarity(category1))
# print(target.similarity(category2))
# print(target.similarity(category3))

target = nlp("Cats are beautiful animals.")

# doc1 = nlp("Dogs are awesome.")
# doc2 = nlp("Some gorgeous creatures are felines.")
# doc3 = nlp("Dolphins are swimming mammals.")
#
# print(target.similarity(doc1))  # 0.8901765218466683
# print(target.similarity(doc2))  # 0.9115828449161616
# print(target.similarity(doc3))  # 0.7822956752876101
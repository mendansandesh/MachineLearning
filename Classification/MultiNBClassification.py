from sklearn.datasets import fetch_20newsgroups

categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
# import sklearn.datasets as skd
# news_train = skd.load_files('/path_to/Fetch20newsgroup/train', categories=categories, encoding='ISO-8859-1')
# news_test = skd.load_files('/path_to/Fetch20newsgroup/test/', categories=categories, encoding='ISO-8859-1')

news_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True)
news_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True)

print "\n"
for idx, val in enumerate(news_train.target_names):
    print "Index ", idx, ": ", val

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_tf = count_vect.fit_transform(news_train.data)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_tf)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, news_train.target)

doc_new = ['God is love', 'OpenGL gpu is fast']
X_new_count = count_vect.transform(doc_new)
X_new_tfidf = tfidf_transformer.transform(X_new_count)
predicted = clf.predict(X_new_tfidf)


print "\n"
for i in range(0, len(doc_new)):
    print "Predicted index for test input ", doc_new[i], "is ", predicted[i]



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import sklearn.datasets as skd

categories = ['chemistry', 'health', 'purchase']
news_train = skd.load_files('/home/inct-sandeshmendan/PycharmProjects/Clustering/inputDir', categories=categories, encoding='ISO-8859-1')

print news_train['target_names']

texts = news_train.data

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

number_of_clusters = 3
modelkmeans = KMeans(n_clusters=number_of_clusters, init='k-means++', max_iter=900, n_init=1)
modelkmeans.fit(X)

order_centroids = modelkmeans.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

for i in range(number_of_clusters):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind])


testStr = "we should buy only if it is at good rate"
print "\nTest input sentence is: ", testStr

X = vectorizer.transform([testStr])

cluster = modelkmeans.predict(X)[0]


print "\nText belongs to cluster number {0}".format(cluster)
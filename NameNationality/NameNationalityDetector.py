import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

df = pd.read_csv("Names_Dataset.csv")

#print(df.head())
Xfeatures = df['names']
ylabels= df['nationality']


cv = CountVectorizer()
X = cv.fit_transform(Xfeatures)

x_train,x_test,y_train,y_test = train_test_split(X,ylabels,test_size=0.33,random_state=42)

nv = MultinomialNB()
nv.fit(x_train,y_train)

sample2= ["Li","John","Ali","Vladmir"]

vect2 = cv.transform(sample2).toarray()

print(nv.predict(vect2))
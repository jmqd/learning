"""
Adding to 1.py: training of data via sklearn's LinearRegression,
and scoring accuracy.
"""

import keys, math, quandl
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL', api_key=keys.quandl)
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]
df['HL_pct'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close']
df['pct_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']

df = df[['Adj. Close', 'HL_pct', 'pct_change', 'Adj. Volume']]

forecast = 'Adj. Close'
df.fillna(-99999, inplace=True)

lookahead_length = int(math.ceil(0.01 * len(df)))
print(lookahead_length)
df['label'] = df[forecast].shift(-lookahead_length)
df.dropna(inplace = True)

features = np.array(df.drop(['label'], 1))
labels = np.array(df['label'])
features = preprocessing.scale(features)
labels = np.array(df['label'])

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.8)

classifier = LinearRegression(n_jobs = -1)
#classifier = svm.SVR() -- another possible model
classifier.fit(features_train, labels_train)
accuracy = classifier.score(features_test, labels_test)
print(accuracy)

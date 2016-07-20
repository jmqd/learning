"""
Adding to 1.py: training of data via sklearn's LinearRegression,
and scoring accuracy.
"""

import keys, math, quandl, datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

style.use('ggplot')

df = quandl.get('WIKI/GOOG', api_key=keys.quandl)
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]
df['HL_pct'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close']
df['pct_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']

df = df[['Adj. Close', 'HL_pct', 'pct_change', 'Adj. Volume']]

forecast = 'Adj. Close'
df.fillna(-99999, inplace=True)

lookahead_length = int(math.ceil(0.01 * len(df)))
print(lookahead_length)
df['label'] = df[forecast].shift(-lookahead_length)

features = np.array(df.drop(['label'], 1))
features = preprocessing.scale(features)
features = features[:-lookahead_length]
features_lately = features[-lookahead_length:]

df.dropna(inplace = True)
labels = np.array(df['label'])
labels = np.array(df['label'])

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.8)

classifier = LinearRegression(n_jobs = -1)
#classifier = svm.SVR() -- another possible model
classifier.fit(features_train, labels_train)
accuracy = classifier.score(features_test, labels_test)

forecast_set = classifier.predict(features_lately)
print(forecast_set, accuracy, lookahead_length)
df['Forecast'] = np.nan

#this is totally hacky
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()










"""
Connecting to quandl, querying a dataset, and very elementary operations to
the dataframe.
"""

import keys, math, quandl
import pandas as pd

df = quandl.get('WIKI/GOOGL', api_key=keys.quandl)
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume',]]
df['HL_pct'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close']
df['pct_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']

df = df[['Adj. Close', 'HL_pct', 'pct_change', 'Adj. Volume']]

forecast = 'Adj. Close'
df.fillna(-99999, inplace=True)

lookahead_length = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast].shift(-lookahead_length)
df.dropna(inplace = True)
print(df.head())

import quandl
import pandas as pd

# yes, I know I published my API keys... we all type git push origin master
# too quickly from time to time... needless to say, I have changed my api keys
quandl.ApiConfig.api_key = 'joPSdv8a2s7kszCLosBz'
quandl.ApiConfig.api_version = '2015-04-09'

def in_usd(date, amount, currency):
    data = quandl.get('CURRFX/{}USD'.format(currency))
    row = data.loc[date, 'Rate']
    return row * amount

date = str(input("Date: "))
amount = float(input("Amount: "))
currency = str(input("Currency: "))


print(in_usd(date, amount, currency))


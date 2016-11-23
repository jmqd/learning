import quandl
import pandas as pd
import secret_file

quandl.ApiConfig.api_key = secret_file.api_key
quandl.ApiConfig.api_version = '2015-04-09'

def in_usd(date, amount, currency):
    data = quandl.get('CURRFX/{}USD'.format(currency))
    row = data.loc[date, 'Rate']
    return row * amount

date = str(input("Date: "))
amount = float(input("Amount: "))
currency = str(input("Currency: "))


print(in_usd(date, amount, currency))


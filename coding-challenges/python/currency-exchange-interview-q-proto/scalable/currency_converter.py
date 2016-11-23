import datetime, quandl, secret_file, pandas as pd, csv, sys, pickle, argparse
import numpy as np

quandl.ApiConfig.api_key = secret_file.api_key
quandl.ApiConfig.api_version = '2015-04-09'

def parse_args():
    parser = argparse.ArgumentParser(description='Transform those currencies. :)')
    parser.add_argument('csv', type=str, help='csv of row_id, date, currency_code, amount')
    args = parser.parse_args()
    return args


def load_tables():
    rate_table = {}
    with open('currencies.csv', 'r') as currencies:
        reader = csv.reader(currencies)
        for row in reader:
            rate_table[row[0]] = quandl.get('CURRFX/{}USD'.format(row[0]))
            print("Saved {} rate table as pickle...".format(row[0]))
    return rate_table

def in_usd(date, amount, table):
    try:
        rate = table.loc[date, 'Rate']
    except KeyError:
        # if the date is missing from the API data, get the
        # average of the two adjacent rows
        date_format = '%Y-%m-%d'
        date = datetime.datetime.strptime(date, date_format)
        day_before = date - datetime.timedelta(days = 1)
        day_after = date + datetime.timedelta(days = 1)
        before = table.loc[day_before.strftime(date_format), 'Rate']
        after = table.loc[day_after.strftime(date_format), 'Rate']
        rate = (before + after) / 2
    return float(rate * amount)

#
# uncomment this if you need to regenerate the rate-tables
# or add more currencies.
#
# rate_table = load_tables()
# save_location = open('rate_tables/table.p', 'wb')
# pickle.dump(rate_table, save_location)
# sys.exit(0)
#

def transform(csv):
    with open('rate_tables/table.p', 'rb') as f:
        rates = pickle.load(f)
    output = np.array(['row_id', 'date', 'currency', 'amount', 'in_usd'])
    for row in csv:
        row_id = row[0]
        date = row[1]
        currency = row[2]
        amount = float(row[3])
        usd_amount = in_usd(date, amount, rates[currency])
        output = np.vstack([output, [row_id, date, currency, amount, usd_amount]])
    return output

def main():
    args = parse_args()
    with open(args.csv, 'r') as f:
        reader = csv.reader(f)
        csv = list(reader)

    output = transform(csv)
    print(output)

    np.savetxt('transform.tsv', output, delimiter = '\t', fmt = '%10s', newline = '\n')


if __name__ == '__main__':
    main()

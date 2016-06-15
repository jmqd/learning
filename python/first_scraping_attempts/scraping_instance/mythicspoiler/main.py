from Card import *
import csv

errors = [('edition', 'title', 'error')]

with open("input.csv", 'r') as images_to_download:
    reader = csv.reader(images_to_download, delimiter = ',', quotechar = '"')
    reader.__next__()
    for row in reader:
        args = {
            'edition': row[0].strip(),
            'title': row[1].strip(),
            'static': row[2] if row[2] else None,
            }
        card = Card(**args)
        card.download()
        errors += card.errors
for item in errors:
    print(item)


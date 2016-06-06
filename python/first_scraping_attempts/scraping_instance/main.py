from Card import *
import csv

with open("input.csv", 'r') as missing_images:
    reader = csv.reader(missing_images, delimiter = ',', quotechar = '"')
    reader.__next__()
    for row in reader:
        args = {
            'edition': row[0].strip(),
            'title': row[1].strip(),
            'static': row[2] if row[2] else None,
            }
        card = Card(**args)
        card.download()
for item in errors:
    print(item)


from Card import *
from PIL import Image
import csv, pprint, time, os
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description = "Given a WotC URL, will scrape, crop, and correctly name the card images. This script makes a very important assumption: That the alt text on the images is the correct name of the magic card.")
parser.add_argument("-e", "--edition", help = "The name of the magic edition at the URL. e.g. \"Champions of Kamigawa\"")
parser.add_argument("-u", "--url", help = "The url where the images are.")
args = parser.parse_args()

errors = [('edition', 'title', 'error')]


new_origin = (10, 9)
new_directory = None
try:
    req = urllib.request.Request('http://magic.wizards.com/en/articles/archive/card-image-gallery/eternal-masters')
    req.add_header('User-agent',
                'Python 3.4.3; Jordan M.; jmcqueen@cardkingdom.com')
    response = urllib.request.urlopen(req)
    wotc = urllib.request.urlopen(req).read()
    response.close()
except Exception as error:
    print("-- ", error)
    self.errors.append((self.edition, self.title, self.url, error))
finally:
    try:
        response.close()
    except NameError:
        pass
wotc = BeautifulSoup(wotc, 'html.parser')
for image in wotc.find_all('img', alt=True):
    if image.get('style') == 'width: 265px; height: 370px;':
        print(image.get('src'))
        dict_args = {
            'title': image.get('alt'),
            'edition': args.edition,
            'url': image.get('src'),
            }
        card = Card(**dict_args)
        card.download()
        if not new_directory:
            old_directory = card.directory
            new_directory = "cropped-{}".format(old_directory)
            os.makedirs(new_directory)
        filename = card.save_location
        img = Image.open(filename)
        width = img.size[0]
        height = img.size[1]
        if height != 370:
            print("-- {}".format(file))
            errors.append("wrong img size {}".format(file))
            continue
        cropped_img = img.crop(
            (
                new_origin[0],
                new_origin[1],
                245 + new_origin[0],
                352 + new_origin[1],
            )
        )
        save_location = "{}/{}".format(new_directory, card.filename)
        cropped_img.save(save_location)

for item in errors:
    print(item)


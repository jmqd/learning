from Card import *
import csv, pprint
from bs4 import BeautifulSoup

errors = [('edition', 'title', 'error')]

def is_magic_card_image(img):
    return img and img.has_attr('alt')

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

for image in wotc.find_all(img=is_magic_card_image):
    print(image.get('alt'), image.get('src'))
for item in errors:
    print(item)


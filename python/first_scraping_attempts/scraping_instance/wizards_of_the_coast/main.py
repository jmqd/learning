from Card import *
import csv, pprint, time
from bs4 import BeautifulSoup

errors = [('edition', 'title', 'error')]


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
            'edition': 'Eternal Masters',
            'url': image.get('src'),
            }
        card = Card(**dict_args)
        card.download()
for item in errors:
    print(item)


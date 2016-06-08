from Card import *
import csv, pprint, time
from bs4 import BeautifulSoup

errors = [('edition', 'title', 'error')]
set_code = 'SOI'

try:
    req = urllib.request.Request('https://deckmaster.info/set.php?shortcode={}'.format(set_code))
    req.add_header('User-agent',
                'Python 3.4.3; Jordan M.; jmcqueen@cardkingdom.com')
    response = urllib.request.urlopen(req)
    page = urllib.request.urlopen(req).read()
    response.close()
except Exception as error:
    print("-- ", error)
finally:
    try:
        response.close()
    except NameError:
        pass
page = BeautifulSoup(page, 'html.parser')
for li in page('li'):
    card = li.find_next('span')
    img = card.find_next('img')
    img_src = img.get('src')
    try:
        img_split = img_src.split('/')
        img_filename = img_split[6] #6th index = e.g. 323141.jpg
        if img_filename[0] == '-': #firstchar of hyphen means crappy image
            continue
        else:
            high_res = img_filename.split('.')[0] + "-hr" + ".jpg"
            img_split[6] = high_res
            img_src = '/'.join(img_split)

    except Exception as e:
        print(e)
        continue
    title = img.find_next('span').get_text()
    lands = ['Forest', 'Mountain', 'Plains', 'Swamp', 'Island']
    if not any(land == title.strip().split(' ')[0] for land in lands):
        title = title.split('(')[0]
    dict_args = {
        'title': title,
        'edition': 'Shadows over Innistrad',
        'url': img_src,
        }
    card = Card(**dict_args)
    card.download()
for item in errors:
    print(item)


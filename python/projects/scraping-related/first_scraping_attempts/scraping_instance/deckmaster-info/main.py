from Card import *
import csv, pprint, time
from bs4 import BeautifulSoup

errors = [('edition', 'title', 'error')]
set_code = 'ORI'
edition = 'Magic Origins'
stopping_point = "Gideon's Phalanx (014 Prerelease)"


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
    is_token = False
    try:
        img_split = img_src.split('/')
        img_filename = img_split[6] #6th index = e.g. 323141.jpg
        if img_filename[0] == '-': #firstchar of hyphen means token (currently)
            is_token = True
        high_res = img_filename.split('.')[0] + "-hr" + ".jpg"
        img_split[6] = high_res
        img_src = '/'.join(img_split)

    except Exception as e:
        print(e)
        continue
    title = img.find_next('span').get_text()
    if title == stopping_point:
        break
    lands = ['Forest', 'Mountain', 'Plains', 'Swamp', 'Island', 'Wastes']
    if not any(land == title.strip().split(' ')[0] for land in lands):
        title_array = title.split(" (")
        variation = title_array[-1].replace(')', '').strip()
        title = title.split('(')[0].strip()
        if is_token:
            title = "{}-token-{}".format(title, variation)
        if ' '.join(title.strip().split(' ')[0:2]) == 'Eldrazi Scion-token':
            title = title + '-' + variation
        if title.strip().split(' ')[0] == 'Elemental-token':
            title = title + '-' + variation

    dict_args = {
        'title': title,
        'edition': edition,
        'url': img_src,
        }
    card = Card(**dict_args)
    card.download()
for item in errors:
    print(item)


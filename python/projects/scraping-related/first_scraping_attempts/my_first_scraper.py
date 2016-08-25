import urllib.request
import os
import re
import csv
import time
from urllib.parse import quote
import shutil

image_regex = re.compile(b'<img\ssrc="http:\/\/magiccards.info\/scans\/en\/[a-z0-9]*\/[0-9]*.jpg')
image_many_arts_regex = re.compile(b'<img\ssrc="http:\/\/magiccards.info\/scans\/en\/[a-z0-9]{1,}\/[0-9]{1,}b.jpg')
regex = re.compile('[:,\.!\'?/]')
url_error_list = []
abbv = {}
not_in_dict_list = []

#alternate_editions = ['ugin', 'ptc', 'gpx', 'grc', 'clash', '15ann', 'pro', 'mgdc', 'wrl', 'wmcq', 'drc', 'rep', 'mlp', 'sum', 'cp', 'arena', 'fnmp', 'mprp', 'sus', 'hho', 'jr', 'pot', 'wotc', 'uqc', 'dcilm']
alternate_editions = ['9eb']
with open("abbv.txt", 'r') as abbv_file:
    for row in abbv_file:
        row_list = row.split(" // ")
        abbv[row_list[0].strip()] = row_list[2].strip().lower()

def slug(string):
    string = string.strip()
    string = string.replace(" ", "-").lower()
    string = regex.sub('', string)
    string = re.sub(r"([-]){2,}", "-", string)
    return string

def card_query(edition, title, card_type=None):
    def main_query(edition, title):
        query = quote("{} e:{}/en".format(title, edition))
        request = "http://magiccards.info/query?q={}&v=card&s=cname".format(query)
        try:
            with urllib.request.urlopen(request) as response:
                query_result = response.read()
        except Exception as e:
            print("--")
            url_error_list.append((edition, title))
            image = None
            if response:
                response.close()
        if card_type not in ("split_card", "flip_card"):
            image = image_regex.findall(query_result)
        if card_type in ("split_card", "flip_card"):
            image = image_many_arts_regex.findall(query_result)
        if len(image) > 1 and card_type not in ("split_card", "flip_card"):
            return 'ambiguous'
        if image:
            image = image[0][10:]
            return image
    image = main_query(edition, title)
    if image == 'ambiguous':
        url_error_list.append((edition, title, 'ambiguous_query'))
    if not image:
        for alternate_edition in alternate_editions:
            image = main_query(alternate_edition, title)
            if image:
                break
    if not image:
        url_error_list.append((edition, title))
        return 'no_match'
    return image


def create_request(card_type, edition, title, variation, number=None):
    if number:
        request = "http://www.magiccards.info/scans/en/{}/{}.jpg".format(abbv[edition], number)
    elif card_type in ['card', 'split_card', 'flip_card']:
        if card_type == 'split_card':
            title = title.replace('-', ' ')
        if edition in corrected_editions:
            edition = corrected_editions[edition]
        request = card_query(abbv[edition], title, card_type)
        if request == 'no_match':
            return 'query_error'
    elif card_type:
        if card_type == 'token' and variation:
            return 'query_error'
        elif card_type == 'token':
            request = "http://www.magiccards.info/extras/{}/{}/{}.jpg".format(card_type, slug(edition), slug(title))
        else:
            request = "http://www.magiccards.info/extras/{}/{}/{}.jpg".format(card_type, slug(edition), slug(title))
    return request


def make_save_location(card_type, edition, title, language, variation=None):
    if not variation:
        save_location = '../__init__website_images/{}/{}/{}.jpg'.format(slug(edition), language, slug(title))
    elif variation and card_type == 'extra':
        variation = variation.replace('/', ' ')
        save_location = '../__init__website_images/{}/{}/{}-{}.jpg'.format(slug(edition), language, slug(title), slug(variation))
    elif variation and card_type != 'extra':
        save_location = '../__init__website_images/{}/{}/{}-{}.jpg'.format(slug(edition), language, slug(title), slug(variation))
    return save_location

corrected_editions = {
    "4e" : "4eb"
        }

def gimme_dat_image(request, edition, title, save_location):
    try:
        req = urllib.request.Request(request)
        req.add_header('User-agent', 'Python 3.4.3; Jordan McQueen; jmcqueen@cardkingdom.com')
        with urllib.request.urlopen(req) as response, open(save_location, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            print("++ ", save_location)
            response.close()
    except urllib.error.HTTPError as he:
        print("--", he)
        url_error_list.append((edition, title, he, request))
    except Exception as e:
        print("--", e)
        url_error_list.append((e, edition, title))
    finally:
        try:
            response.close()
        except NameError:
            pass


languages = ('jp', 'de', 'fr', 'it', 'pt', 'cn', 'jp', 'ru', 'tw', 'ko')
unprinted = {
        "jp" : ["4th Edition", "5th Edition", "6th Edition", "7th Edition", "8th Edition"],
        "de" : ["4th Edition"],
        "fr" : ["4th Edition"],
        "it" : ["4th Edition"],
        "cn" : ["4th Edition"],
        "tw" : ["4th Edition"],
        "pt" : [],
        "ru" : ["4th Edition"],
        "ko" : ["4th Edition"]
        }


def do_scraping(card_type, edition, title, variation=None, number=None):
    my_first_rodeo = True
    for language in languages:
        if edition in unprinted[language]:
            print("Skipped: ", (language, edition))
            continue
        print(edition)
        save_location = make_save_location(card_type, edition, title, language, variation)
        if os.path.isfile(save_location):
            print("++ (already saved) ", save_location)
            continue
        directory= "../__init__website_images/{}/{}/".format(slug(edition), language)
        os.makedirs(directory, exist_ok=True)
        if my_first_rodeo:
            request = create_request(card_type, edition, title, variation, number)
            if not isinstance(request, str):
                request = request.decode('utf-8')
        if request in ("query_error", "ambiguous"):
            print ((edition, title, language, "query_error or ambiguous"))
            continue
        request = request.split("/")
        print(request)
        if request[5] in corrected_editions:
            request[5] = corrected_editions[request[5]]
        request[4] = language
        request = "/".join(request)
        time.sleep(3)
        gimme_dat_image(request, edition, title, save_location)
        my_first_rodeo = False



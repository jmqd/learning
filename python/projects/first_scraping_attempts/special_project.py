import urllib.request
import os
import re
import csv
import time
from urllib.parse import quote
import shutil

image_regex = re.compile(r"\" src=\"http://deckmaster.info/images/cards/ORI/[0-9]{1,}.jpg")
name_regex = re.compile(r"[-a-z',A-Z]{1,}([ ,-][a-zA-Z]{0,}){0,} \([0-9]{3}Prerelease\)")
regex = re.compile('[:,\.!\'?/]')

def slug(string):
    string = string.strip()
    string = string.replace(" ", "-").lower()
    string = regex.sub('', string)
    string = re.sub(r"([-]){2,}", "-", string)
    return string

headers = {}
def do_scraping(title, image_url):
    save_location = "../__init__website_images/promotional/{}-prerelease-foiljpg".format(slug(title))
    if os.path.isfile(save_location):
        print("++ (already saved) ", save_location)
        return 'already_exists'
    request = image_url
    try:
        req = urllib.request.Request(request)
        req.add_header('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko20071127 Firefox/2.0.0.11')
        with urllib.request.urlopen(req) as response, open(save_location, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        print("++ ", save_location)
        time.sleep(5)
    except urllib.error.HTTPError as he:
        print("--", he)
        time.sleep(5)
    except Exception as e:
        print("--", e)


with open("list.txt", 'r') as scrape_list:
    for row in scrape_list:
        title = name_regex.search(row)
        image_src = image_regex.search(row)
        if title and image_src:
            image_src = image_src.group(0)[7:]
            title = title.group(0)
            title = title.split('(')
            title = title[0].strip()
            card = (title, image_src)
            do_scraping(title, image_src)



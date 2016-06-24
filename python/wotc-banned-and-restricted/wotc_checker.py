from bs4 import BeautifulSoup
import urllib.request

errors = []
value = 0
try:
    req = urllib.request.Request('http://magic.wizards.com/en/rss/rss.xml')
    req.add_header('User-agent',
                'Python 3.4.3; Jordan M.; jmcqueen@cardkingdom.com')
    response = urllib.request.urlopen(req)
    wotc = urllib.request.urlopen(req).read()
    response.close()
except Exception as error:
    errors.append(error)
finally:
    try:
        response.close()
    except NameError:
        pass
wotc = BeautifulSoup(wotc, 'html.parser')
for item in wotc.find_all('item'):
    title = item.title.get_text().lower()
    if 'banned' in title or 'restricted' in title:
        value = 1
if value == 1:
    print("True")
else:
    print("False")

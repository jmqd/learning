import sys, urllib.request, json, pprint, csv
from datetime import date

try:
    req = urllib.request.Request('http://mtgjson.com/json/SetList.json')
    req.add_header('User-agent',
                'Python 3.4.3; Jordan M.; jmcqueen@cardkingdom.com')
    response = urllib.request.urlopen(req)
    set_list = urllib.request.urlopen(req).read().decode()
    response.close()
except Exception as error:
    print("-- ", error)
finally:
    try:
        response.close()
    except NameError:
        pass
set_list = json.loads(set_list)
set_dict = {}
with open('set-list-{}.tsv'.format(date.today()), 'w', newline = '\n') as tsv:
    writer = csv.writer(tsv, delimiter = '\t')
    writer.writerow(['name', 'code', 'release_date'])
    for edition in set_list:
        writer.writerow([edition['name'],
                         edition['code'],
                         edition['releaseDate'],])
        set_dict[edition['name']] = {
            'code': edition['code'],
            'release_date': edition['releaseDate'],
            }
pprint.pprint(set_dict, indent=3)

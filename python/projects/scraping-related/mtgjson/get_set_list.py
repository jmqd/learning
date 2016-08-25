import sys, urllib.request, json, pprint, csv
from datetime import date

def get_url(url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-agent',
                    'Python 3.4.3; Jordan M.; jmcqueen@cardkingdom.com')
        response_object = urllib.request.urlopen(req)
        response = response_object.read().decode()
    except Exception as error:
        print("-- ", error)
    finally:
        try:
            response_object.close()
        except NameError:
            pass
    return response


def write_to_tsv(list_of_dicts, name = 'set-list'):
    filename = '{}-{}.tsv'.format(name, date.today())
    with open(filename, 'w', newline = '\n') as tsv:
        writer = csv.writer(tsv, delimiter = '\t')
        # statically programmed for this instance -- I want a specific order
        writer.writerow(['name', 'code', 'release_date'])
        for edition in list_of_dicts:
            writer.writerow([edition['name'],
                             edition['code'],
                             edition['releaseDate'],])
    return True

# specific stuff...
url = "http://mtgjson.com/json/SetList.json"

json_string = get_url(url)
list_of_dicts = json.loads(json_string)
write_to_tsv(list_of_dicts)

pprint.pprint(list_of_dicts, indent=2)

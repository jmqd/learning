import secrets, pprint, requests, json
from datetime import datetime

# testing config stuff -- prod will look different, of course
def init_testing_environment():
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    lat = input("Enter latitude > ")
    lng = input("Enter longitude > ")

    # in this particular application, we're primarily interested in lakes,
    # rivers, streams, etc... type :: 'natural_feature' in Google's API.
    loc_type = "natural_feature"

    parameters = {
        'url': url,
        'location': "{},{}".format(lat, lng),

        # testing value. this may need tweaking or additional logic
        # later on down the line, in case of failure to find place.
        'radius': 1,
        'type': loc_type,
        'key': secrets.api_key,
            }
    return parameters

def query_google_places_api(parameters):
    # we pop the url so as to not include it while generating the query string
    url = parameters.pop('url')

    # constructs the query string from the remaining parameters
    url += ''.join(["&{}={}".format(k, v) for k, v in parameters.iteritems()])

    reverse_lookup = requests.get(url)
    return reverse_lookup


def display_results(results):
    for result in results.json()['results']:
        pprint.pprint(result['name'], indent = 4)

# procedural controller execution
parameters = init_testing_environment()
results = query_google_places_api(parameters)
display_results(results)

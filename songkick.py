'''
all songkick functions
'''
import requests


import config
from util import get_date

API_KEY = config.SONGKICK_API_KEY

# TO DO
# Try location with IP address

def get_events(location, start, end):
    '''
    wrapper function
    '''
    return get_artists(get_location_id(location), location, start, end)


def get_location_id(location):
    '''
    get location ID given a location
    '''
    request = 'https://api.songkick.com/api/3.0/search/locations.json?query={}&apikey={}'.format(
        location, API_KEY)
    response = requests.get(request)
    for place in response.json()['resultsPage']['results']['location']:
        if str(place['city']['displayName']).lower() == location.lower():
            return place['metroArea']['id']
    return None


def get_artists(location_id, location, start, end):
    '''
    get events given a location ID
    '''
    artists = set()
    latest_date = start
    end_date = end
    page_number = 1

    while latest_date < end_date:
        response = get_response(location_id, page_number)

        for event in response['resultsPage']['results']['event']:
            if location.lower() in str(event['location']['city']).lower():
                if event['start']['datetime']:
                    date = get_date(event['start']['datetime'][:10])
                    if latest_date < date:
                        latest_date = get_date(event['start']['datetime'][:10])
                    if event['performance']:
                        artists.add(
                            event['performance'][0]['artist']['displayName'])
        page_number += 1

    return list(artists)


def get_response(location_id, page_number):
    '''
    get response from songkick api
    '''
    parameters = {"page": page_number}
    request = 'https://api.songkick.com/api/3.0/metro_areas/{}/calendar.json?apikey={}'.format(
        location_id, API_KEY)
    response = requests.get(request, params=parameters)
    return response.json()


#if __name__ == '__main__':
#    LOCATION_ID = get_location_id('philadelphia')
#    print(get_events(LOCATION_ID, 'philadelphia', '2019-02-08', '2019-02-10'))

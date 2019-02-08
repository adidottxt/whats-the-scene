'''
all songkick functions
'''
import requests

import config

API_KEY = config.SONGKICK_API_KEY

# TO DO
# Take in location
# Do location search in Songkick to get metro area / city
# https://www.songkick.com/developer/location-search
# - Try this with both text + IP address
# Get list of metro area's upcoming events
# https://www.songkick.com/developer/upcoming-events-for-metro-area


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

def get_events(location_id):
    '''
    get events given a location ID
    '''
    request = 'https://api.songkick.com/api/3.0/metro_areas/{}/calendar.json?apikey={}'.format(
        location_id, API_KEY)
    response = requests.get(request)
    print(response.json())


if __name__ == '__main__':
    get_events(get_location_id('philadelphia'))

'''
Log in log off
'''

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import config

USERNAME = config.CLIENT_USERNAME

ARTISTS = ['four tet']

def login_to_spotify(client_id, client_secret):
    '''
    This handles logging in to Spotify and returning a Spotipy object
    to be used to gather our data
    '''

    os.environ['SPOTIPY_CLIENT_ID'] = client_id
    os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
    os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback/'

    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    spotify = spotipy.Spotify(
        client_credentials_manager=client_credentials_manager)

    return spotify


def create_playlist(spotify_object, artists, week):
    new_playlist = spotify_object.user_playlist_create(
        USERNAME, name=week, description="test")

    for artist in artists:
        result = spotify_object.search(artist, type='artist')
        print(result)

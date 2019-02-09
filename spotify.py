'''
spotipy functions
'''

from random import shuffle

import spotipy
from spotipy import util


def login_to_spotify(client_username, client_id, client_secret):
    '''
    This handles logging in to Spotify and returning a Spotipy object
    to be used to gather our data
    '''

    scope = 'user-follow-modify playlist-modify-public \
        playlist-read-private'

    token = util.prompt_for_user_token(
        username=client_username,
        scope=scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri='http://localhost:8888/callback/')

    spotify = spotipy.Spotify(auth=token)

    return spotify


def create_playlist(spot_obj, username, artists, week):
    '''
    Create a playlist with top songs from artists
    '''
    if get_playlist_id(spot_obj, username, week) is None:
        new_playlist = spot_obj.user_playlist_create(  # pylint: disable=unused-variable
            username,
            week,
        )

    new_playlist_id = get_playlist_id(spot_obj, username, week)

    tracks = []
    dup_artists = set()

    shuffle(artists)

    for artist in artists:
        for item in spot_obj.search(artist, type='artist')['artists']['items']:
            if item['name'].lower() == artist.lower() and \
                    item['name'].lower() not in dup_artists:
                i = 0
                dup_artists.add(item['name'].lower())
                a_id = item['id']
                try:
                    while spot_obj.artist_top_tracks(
                            a_id)['tracks'][i]['artists'][0]['name'].lower() \
                            != artist.lower():
                        i += 1
                    print("Adding song: ", spot_obj.artist_top_tracks(
                        a_id)['tracks'][i]['name'])
                    tracks.append(spot_obj.artist_top_tracks(
                        a_id)['tracks'][i]['id'])
                except LookupError:
                    continue

    spot_obj.user_playlist_add_tracks(username, new_playlist_id, tracks)
    print("success! done adding tracks to playlist")


def get_playlist_id(spot_obj, username, playlist_name):
    '''
    get playlist id bc spotify's api is odd
    '''
    playlists = spot_obj.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'].lower() == playlist_name.lower():
            return playlist['id']

    print("no playlist found, creating playlist")
    return None

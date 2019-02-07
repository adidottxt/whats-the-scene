'''
Running things
'''
import config
from spotify import login_to_spotify, create_playlist
from util import get_week

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
CLIENT_USERNAME = config.CLIENT_USERNAME

ARTISTS = ['four tet', 'jon hopkins', 'jamie xx', 'caribou', 'mall grab']

if __name__ == '__main__':
    SPOTIFY_OBJECT = login_to_spotify(CLIENT_USERNAME, CLIENT_ID, CLIENT_SECRET)
    WEEK = get_week()
    create_playlist(SPOTIFY_OBJECT, CLIENT_USERNAME, ARTISTS, WEEK)

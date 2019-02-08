'''
Running things
'''
import config
from spotify import login_to_spotify, create_playlist
from util import get_today, get_three_days, get_week
from songkick import get_events

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
CLIENT_USERNAME = config.CLIENT_USERNAME

# ARTISTS = ['four tet', 'jon hopkins', 'jamie xx', 'caribou', 'mall grab']

if __name__ == '__main__':
    SPOTIFY_OBJECT = login_to_spotify(
        CLIENT_USERNAME, CLIENT_ID, CLIENT_SECRET)

    WEEK = get_week()
    TODAY = get_today()
    THREE = get_three_days()

    ARTISTS = get_events('philadelphia', TODAY, THREE)
    create_playlist(SPOTIFY_OBJECT, CLIENT_USERNAME, ARTISTS, WEEK)

'''
Running things
'''
import config
from spotify import login_to_spotify, create_playlist
from util import get_days, get_title
from songkick import get_events

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
CLIENT_USERNAME = config.CLIENT_USERNAME

if __name__ == '__main__':
    SPOTIFY_OBJECT = login_to_spotify(
        CLIENT_USERNAME, CLIENT_ID, CLIENT_SECRET)

    COUNT = 2

    TITLE = get_title('philadelphia', COUNT)
    START, END = get_days(COUNT)

    ARTISTS = get_events('philadelphia', START, END)
    create_playlist(SPOTIFY_OBJECT, CLIENT_USERNAME, ARTISTS, TITLE)

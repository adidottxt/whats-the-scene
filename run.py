'''
Running things
'''
from login import login_to_spotify
import config

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET

if __name__ == '__main__':
    SPOTIFY_OBJECT = login_to_spotify(CLIENT_ID, CLIENT_SECRET)

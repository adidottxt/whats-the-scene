# 🎶 What's the scene?

Automated Spotify playlist creation based on who's playing in your town using 
Spotify and Songkick APIs.

This project is currently a work in progress.

### Requirements + How To Run:
- Install `spotipy` and `requests` using the requirements.txt file. This 
  can be done by running the command `pip install -r requirements.txt`. 
  Ideally, this is done within a virtual environment.
- Ensure that you have a Songkick API key and a Spotify API client ID, 
  secret, and your Spotify username. These must be put into a `config.py` file 
  in the same folder as `run.py`, in the following format:

  ```python
  CLIENT_ID = 'insert-your-client-id-as-a-string-here'
  CLIENT_SECRET = 'insert-your-client-secret-as-a-string-here'
  CLIENT_USERNAME = 'insert-your-spotify-username-here'
  SONGKICK_API_KEY = 'insert-your-songkick-api-key-here'
  ```

- For more information on the Spotify API, click [here](https://developer.spotify.com/).
- For more information on the Songkick API, click [here](https://www.songkick.com/developer).
- Run `run.py` with your city as the sole argument. For example, if you live 
  in Philadelphia, `python run.py philadelphia`.
- The current setup only creates a playlist for artists playing in your 
  city for the next two days. This can be adjusted by adding another 
  argument to your command line statement. For example, if you want a 
  playlist for the next week, use `python run.py philadelphia 7`.

### Project To-Dos:
- <b>Error handling for user input.</b>
- <b>Spotify</b>
  * Ensure songs are not duplicated in a playlist
  * Ensure each playlist is of a certain size
  * Pick songs from top songs at random (this is a debatable feature)


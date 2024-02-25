import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from config import *

def setup_credentials():
    scope = 'user-read-currently-playing user-modify-playback-state'
    sp_oauth = SpotifyOAuth(scope=scope, 
                            username=username,
                            client_id = client_id,
                            client_secret = client_secret,
                            redirect_uri=redirect_uri)

    # Obtain the access token using the embedded browser
    token_info = sp_oauth.get_cached_token()

    if not token_info:
        # Prompt the user to authenticate and authorize the application
        auth_url = sp_oauth.get_authorize_url()
        print(f"Please visit this URL to authorize the application: {auth_url}")

        # Wait for the user to complete the authentication process
        response = input("Enter the URL you were redirected to: ")
        code = sp_oauth.parse_response_code(response)

        # Exchange the authorization code for a token
        token_info = sp_oauth.get_access_token(code)

    token = token_info['access_token']
    sp = spotipy.Spotify(auth=token)
    
    return sp


def unpause_song(uri):
    """
    unpauses the currently playing song at the beginning
    """
    sp = setup_credentials()
    sp.start_playback(uris = [uri])


def pause_song():
    """
    pauses the currently playing song
    """
    sp = setup_credentials()
    sp.pause_playback()


def skip_song():
    """
    Skips the currently playing song
    """
    sp = setup_credentials()
    sp.next_track()


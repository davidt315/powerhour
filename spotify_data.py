import spotipy
import spotipy.util as util
from config import *

def setup_credentials():
    """
    sets up all the credentials needed for data and to pause/play and returns it
    """
    if 'sp' not in globals():
        scopes = 'user-read-currently-playing user-modify-playback-state'
        token = util.prompt_for_user_token( username,
                                            scopes,
                                            client_id = client_id,
                                            client_secret = client_secret,
                                            redirect_uri = redirect_uri)
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


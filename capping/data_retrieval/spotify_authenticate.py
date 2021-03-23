import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def authenticate():
    try:
        Spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    except Exception as e:
        print("[*] Could Not Authenticate.\n", e)
    return Spotify

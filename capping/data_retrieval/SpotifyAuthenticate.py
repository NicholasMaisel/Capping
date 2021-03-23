import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def authenticate():
    Spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    return Spotify 

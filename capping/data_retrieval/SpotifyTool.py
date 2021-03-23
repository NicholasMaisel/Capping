import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

SPOTIFY = None
TRACK_FEATURES = pd.DataFrame()

def authenticate():
    global SPOTIFY
    SPOTIFY = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    return True

def get_audio_features():
    global TRACK_FEATURES
    # Read Track IDS
    track_ids = pd.read_csv('SpotifyIds.csv')['1'].dropna()

    # Split into chunks
    chunks = [track_ids.loc[i:i + 100] for i in range(1,len(track_ids),100)]

    # Pull audio_features
    for chunk in chunks:
        features = SPOTIFY.audio_features(chunk)
        for track in features:
            TRACK_FEATURES = TRACK_FEATURES.append([list(track.values())])

def main():
    authenticate()
    get_audio_features()
    TRACK_FEATURES.to_csv('audio_features.csv', index = False)


if __name__ == '__main__':
    main()

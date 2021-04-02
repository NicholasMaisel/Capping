from . import spotify_authenticate
import pandas as pd
import config

# Authenticate and create Spotify Connection
SPOTIFY = spotify_authenticate.authenticate()

def get_audio_features(ids_path, out_path):
    global SPOTIFY
    try:
        open(ids_path, 'r')
    except:
        print('[*] datasets/randomids.csv not found. Try running random_spotify_search first.')

    # Read Track IDS
    track_ids = pd.read_csv(ids_path)
    # Split into chunks
    chunks = [track_ids.loc[i:i + 99] for i in range(1,len(track_ids),100)]

    # Pull audio_features
    track_features = pd.DataFrame()

    count1 = 0
    count2 = 100
    for chunk in chunks:
        print('Working on songs: {}-{}'.format(count1,count2))
        features = SPOTIFY.audio_features(list(chunk['id']))
        for track in features:
            if track != None:
                track_features = track_features.append(
                {'danceability': track['danceability'],
                 'energy': track['energy'],
                 'key': track['key'],
                 'loudness': track['loudness'],
                 'mode': track['mode'],
                 'speechiness': track['speechiness'],
                 'acousticness': track['acousticness'],
                 'instrumentalness': track['instrumentalness'],
                 'liveness': track['liveness'],
                 'valence': track['valence'],
                 'tempo': track['tempo'],
                 'id': track['id'],
                 'duration_ms': track['duration_ms'],
                 'time_signature': track['time_signature']
                 }, ignore_index = True)

        count1 = count2
        count2 = count1 + 100

    track_features = track_features.merge(track_ids, on='id')
    track_features.to_csv(out_path, index = None)
    return True

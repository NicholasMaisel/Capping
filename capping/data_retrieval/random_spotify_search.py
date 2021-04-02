from . import spotify_authenticate
import config
import random
import pandas as pd



# Authenticate and create Spotify Connection
SPOTIFY = spotify_authenticate.authenticate()

def random_query():
    random_char = random.choices('abcdefghijklmnopqrstuvwxyz', k = random.randrange(1,4))
    search_query = ''.join(random_char) + '%'
    return(search_query)

def generate_random_ids(num_unqiue = 10000):
    global SPOTIFY
    ids = pd.DataFrame()
    while len(ids) < num_unqiue:
        print('Number of unique tracks:{}'.format(len(ids)))
        results = SPOTIFY.search(q = random_query(), limit = 50, type = 'track')
        for track in results['tracks']['items']:
            ids = ids.append({'name':track['name'],
                            'id':track['id'],
                            'artist_name': track['artists'][0]['name'],
                            'arstist_id': track['artists'][0]['id']}, ignore_index = True)
            ids.drop_duplicates(subset = 'name', inplace = True)
    ids.to_csv(config.random_ids_path, index = None)
    return True

import spotify_authenticate
import random
import pandas as pd

# Authenticate and create Spotify Connection
SPOTIFY = spotify_authenticate.authenticate()

def random_query():
    random_char = random.choices('abcdefghijklmnopqrstuvwxyz', k = random.randrange(1,4))
    search_query = ''.join(random_char) + '%'
    return(search_query)

def generate_random_ids():
    global SPOTIFY
    ids = pd.DataFrame()
    while len(ids)<10000:
        print('Number of unique tracks:{}'.format(len(ids)))
        results = SPOTIFY.search(q = random_query(), limit = 50, type = 'track')
        for track in results['tracks']['items']:
            ids = ids.append({'name':track['name'],
                            'id':track['id'],
                            'artists': track['artists']}, ignore_index = True)
            ids.drop_duplicates(subset = 'name', inplace = True)

    return ids

def main():
    generate_random_ids().to_csv('../datasets/randomids.csv', index = None)

if __name__ == '__main__':
    main()

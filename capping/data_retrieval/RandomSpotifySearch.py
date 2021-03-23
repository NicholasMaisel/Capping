import SpotifyAuthenticate
import random
import pandas as pd

# Authenticate and create Spotify Connection
try:
    SPOTIFY = SpotifyAuthenticate.authenticate()
except:
    print("[*] Could Not Authenticate.")


def random_query():
    random_char = random.choices('abcdefghijklmnopqrstuvwxyz', k = random.randrange(1,4))
    search_query = ''.join(random_char) + '%'
    return(search_query)


def generate_random_ids():
    global SPOTIFY
    ids = []
    for i in range(201):
        print(random_query())
        results = SPOTIFY.search(q = random_query(), limit = 50, type = 'track')
        for track in results['tracks']['items']:
            ids.append(track['id'])

    return ids


def main():
    pd.DataFrame(generate_random_ids(),
                columns =['Spotify_Ids']).to_csv('randomids.csv', index = None)

if __name__ == '__main__':
    main()

from . import spotify_authenticate
import pandas as pd
import config

SPOTIFY = spotify_authenticate.authenticate()
# List of target playlists
target_genres = ['Rock','Pop','Country','Hip Hop','EDM', 'Jazz', 'Classical']

def get_labeled_ids():
    global SPOTIFY
    # Find target genre playlist ids from playlist_ids in intermediate_data
    playlist_ids = pd.read_csv(config.genre_playlist_ids_path)

    labeled_song_ids = pd.DataFrame()
    for genre in target_genres:
        for index, row in playlist_ids[playlist_ids['name'] == "The Sound of " + genre].iterrows():
            temp = SPOTIFY.user_playlist_tracks(user = 'thesoundofspotify',
                                                playlist_id = row['id'])

            for offset in range(0,temp['total'],100):
                print('Working on songs {}-{} of {} for Genre: {}'.format(offset, offset+100,
                                                                  temp['total'], genre.split(' ')[-1]))
                results = SPOTIFY.user_playlist_tracks(user = 'thesoundofspotify',
                                                     playlist_id = row['id'],
                                                     offset = offset)

                for track in [result['track'] for result in results['items']]:
                    labeled_song_ids = labeled_song_ids.append(
                                    {'name':track['name'],
                                     'id':track['id'],
                                     'artist_name': track['artists'][0]['name'],
                                     'arstist_id': track['artists'][0]['id'],
                                     'genre': genre.split(' ')[-1]},
                                     ignore_index = True)

    labeled_song_ids.to_csv(config.labeled_song_ids_path, index = False)

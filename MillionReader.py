import h5py as h5
import glob
import config
import pandas as pd
import json
import re
from os import path

FILE_LIST = []
SONG_IDS = []
SPOTIFY_IDS = pd.DataFrame()

def get_paths():
    global FILE_LIST
    global SONG_IDS
    FILE_LIST = glob.glob('{}/**/*.h5'.format(config.million_song_path), recursive = True)
    return True

def read_song_id():
    global FILE_LIST
    global SONG_IDS
    for file in FILE_LIST:
        SONG_IDS.append(h5.File(file,'r')['metadata']['songs']['song_id'][0].decode('utf-8'))
    return True

def read_spotify_id():
    global SONG_IDS
    global SPOTIFY_IDS
    for song in SONG_IDS:
        with open('{}/{}/{}.json'.format(config.echonest, song[2:4],song),'r') as f:
            temp = json.load(f)
        try:
            spotify_id = re.search('spotify:track:[a-zA-Z0-9_.-]{22}',
                                    str(temp['response']['songs'][0])).group(0)
            SPOTIFY_IDS = SPOTIFY_IDS.append([[song,spotify_id]])
        except:
            SPOTIFY_IDS = SPOTIFY_IDS.append([[song,'']])


def save_data():
    global SPOTIFY_IDS
    # Saves the SPOTIFY_ID DataFrame
    SPOTIFY_IDS.to_csv('SpotifyIds.csv', index = False)

def main():
    get_paths()
    read_song_id()
    read_spotify_id()
    save_data()


if __name__ == '__main__':
    main()

import h5py
import glob
import config


FILE_LIST =[]

def get_paths(ms_path):
    global FILE_LIST
    FILE_LIST = glob.glob('{}/**/*.h5'.format(ms_path), recursive = True)
    return True



def main():
    get_paths(config.million_song_path)
    print(FILE_LIST)


main()

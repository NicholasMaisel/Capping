import sys
import argparse
import data_retrieval
import os
import config

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g',
                        '--generate_random_ids',
                        help='Generates a specified random number spotify songs (default 10000)',
                        const = 10000,
                        nargs = '?',
                        type = int)

    parser.add_argument('-r',
                        '--retrieve_features',
                        help='Generates random spotify songs',
                        const = config.random_ids_path,
                        nargs = '?',
                        type = str)

    args = parser.parse_args()
    if args.generate_random_ids:
        data_retrieval.random_spotify_search.generate_random_ids(args.generate_random_ids)
    if args.retrieve_features:
        data_retrieval.feature_retrieval.get_audio_features(args.retrieve_features)





if __name__ == '__main__':
    main()

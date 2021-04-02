import sys
import argparse
import data_retrieval
import os
import config

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate_random_ids',
                        help='Generates a specified random number spotify songs (default 10000)',
                        const = 10000,
                        nargs = '?',
                        type = int)
    parser.add_argument('--retrieve_random_features',
                        help='Retrieves features for random songs generated in generate_random_ids',
                        action='store_true',
                        default=False)
    parser.add_argument('--retrieve_labeled_ids',
                        help='Pulls songs from identified genre playlists',
                        action='store_true',
                        default=False)
    parser.add_argument('--retrieve_labeled_features',
                        help="Retrieves acousic features for songs from --get_labled_ids",
                        action='store_true',
                        default=False)

    args = parser.parse_args()
    if args.generate_random_ids:
        data_retrieval.random_spotify_search.generate_random_ids(args.generate_random_ids)

    if args.retrieve_random_features:
        data_retrieval.feature_retrieval.get_audio_features(ids_path = config.random_ids_path,
                                                            out_path = config.unlabeled_features_path)
    if args.retrieve_labeled_ids:
        data_retrieval.genre_sample_retrieval.get_labeled_ids()

    if args.retrieve_labeled_features:
        data_retrieval.feature_retrieval.get_audio_features(ids_path = config.labeled_song_ids_path,
                                        out_path = config.labeled_features_path)





if __name__ == '__main__':
    main()

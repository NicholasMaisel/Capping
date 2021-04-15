import lyricsgenius

# input


def lyric_word_counter(artist_list, number_of_songs, word_of_choice):
    for artist in artist_list:
        genius = lyricsgenius.Genius('eQ4wM1lg9zClUNMLGaLFC8tBdOyJP-58AfOHYHKPZIERLSUXpufboLL0MnFUpbpM')
        genius.verbose = False
        genius.remove_section_headers = True
        genius.excluded_terms = ["(Remix)", "(Live)"]
        my_artist = genius.search_artist(artist, max_songs=number_of_songs, sort="popularity")
        song_list = []
        for song in my_artist.songs:
            song_title = song.title
            song_list.append(song_title)

        punctuation = (',', '"', ",", ';', ':', '.', '?', '!', '(', ')',
                       '{', '}', '/', '\\', '_', '|', '-', '@', '#', '*')

        lyric_statistics = {'word_counts': {},
                            'amount': 0
                            }

        for i, song in enumerate(my_artist.songs):
            for p in punctuation:
                song.lyrics = song.lyrics.replace(p, '')
            for word in my_artist.songs[i].lyrics.split():
                lyric_statistics['amount'] += 1
                word = word.lower()
                if word not in lyric_statistics['word_counts']:
                    lyric_statistics['word_counts'][word] = 0
                lyric_statistics['word_counts'][word] += 1

        words_per_song = lyric_statistics['amount'] / number_of_songs
        word_of_choice_count = lyric_statistics['word_counts'].get(word_of_choice)
        lyric_statistics['word_counts'] = sorted(lyric_statistics['word_counts'].items(), key=lambda x: x[1], reverse=True)

        print('\n')
        print(artist, number_of_songs, 'most popular songs:', song_list)
        print(artist + ' Most Common Words:', lyric_statistics['word_counts'])
        print('Words per song:', words_per_song)
        print('# of times', "'" + word_of_choice + "' is used:", word_of_choice_count)
        print('\n')


lyric_word_counter(['Taylor Swift'], 10, 'you')


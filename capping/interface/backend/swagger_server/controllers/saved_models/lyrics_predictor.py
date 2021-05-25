from joblib import load
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import lyricsgenius
import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


model = load('swagger_server/controllers/saved_models/saved_lyrical_model.joblib')
transformer = load('swagger_server/controllers/saved_models/transformer.bin')
vectorizer = load('swagger_server/controllers/saved_models/vectorizer.bin')


def lyric_cleaning(artist, song):
    genius = lyricsgenius.Genius('eQ4wM1lg9zClUNMLGaLFC8tBdOyJP-58AfOHYHKPZIERLSUXpufboLL0MnFUpbpM')
    genius.verbose = False
    genius.remove_section_headers = True
    genius.excluded_terms = ["(Remix)", "(Live)"]
    my_artist = genius.search_artist(artist, max_songs=1, sort="popularity")
    my_song = my_artist.song(song)
    my_lyrics = my_song.lyrics
    punctuation = (',', '"', "'",  ",", ';', ':', '.', '?', '!', '(', ')',
                   '{', '}', '/', '\\', '_', '|', '-', '@', '#', '*', '[', ']')
    stop_words = list(stopwords.words('english'))

    for p in punctuation:
        my_lyrics = my_lyrics.replace(p, '')
        my_lyrics = my_lyrics.lower()

        tokenized_song = word_tokenize(my_lyrics)
        tokenized_song = [w for w in tokenized_song if w not in stop_words]
        tokenized_song = lemmatize_song(tokenized_song)
    return str(tokenized_song)


def song_genre_predictor(artist, song):
    song_lyrics = lyric_cleaning(artist, song)
    song_lyrics = [song_lyrics]
    song_lyrics = lemmatize_song(song_lyrics)
    my_lyric_counts = vectorizer.transform(song_lyrics)
    my_lyrics_transformed = transformer.transform(my_lyric_counts)
    predicted_genre = model.predict(my_lyrics_transformed)
    return my_lyrics_transformed


def lemmatize_song(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_lyrics = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_lyrics.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_lyrics

def one_step_predict(song, artist):
    prediction = model.predict(song_genre_predictor(artist=artist, song=song))[0]
    return prediction

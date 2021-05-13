USE MusicAnalysis
SELECT * from labeled_features

-- Add Artists from temp flat file (labeled_features)
INSERT INTO Artists(
    ArtistID,
    ArtistName)
SELECT DISTINCT(artist_ID), artist_name 
FROM labeled_features;

-- Add Songs from temp flat file (labeled_features)
INSERT INTO Songs(
    SongID,
    SongName,
    SongGenre,
    AristID
)
SELECT id, name, genre, artist_id 
FROM labeled_features;


EXEC sp_RENAME 'labeled_features.key' , 'musicalkey', 'COLUMN'

-- Add SongFeatures from temp flat file (labeled_features)
INSERT INTO SongFeatures(
Acousticness, Danceability, Duration_ms, Energy, Instrumentalness,
MusicalKey, Liveness, Loudness, Mode, Speechiness, Tempo, Time_signature, 
Valence, SongID)
SELECT
acousticness, danceability, duration_ms, energy, instrumentalness,
musicalkey, liveness, loudness, mode, speechiness, tempo, time_signature,
valence, id 
FROM labeled_features

DROP TABLE labeled_features;
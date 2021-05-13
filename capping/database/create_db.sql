CREATE DATABASE MusicAnalysis;
USE MusicAnalysis

CREATE TABLE Artists (
    ArtistID VARCHAR(22) NOT NULL,
    ArtistName VARCHAR(50) NOT NULL,
    PRIMARY KEY (ArtistID)
);
GO

CREATE TABLE Songs (
    SongID VARCHAR(22) NOT NULL,
    SongName VARCHAR(175) NOT NULL,
    SongGenre VARCHAR(15) NOT NULL,
    AristID VARCHAR(22) FOREIGN KEY REFERENCES Artists(ArtistID)
    PRIMARY KEY (SongID)
);
GO

CREATE TABLE SongFeatures(
    Acousticness FLOAT NOT NULL,
    Danceability FLOAT NOT NULL,
    Duration_ms INT NOT NULL,
    Energy FLOAT NOT NULL,
    Instrumentalness FLOAT NOT NULL,
    MusicalKey INT NOT NULL,
    Liveness FLOAT NOT NULL,
    Loudness FLOAT NOT NULL,
    Mode INT NOT NULL,
    Speechiness FLOAT NOT NULL,
    Tempo FLOAT NOT NULL,
    Time_signature INT NOT NULL,
    Valence FLOAT NOT NULL,
    SongID VARCHAR(22) FOREIGN KEY REFERENCES Songs(SongID)
);
GO

CREATE TABLE SongLyrics(
    SongID VARCHAR(22) FOREIGN KEY REFERENCES Songs(SongID),
    Lyrics VARCHAR(7500) NOT NULL,
);
GO
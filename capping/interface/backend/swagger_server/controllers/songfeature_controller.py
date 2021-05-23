import connexion
import six

from swagger_server.models.song import Song  # noqa: E501
from swagger_server.models.songfeature import Songfeature  # noqa: E501
from swagger_server import util

from .db_util import query_to_dict

def songfeature_filter_get(songid=None, genre=None, artist=None):  # noqa: E501
    """Get all song features that meet filters

     # noqa: E501

    :param songid: id of song to filter by
    :type songid: str
    :param genre: genre to filter songs by
    :type genre: str
    :param artist: artist to filter by
    :type artist: str

    :rtype: List[Song]
    """
    query = 'SELECT * FROM SongFeatures'
    multi_flag = "WHERE"
    if genre and not artist:
        query = """
        SELECT Acousticness, Danceability, Duration_ms, Energy,Instrumentalness, MusicalKey,
            Liveness,Loudness,Mode, Speechiness,Tempo, Time_signature, Valence, Songs.SongID,
            Songs.SongName
        FROM SongFeatures
        JOIN Songs
        ON Songs.SongID = SongFeatures.SongID
        AND Songs.SongGenre = '{}'
        """.format(genre)
        multi_flag = "AND"

    if artist and not genre:
        #Query too complicated, separate entity
        query = """
        SELECT Acousticness, Danceability, Duration_ms, Energy,Instrumentalness, MusicalKey,
            Liveness,Loudness,Mode, Speechiness,Tempo, Time_signature, Valence, Songs.SongID
        FROM SongFeatures
        JOIN Songs
        ON Songs.SongID = SongFeatures.SongID
        JOIN Artists
        ON Songs.ArtistID = Artists.ArtistID
        WHERE Artists.ArtistName = '{}'
        """.format(artist)
        multi_flag = "AND"

    if artist and genre:
        query = """
        SELECT Acousticness, Danceability, Duration_ms, Energy,Instrumentalness, MusicalKey,
            Liveness,Loudness, Mode, Speechiness,Tempo, Time_signature, Valence, Songs.SongID
        FROM SongFeatures
        JOIN Songs
        ON Songs.SongID = SongFeatures.SongID
        JOIN Artists
        ON Songs.ArtistID = Artists.ArtistID
        WHERE Artists.ArtistName = '{}'
        AND Songs.SongGenre = '{}'
        """.format(artist, genre)

    if songid:
        query = query + " {} SongFeatures.SongID = '{}'".format(songid)

    results = query_to_dict(query)
    features_list = []

    for r in results:
        features_list.append(
        Songfeature(acousticness= r['Acousticness'],
                    danceability= r['Danceability'],
                    duration_ms= r['Duration_ms'],
                    energy= r['Energy'],
                    instrumentalness= r['Instrumentalness'],
                    musicalkey= r['MusicalKey'],
                    liveness= r['Liveness'],
                    loudness= r['Loudness'],
                    mode= r['Mode'],
                    speechiness= r['Speechiness'],
                    tempo= r['Tempo'],
                    timesignature= r['Time_signature'],
                    valence= r['Valence'],
                    songid= r['SongID']))
    return features_list


def songfeature_get():  # noqa: E501
    """Get all song features

     # noqa: E501


    :rtype: List[Songfeature]
    """
    query = 'SELECT * FROM SongFeatures'
    results = query_to_dict(query)
    features_list = []
    for r in results:
        features_list.append(
        Songfeature(acousticness= r['Acousticness'],
                    danceability= r['Danceability'],
                    duration_ms= r['Duration_ms'],
                    energy= r['Energy'],
                    instrumentalness= r['Instrumentalness'],
                    musicalkey= r['MusicalKey'],
                    liveness= r['Liveness'],
                    loudness= r['Loudness'],
                    mode= r['Mode'],
                    speechiness= r['Speechiness'],
                    tempo= r['Tempo'],
                    timesignature= r['Time_signature'],
                    valence= r['Valence'],
                    songid= r['SongID']))
    return features_list

def songfeature_songid_get(songid):  # noqa: E501
    """Gets song feature from song ID

     # noqa: E501

    :param songid: id of song
    :type songid: str

    :rtype: List[Songfeature]
    """
    return 'do some magic!'

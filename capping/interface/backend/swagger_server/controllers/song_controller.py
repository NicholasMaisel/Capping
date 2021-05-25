import connexion
import six

from swagger_server.models.song import Song  # noqa: E501
from swagger_server import util
from .db_util import query_to_dict


def song_filter_get(songid=None, genre=None, artist=None, name=None):  # noqa: E501
    """Get all songs

     # noqa: E501

    :param songid: id of song to filter by
    :type songid: str
    :param genre: genre to filter songs by
    :type genre: str
    :param artist: artist to filter by
    :type artist: str

    :rtype: List[Song]
    """
    query = "SELECT * FROM Songs"
    multi_flag = "WHERE"
    if artist:
        query = query + " JOIN Artists ON Songs.ArtistID = Artists.ArtistID WHERE Artists.ArtistName = '{}'".format(artist)
        multi_flag = "AND"

    if songid:
        query = query + " {} SongID = '{}'".format(multi_flag ,songid)
        multi_flag = "AND"

    if genre:
        query = query + " {} SongGenre = '{}'".format(multi_flag ,genre)
        multi_flag = "AND"

    if name:
        query = query + " {} SongName = '{}'".format(multi_flag, name)
        multi_flag = "AND"

    result = query_to_dict(query)
    song_list = []
    for r in result:
        song_list.append(Song(r['SongID'],r['SongName'],r['SongGenre'],r['ArtistID']))
    return song_list


def song_get():  # noqa: E501
    """Get all songs

     # noqa: E501


    :rtype: List[Song]
    """
    query = 'SELECT * FROM Songs'
    result = query_to_dict(query)
    song_list = []
    for r in result:
        song_list.append(Song(r['SongID'],r['SongName'],r['SongGenre'],r['ArtistID']))
    return song_list

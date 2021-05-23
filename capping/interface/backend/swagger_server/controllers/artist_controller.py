import connexion
import six

from swagger_server.models.artist import Artist  # noqa: E501
from swagger_server import util

from .db_util import query_to_dict

def artist_filter_get(genre=None):  # noqa: E501
    """Get artists that meet filters

     # noqa: E501

    :param genre: genre to filter songs by
    :type genre: str

    :rtype: List[Artist]
    """
    query = 'SELECT DISTINCT(Artists.ArtistID), Artists.ArtistName, SongGenre FROM Artists'
    if genre:
        query = query + " JOIN Songs ON Artists.ArtistID = Songs.ArtistID AND Songs.SongGenre = '{}'".format(genre)
    result  = query_to_dict(query)
    artist_list = []
    for r in result:
        artist_list.append(Artist(r['ArtistID'],r['ArtistName']))
    return result


def artist_get():  # noqa: E501
    """Get all artists

     # noqa: E501


    :rtype: List[Artist]
    """
    query = 'SELECT DISTINCT * FROM Artists'
    result  = query_to_dict(query)
    artist_list = []
    for r in result:
        artist_list.append(Artist(r['ArtistID'],r['ArtistName']))
    return artist_list

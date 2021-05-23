import connexion
import six

from swagger_server.models.lyrics import Lyrics  # noqa: E501
from swagger_server.models.song import Song  # noqa: E501
from swagger_server import util


def lyrics_filter_get(songid=None, genre=None, artist=None):  # noqa: E501
    """Get all song lyrics that meet filters

     # noqa: E501

    :param songid: id of song to filter by
    :type songid: str
    :param genre: genre to filter songs by
    :type genre: str
    :param artist: artist to filter by
    :type artist: str

    :rtype: List[Song]
    """
    return 'do some magic!'


def lyrics_get():  # noqa: E501
    """Get all lyrics

     # noqa: E501


    :rtype: List[Lyrics]
    """
    return 'do some magic!'

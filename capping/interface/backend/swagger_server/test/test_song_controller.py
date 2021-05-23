# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.song import Song  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSongController(BaseTestCase):
    """SongController integration test stubs"""

    def test_song_filter_get(self):
        """Test case for song_filter_get

        Get all songs
        """
        query_string = [('songid', 'songid_example'),
                        ('genre', 'genre_example'),
                        ('artist', 'artist_example')]
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/song/filter',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_song_get(self):
        """Test case for song_get

        Get all songs
        """
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/song',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

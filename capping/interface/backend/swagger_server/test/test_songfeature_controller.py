# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.song import Song  # noqa: E501
from swagger_server.models.songfeature import Songfeature  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSongfeatureController(BaseTestCase):
    """SongfeatureController integration test stubs"""

    def test_songfeature_filter_get(self):
        """Test case for songfeature_filter_get

        Get all song features that meet filters
        """
        query_string = [('songid', 'songid_example'),
                        ('genre', 'genre_example'),
                        ('artist', 'artist_example')]
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/songfeature/filter',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_songfeature_get(self):
        """Test case for songfeature_get

        Get all song features
        """
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/songfeature',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_songfeature_songid_get(self):
        """Test case for songfeature_songid_get

        Gets song feature from song ID
        """
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/songfeature/{songid}'.format(songid='songid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

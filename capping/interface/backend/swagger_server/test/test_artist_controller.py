# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.artist import Artist  # noqa: E501
from swagger_server.test import BaseTestCase


class TestArtistController(BaseTestCase):
    """ArtistController integration test stubs"""

    def test_artist_filter_get(self):
        """Test case for artist_filter_get

        Get artists that meet filters
        """
        query_string = [('genre', 'genre_example')]
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/artist/filter',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_artist_get(self):
        """Test case for artist_get

        Get all artists
        """
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/artist',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

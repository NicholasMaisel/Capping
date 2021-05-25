# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.prediction import Prediction  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPredictionController(BaseTestCase):
    """PredictionController integration test stubs"""

    def test_predict_input_get(self):
        """Test case for predict_input_get

        Access to the neural network
        """
        query_string = [('acousticness', 8.14),
                        ('danceability', 8.14),
                        ('duration_ms', 56),
                        ('energy', 8.14),
                        ('instrumentalness', 8.14),
                        ('musicalkey', 56),
                        ('liveness', 8.14),
                        ('loudness', 8.14),
                        ('mode', 56),
                        ('speechiness', 8.14),
                        ('tempo', 8.14),
                        ('timesignature', 56),
                        ('valence', 8.14),
                        ('model_type', 'model_type_example')]
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/predict/input',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_predict_lyrics_input_get(self):
        """Test case for predict_lyrics_input_get

        Predict a songs genre
        """
        query_string = [('song', 'song_example'),
                        ('artist', 'artist_example')]
        response = self.client.open(
            '/NicholasMaisel/MusicCapping/1.0.0/predict/lyrics/input',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

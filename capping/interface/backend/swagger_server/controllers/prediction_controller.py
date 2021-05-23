import connexion
import six

from swagger_server.models.prediction import Prediction  # noqa: E501
from swagger_server import util

from .saved_models.predict_from_models import predict as model_predictor


def predict_input_get(acousticness, danceability, duration_ms, energy, instrumentalness, musicalkey, liveness, loudness, mode, speechiness, tempo, timesignature, valence, model_type):  # noqa: E501
    """Access to the neural network

     # noqa: E501

    :param acousticness:
    :type acousticness:
    :param danceability:
    :type danceability:
    :param duration_ms:
    :type duration_ms: int
    :param energy:
    :type energy:
    :param instrumentalness:
    :type instrumentalness:
    :param musicalkey:
    :type musicalkey: int
    :param liveness:
    :type liveness:
    :param loudness:
    :type loudness:
    :param mode:
    :type mode: int
    :param speechiness:
    :type speechiness:
    :param tempo:
    :type tempo:
    :param timesignature:
    :type timesignature: int
    :param valence:
    :type valence:
    :param model_type:
    :type model_type: str

    :rtype: List[Prediction]
    """
    input = {
    "acousticness": acousticness,
    "danceability": danceability,
    "duration_ms": duration_ms,
    "energy": energy,
    "instrumentalness": instrumentalness,
    "liveness": liveness,
    "loudness": loudness,
    "mode": mode,
    "musicalkey": musicalkey,
    "speechiness": speechiness,
    "tempo": tempo,
    "timesignature": timesignature,
    "valence": valence}


    prediction = model_predictor(input, model_type)

    return prediction

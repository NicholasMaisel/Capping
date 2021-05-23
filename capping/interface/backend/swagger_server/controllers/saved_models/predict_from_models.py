from joblib import load
from numpy import argmax
from keras.models import load_model
import pandas as pd



def predict(input, model):
    """
        Takes input and provides a prediction using on of the model types.

        Input should include the following features in the following order:
        ["acousticness","danceability","energy","duration_ms",
         "instrumentalness","loudness","liveness","speechiness",
         "valence","tempo"]
    """


    genres = ['Rock','EDM','Jazz', 'Hop', 'Pop', 'Country', 'Classical']

    if model == 'nn':
        keys = ["acousticness","danceability","energy","duration_ms",
                     "instrumentalness","loudness","liveness","speechiness",
                     "valence","tempo"]

        input = [input[key] for key in keys]
        input = [input]
        model = load_model('swagger_server/controllers/saved_models/saved_nn_model')
        scaler = load('swagger_server/controllers/saved_models/std_scaler.bin')
        input = scaler.transform(input)
        prediction = argmax(model.predict(input), axis = 1)
        prediction = genres[prediction[0]]

    elif model == 'knn':
        keys = ['danceability', 'energy', 'instrumentalness',
         'loudness', 'valence', 'tempo']
        input = [[input[key] for key in keys]]
        # MODIFY INPUT TO ONLY CONTAIN THE CORRECT VALUES
        model = load('swagger_server/controllers/saved_models/saved_knn.joblib')
        prediction = model.predict(input)[0]

    elif model == 'ensemble':
        keys = ["acousticness","danceability","energy","duration_ms",
                     "instrumentalness","loudness","liveness","speechiness",
                     "valence","tempo"]
        input = [[input[key] for key in keys]]
        model = load('swagger_server/controllers/saved_models/saved_ensemble_model.joblib')
        scaler = load('swagger_server/controllers/saved_models/ensemble_std_scaler.bin')
        input = scaler.transform(input)
        prediction = genres[model.predict(input)[0]]

    return prediction

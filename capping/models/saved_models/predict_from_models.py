from joblib import load
from numpy import argmax
from keras.models import load_model
from pandas import Series

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
        model = load_model('./saved_nn_model')
        scaler = load('std_scaler.bin')
        input = scaler.transform(input)
        prediction = genres[argmax(model.predict(input), axis = 1)]

    elif model == 'knn':
        # MODIFY INPUT TO ONLY CONTAIN THE CORRECT VALUES
        model = load('/knn/saved_knn.joblib')
        prediction = model.predict(input)

    elif model == 'ensemble':
        model = load('/voting_ensemble/saved_ensemble_model.joblib')
        scaler = load('/votin_ensemble/std_scaler.bin')
        input = scaler.transform(input)
        prediciton = genres[model.predict(input)]

    return prediction

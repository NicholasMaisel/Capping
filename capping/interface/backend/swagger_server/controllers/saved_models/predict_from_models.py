from joblib import load
from numpy import argmax
from keras.models import load_model
import pandas as pd

def predict_from_nn(input):
    genres = ['Rock','EDM','Jazz', 'Hop', 'Pop', 'Country', 'Classical']

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
    return prediction

def predict_from_knn(input):
    keys = ['danceability', 'energy', 'instrumentalness',
     'loudness', 'valence', 'tempo']
    input = [[input[key] for key in keys]]
    # MODIFY INPUT TO ONLY CONTAIN THE CORRECT VALUES
    model = load('swagger_server/controllers/saved_models/saved_knn.joblib')
    prediction = model.predict(input)[0]
    return prediction


def predict_from_ensemble(input):
    genres = ['Rock','EDM','Jazz', 'Hop', 'Pop', 'Country', 'Classical']

    keys = ["acousticness","danceability","energy","duration_ms",
                 "instrumentalness","loudness","liveness","speechiness",
                 "valence","tempo"]
    input = [[input[key] for key in keys]]
    model = load('swagger_server/controllers/saved_models/saved_ensemble_model.joblib')
    scaler = load('swagger_server/controllers/saved_models/ensemble_std_scaler.bin')
    input = scaler.transform(input)

    prediction = genres[model.predict(input)[0]]
    return prediction

def predict_from_svm(input):
    keys = ["acousticness","danceability","energy","duration_ms",
                 "instrumentalness","loudness","liveness","speechiness",
                 "valence","tempo"]
    input = [[input[key] for key in keys]]
    model = load('swagger_server/controllers/saved_models/saved_svm.joblib')
    prediction = model.predict(input)[0]

    return prediction


def predict(input, model):
    if model == "nn":
        prediction = predict_from_nn(input)
    if model == "knn":
        prediction = predict_from_knn(input)
    if model == "ensemble":
        prediction = predict_from_ensemble(input)
    if model == "svm":
        prediction = predict_from_svm(input)
    if model == "all":
        prediction = {"nn_prediction": predict_from_nn(input),
                      "knn_prediction": predict_from_nn(input),
                      "ensemble_prediction": predict_from_ensemble(input),
                      "svm_prediction": predict_from_svm(input)}


    return prediction

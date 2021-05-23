from joblib import load
import numpy as np

# Load model
model = load('saved_knn.joblib')
input = [[0.572,0.835,0.000377,-6.219,0.795,129.981]]
# NOTE: When predicting using the knn classifier, we only use the following
#       features in the following order
#[['danceability', 'energy', 'instrumentalness','loudness', 'valence', 'tempo', 'genre']]

print(model.predict(input))

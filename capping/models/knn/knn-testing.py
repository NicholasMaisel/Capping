import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, recall_score
from sklearn.pipeline import Pipeline
from itertools import combinations
import csv
from joblib import dump

def read_data():
    data = pd.read_csv('../../datasets/labeled_data/labeled_features.csv')
    return data


def knn(data):
    data = data[['danceability', 'energy', 'instrumentalness',
     'loudness', 'valence', 'tempo', 'genre']]

    # Remove songs with multiple classifications
    data.drop_duplicates(subset = ["danceability","energy",
                 "instrumentalness","loudness","tempo",
                 "valence"], inplace = True)

    x = data.iloc[:, :-1].values
    y = data.iloc[:, len(data.columns)-1].values

    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4, random_state=1)
    pipe = Pipeline([('scaler', StandardScaler()),
                              ('knn',KNeighborsClassifier(n_neighbors =10))])
    pipe.fit(x_train, y_train)
    y_pred = pipe.predict(x_test)

    #Save model and scaler for later use
    dump(pipe, 'saved_knn.joblib')

def main():
    knn(read_data())

if __name__ == '__main__':
    main()

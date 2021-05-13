import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, recall_score, plot_confusion_matrix
from sklearn.pipeline import Pipeline
from itertools import combinations
import csv
import seaborn as sns

def read_data():
    data = pd.read_csv('../datasets/labeled_data/labeled_features.csv')
    return data

def con_mat_to_df(con_mat, labels):
    con_mat = con_mat.tolist()
    con_mat_dict = {}
    for i in range(len(labels)):
        con_mat_dict[labels[i]] = con_mat[i]
    con_mat_df = pd.DataFrame(con_mat_dict, index = labels)
    sns.heatmap(con_mat_df, annot = True,cmap="YlGnBu")
    plt.show()

    return(con_mat_df)

def knn_features_test(data):
    # Select Features
    full_data = data[["acousticness","danceability","energy",
                 "instrumentalness","liveness","loudness",
                 "valence","tempo","genre"]]

    # Remove songs with multiple classifications
    full_data.drop_duplicates(subset = ["acousticness","danceability","energy",
                 "instrumentalness","liveness","loudness","tempo",
                 "valence"], inplace = True)

    # Train-test split
    selected_combos = combinations(["acousticness","danceability","energy",
                 "instrumentalness","liveness","loudness","key",
                 "valence","tempo"],6)

    scores = {}
    while True:
        try:
            features = list(next(selected_combos))
            features.append('genre')

            data = full_data[features]
            x = data.iloc[:, :-1].values
            y = data.iloc[:, len(features)-1].values

            x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4)
            pipe = Pipeline([('scaler', StandardScaler()),
                              ('knn',KNeighborsClassifier())])
            pipe.fit(x_train, y_train)
            y_pred = pipe.predict(x_test)
            scores[tuple(features)] = recall_score(y_test,y_pred, average ='weighted')

        except StopIteration:
            break
    max_combo = max(scores, key = scores.get)

    print('Max recall combo: {} with score: {}'.format(max_combo, scores[max_combo]))

def knn(data):
    # Select Features
    full_data = data[["acousticness","danceability","energy",
                 "instrumentalness","liveness","loudness",
                 "valence","tempo","genre"]]

    # Remove songs with multiple classifications
    full_data.drop_duplicates(subset = ["acousticness","danceability","energy",
                 "instrumentalness","liveness","loudness","tempo",
                 "valence"], inplace = True)

    # Train-test split
    data = full_data[['danceability', 'energy', 'instrumentalness',
     'loudness', 'valence', 'tempo', 'genre']]


    x = data.iloc[:, :-1].values
    y = data.iloc[:, len(data.columns)-1].values

    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4)
    pipe = Pipeline([('scaler', StandardScaler()),
                              ('knn',KNeighborsClassifier())])
    pipe.fit(x_train, y_train)
    y_pred = pipe.predict(x_test)

    print(classification_report(y_test, y_pred))
    con_mat = confusion_matrix(y_test, y_pred, normalize = 'true')
    genres = ['Rock','Pop','Country','Hip Hop','EDM', 'Jazz', 'Classical']
    print(con_mat_to_df(con_mat, genres))

def main():
    #knn_features_test(read_data())
    knn(read_data())

if __name__ == '__main__':
    main()

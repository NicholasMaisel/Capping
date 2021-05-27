from sklearn.svm import SVC
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, recall_score, plot_confusion_matrix
from sklearn.feature_selection import SelectFromModel
from joblib import dump


def read_data():
    data = pd.read_csv('../../datasets/labeled_data/labeled_features.csv')
    return data

def svc_classify(data):
    data = data[["acousticness","danceability","energy","duration_ms",
                 "instrumentalness","loudness","liveness","speechiness",
                 "valence","tempo","genre"]]

    y = data.pop('genre')
    x = data

    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state=6)

    pipe = Pipeline([('scaler', StandardScaler()),
                              ('svc',SVC(C = 10, gamma = "auto", kernel='rbf'))])

    pipe.fit(x_train, y_train)
    y_pred = pipe.predict(x_test)
    print(y_pred)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test,y_pred))
    dump(pipe, 'saved_svm.joblib')




def main():
    svc_classify(read_data())


if __name__ == '__main__':
    main()

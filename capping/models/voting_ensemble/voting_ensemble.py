import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from joblib import dump

classif_1 = AdaBoostClassifier(n_estimators=50, random_state=1)
classif_2 = RandomForestClassifier(n_estimators=25, random_state=1)
classif_3 = ExtraTreesClassifier(n_estimators = 20, min_samples_split=2, random_state=1)


data = pd.read_csv('../../datasets/labeled_data/labeled_features.csv')
data = data[["acousticness","danceability","energy","duration_ms",
             "instrumentalness","loudness","liveness","speechiness",
             "valence","tempo","genre"]]

# # Prepare target variable
def prepare_target(dataframe, target):
    le = LabelEncoder()
    le.fit(dataframe[target])
    dataframe[target] = le.transform(dataframe[target])
    return dataframe

data = prepare_target(data, "genre")
scaler = StandardScaler()
y = data.pop('genre')
x = scaler.fit_transform(data)
dump(scaler, 'ensemble_std_scaler.bin')

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4,
                                                    random_state=1356)


ensemble_classif = VotingClassifier(estimators = [
('ada', classif_1), ('rf', classif_2), ('ext', classif_3)
], voting='hard')

ensemble_classif.fit(x_train,y_train)
dump(ensemble_classif, 'saved_ensemble_model.joblib')

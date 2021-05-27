from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import pandas as pd
from sklearn.svm import SVC

data = pd.read_csv('../../datasets/labeled_data/labeled_features.csv')
data = data[["acousticness","danceability","energy","duration_ms",
                 "instrumentalness","loudness","liveness","speechiness",
                 "valence","tempo","genre"]]
scaler = StandardScaler()
y = data.pop('genre')
x = scaler.fit_transform(data)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)


param_grid = {'C': [0.1, 1, 10, 100],
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
              'gamma':['scale', 'auto'],
              'kernel': ['linear', 'rbf']}
svc = svm.SVC()
clf = GridSearchCV(svc, param_grid, refit = True)

clf.fit(x_train, y_train)
print(clf.best_params_)

sorted(clf.cv_results_.keys())

from sklearn.svm import SVC
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, recall_score, plot_confusion_matrix
from sklearn.feature_selection import SelectFromModel


def con_mat_to_df(con_mat, labels):
    con_mat = con_mat.tolist()
    con_mat_dict = {}
    for i in range(len(labels)):
        con_mat_dict[labels[i]] = con_mat[i]
    con_mat_df = pd.DataFrame(con_mat_dict, index = labels)
    sns.heatmap(con_mat_df, annot = True,cmap="YlGnBu")
    plt.show()


def read_data():
    data = pd.read_csv('../datasets/labeled_data/labeled_features.csv')
    return data

def tree_classify(data):
    data = data[["acousticness","danceability","energy",
                     "instrumentalness","liveness","loudness",
                     "valence","tempo","genre"]]

    x = data.iloc[:, :-1].values
    y = data.iloc[:, len(data.columns)-1].values
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4)

    pipe = Pipeline([('scaler', StandardScaler()),
                     ('feature_selection', SelectFromModel(SVC())
                              ('svc',SVC(gamma = "auto"))])

    pipe.fit(x_train, y_train)
    y_pred = pipe.predict(x_test)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test,y_pred))


def main():
    tree_classify(read_data())


if __name__ == '__main__':
    main()

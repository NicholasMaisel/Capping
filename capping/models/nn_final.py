import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.utils import class_weight
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras_sequential_ascii import keras2ascii

# Load Data
data = pd.read_csv('../datasets/labeled_data/labeled_features.csv')
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

y = data['genre']
x = data.drop('genre', axis = 1)

scaler = StandardScaler()
x = scaler.fit_transform(x)

# Create the validation and training dataframes
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4,random_state=1356)

model = tf.keras.models.Sequential([
                    tf.keras.layers.Dense(5, activation=tf.nn.relu),
                    tf.keras.layers.Dropout(0.15),
                    tf.keras.layers.Dense(4, activation=tf.nn.relu),
                    tf.keras.layers.Dense(7, activation=tf.nn.softmax)])

opt = tf.keras.optimizers.Adam(learning_rate=0.025)
model.compile(loss='sparse_categorical_crossentropy',optimizer=opt,metrics=['accuracy'])
model.fit(x_train, y_train, epochs=100)
model.evaluate(x_test, y_test)

predictions = model.predict(x_test)
predicted_classes = np.argmax(predictions, axis = 1)
con_mat = confusion_matrix(y_test, predicted_classes)
metrics = classification_report(y_test, predicted_classes)
print(con_mat)
print(metrics)
print(keras2ascii(model))

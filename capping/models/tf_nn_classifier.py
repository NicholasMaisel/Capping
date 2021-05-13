import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental.preprocessing import Normalization
from tensorflow.keras.layers.experimental.preprocessing import IntegerLookup
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.utils import class_weight

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

validation_frame = data.sample(frac=0.3, random_state=1234)
train_frame = data.drop(validation_frame.index)

def encode_numerical_feature(feature, name, dataset):
    # Create Normalization layer for our feature
    normalizer = Normalization()

    # Prepare the dataset that only yields our feature
    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))

    # Learn the statistics of the data
    normalizer.adapt(feature_ds)

    # Normalize the input feature
    encoded_feature = normalizer(feature)
    return encoded_feature


def dataframe_to_dataset(dataframe, shuffle=True, batch_size=64):
  dataframe = dataframe.copy()
  labels = dataframe.pop('genre')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds

train_ds = dataframe_to_dataset(train_frame)
val_ds = dataframe_to_dataset(validation_frame)



#Adaptation Steps
acousticness = keras.Input(shape=(1,), name="acousticness", dtype="float64")
danceability = keras.Input(shape=(1,), name="danceability", dtype="float64")
duration_ms = keras.Input(shape=(1,), name="duration_ms", dtype="int64")
energy = keras.Input(shape=(1,), name="energy", dtype="float64")
instrumentalness = keras.Input(shape=(1,), name="instrumentalness", dtype="float64")
liveness = keras.Input(shape=(1,), name="liveness", dtype="float64")
speechiness = keras.Input(shape=(1,), name="speechiness", dtype="float64")
loudness = keras.Input(shape=(1,), name="loudness", dtype="float64")
valence = keras.Input(shape=(1,), name="valence", dtype="float64")
tempo = keras.Input(shape=(1,), name="tempo", dtype="float64")

all_inputs = [
    acousticness,
    danceability,
    energy,
    instrumentalness,
    liveness,
    loudness,
    speechiness,
    duration_ms,
    valence,
    tempo,
]

acousticness_encoded = encode_numerical_feature(acousticness, "acousticness", train_ds)
danceability_encoded = encode_numerical_feature(danceability, "danceability", train_ds)
energy_encoded = encode_numerical_feature(energy, "energy", train_ds)
instrumentalness_encoded = encode_numerical_feature(instrumentalness, "instrumentalness", train_ds)
liveness_encoded = encode_numerical_feature(liveness, "liveness", train_ds)
loudness_encoded = encode_numerical_feature(loudness, "loudness", train_ds)
speechiness_encoded = encode_numerical_feature(speechiness, "speechiness", train_ds)
duration_ms_encoded = encode_numerical_feature(acousticness, "duration_ms", train_ds)
valence_encoded = encode_numerical_feature(valence, "valence", train_ds)
tempo_encoded = encode_numerical_feature(tempo, "tempo", train_ds)

all_features = layers.concatenate(
    [
        acousticness_encoded,
        danceability_encoded,
        energy_encoded,
        instrumentalness_encoded,
        liveness_encoded,
        loudness_encoded,
        speechiness_encoded,
        duration_ms_encoded,
        valence_encoded,
        tempo_encoded,
    ]
)

nn = layers.Dense(6, activation="relu")(all_features)
nn = layers.Dropout(0.5)(nn)
output = layers.Dense(7,activation='softmax')(nn)
model = keras.Model(all_inputs, output)

model.compile("adam",loss = "sparse_categorical_crossentropy", metrics=["accuracy"], run_eagerly=True)

model.fit(train_ds, epochs = 50, validation_data=val_ds)
preds = model.predict(val_ds)
classes = np.argmax(preds, axis = 1)

#PREDICTION AND TESTING
random_test_data = data.sample(frac=0.25)
random_test_data['predicted_genre'] = ''

for record in random_test_data.index:
    sample = random_test_data.loc[record,].to_dict()
    sample.pop('genre') # Remove Genre
    sample.pop('predicted_genre')
    input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
    prediction = model.predict(input_dict)
    random_test_data.loc[record,'predicted_genre'] = np.argmax(prediction, axis = 1)

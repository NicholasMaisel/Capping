import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental.preprocessing import Normalization
from tensorflow.keras.layers.experimental.preprocessing import IntegerLookup
from sklearn.preprocessing import LabelEncoder

# Load Data
data = pd.read_csv('../datasets/labeled_data/labeled_features.csv')
data = data[["acousticness","danceability","duration_ms","energy",
             "instrumentalness","loudness","speechiness",
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

def encode_string_categorical_feature(feature, name, dataset):
    # Create a StringLookup layer which will turn strings into integer indices
    index = StringLookup()

    # Prepare a Dataset that only yields our feature
    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))

    # Learn the set of possible string values and assign them a fixed integer index
    index.adapt(feature_ds)

    # Turn the string input into integer indices
    encoded_feature = index(feature)

    # Create a CategoryEncoding for our integer indices
    encoder = IntegerLookup(output_mode="binary")

    # Prepare a dataset of indices
    feature_ds = feature_ds.map(index)

    # Learn the space of possible indices
    encoder.adapt(feature_ds)

    # Apply one-hot encoding to our indices
    encoded_feature = encoder(encoded_feature)
    return encoded_feature

def encode_integer_categorical_feature(feature, name, dataset):
    # Create a CategoryEncoding for our integer indices
    encoder = IntegerLookup(output_mode="binary")

    # Prepare a Dataset that only yields our feature
    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))

    # Learn the space of possible indices
    encoder.adapt(feature_ds)

    # Apply one-hot encoding to our indices
    encoded_feature = encoder(feature)
    return encoded_feature

def dataframe_to_dataset(dataframe, shuffle=True, batch_size=32):
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
#liveness = keras.Input(shape=(1,), name="liveness", dtype="float64")
speechiness = keras.Input(shape=(1,), name="speechiness", dtype="float64")
loudness = keras.Input(shape=(1,), name="loudness", dtype="float64")
valence = keras.Input(shape=(1,), name="valence", dtype="float64")
tempo = keras.Input(shape=(1,), name="tempo", dtype="float64")

all_inputs = [
    acousticness,
    danceability,
    energy,
    instrumentalness,
    #liveness,
    loudness,
    speechiness,
    duration_ms,
    valence,
    tempo,
]

acousticness_encoded = encode_numerical_feature(acousticness, "acousticness", train_ds)
danceability_encoded = encode_numerical_feature(acousticness, "danceability", train_ds)
energy_encoded = encode_numerical_feature(acousticness, "energy", train_ds)
instrumentalness_encoded = encode_numerical_feature(acousticness, "instrumentalness", train_ds)
#liveness_encoded = encode_numerical_feature(acousticness, "liveness", train_ds)
loudness_encoded = encode_numerical_feature(acousticness, "loudness", train_ds)
speechiness_encoded = encode_numerical_feature(acousticness, "speechiness", train_ds)
duration_ms_encoded = encode_numerical_feature(acousticness, "duration_ms", train_ds)
valence_encoded = encode_numerical_feature(acousticness, "valence", train_ds)
tempo_encoded = encode_numerical_feature(acousticness, "tempo", train_ds)

all_features = layers.concatenate(
    [
        acousticness_encoded,
        danceability_encoded,
        energy_encoded,
        instrumentalness_encoded,
        #liveness_encoded,
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

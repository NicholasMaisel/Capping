from keras.models import load_model
import numpy as np
from joblib import load

model = load_model('./saved_nn_model')
scaler = load('std_scaler.bin')

input = [[0.428,0.793,0.488,184005,0,-5.807,0.0823,0.0462,0.5,133.957]]
input = scaler.transform(input)
print(np.argmax(model.predict(input), axis=1))

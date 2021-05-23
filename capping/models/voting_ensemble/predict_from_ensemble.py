from joblib import load

model = load('saved_ensemble_model.joblib')
scaler = load('std_scaler.bin')
input = [[0.0136,0.71,0.674,184413,0.0000173,-5.393,0.0366,0.0352,0.7,124.033],
[0.0697,0.733,0.676,226581,0,-5.655,0.208,0.0432,0.701,97.448],
[0.257,0.8,0.597,320201,0,-7.835,0.185,0.107,0.634,149.999],
[0.0439,0.877,0.677,172185,0,-4.969,0.0986,0.356,0.627,144.941],
[0.109,0.654,0.848,195240,0.032,-8.121,0.103,0.382,0.185,163.989],
[0.0339,0.877,0.534,197560,0.0000167,-6.178,0.0441,0.15,0.89,108.17],
[0.0354,0.728,0.647,303533,0.0000017,-5.199,0.285,0.24,0.215,160.009],
[0.0388,0.744,0.604,230137,0.0000616,-6.94,0.429,0.0654,0.517,101.012]]

input = scaler.transform(input)
print(model.predict(input))
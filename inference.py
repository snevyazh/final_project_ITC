import pandas as pd
import numpy as np

import librosa
from surfboard import feature_extraction

from flask import Flask
from flask import request

@app.route('/predict_pneumonia')
def predict_pneumonia():
    config = {'log_melspec': {'hop_length_seconds': 0.02, 'n_fft_seconds': 0.08,'n_mels': 64},
    'loudness_slidingwindow': {'frame_length_seconds': 1.0,'hop_length_seconds': 0.25}}
    path = request.args.get('path'))
    X_temp = (
    feature_extraction.extract_features_from_paths(
        path,
        components_list=[{key: config[key]} for key in config],
        statistics_list=["mean", "std"],
    )
    .replace(-np.inf, np.nan)
    .fillna(method="bfill"))
    y_temp = classifier_SVM.predict(X_temp)
    print(y_temp)
    return str(y_temp)


if __name__ == '__main__':
    app.run()
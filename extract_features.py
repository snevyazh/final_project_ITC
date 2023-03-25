import surfboard
import pandas as pd
import numpy as np
from surfboard import feature_extraction

config = {
    'log_melspec': {
        'hop_length_seconds': 0.02,
        'n_fft_seconds': 0.08,
        'n_mels': 64,
    },
    'loudness_slidingwindow': {
        'frame_length_seconds': 1.0,
        'hop_length_seconds': 0.25
    }
}

path_train = pd.read_csv('path_train.csv')
path_test = pd.read_csv('path_test.csv')


X_train = (
    feature_extraction.extract_features_from_paths(
        path_train['path'],
        components_list=[{key: config[key]} for key in config],
        statistics_list=["mean", "std"],
    )
    .replace(-np.inf, np.nan)
    .fillna(method="bfill")
)

X_test = (
    feature_extraction.extract_features_from_paths(
        path_test['path'],
        components_list=[{key: config[key]} for key in config],
        statistics_list=["mean", "std"],
    )
    .replace(-np.inf, np.nan)
    .fillna(method="bfill"))
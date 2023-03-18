import pandas as pd
import numpy as np
import pickle
import surfboard
import subprocess
from surfboard import feature_extraction
import os
import socket
import threading

from flask import Flask
from flask import request


PORT = 3000
PORT_NC = 5000
PATH = 'sound_file.wav'

with open('model.pkl', 'rb') as trained_model_dump:
    loaded_model = pickle.load(trained_model_dump)

def receive_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', PORT_NC))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")
            with open(PATH, 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)

app = Flask(__name__)
@app.route('/predict_pneumonia')
def predict_pneumonia():
    config = {'log_melspec': {'hop_length_seconds': 0.02, 'n_fft_seconds': 0.08,'n_mels': 64},
    'loudness_slidingwindow': {'frame_length_seconds': 1.0,'hop_length_seconds': 0.25}}
    # path = request.args.get('path')
    path = PATH
    print('Got request')
    X_temp = (
    feature_extraction.extract_features_from_paths(
        [path],
        components_list=[{key: config[key]} for key in config],
        statistics_list=["mean", "std"],
    )
    .replace(-np.inf, np.nan)
    .fillna(method="bfill"))
    y_temp = loaded_model.predict(X_temp)
    print(y_temp)
    return str(y_temp[0])

@app.route('/test_conn')
def test_connection():
    # config = {'log_melspec': {'hop_length_seconds': 0.02, 'n_fft_seconds': 0.08,'n_mels': 64},
    # 'loudness_slidingwindow': {'frame_length_seconds': 1.0,'hop_length_seconds': 0.25}}
    # path = request.args.get('path')
    # path = PATH

    return "OK"


@app.route('/submit_file')
def get_file():
    if os.path.exists(PATH):
        os.remove(PATH)
    else:
        print("File does not exist, working clear")

    thread = threading.Thread(target=receive_file)
    thread.start()

    return "Please upload the file"


@app.route('/upload_file', methods=['POST'])
def submit_file():
    if 'audio' not in request.files:
        return 'No audio file in request', 400

    audio_file = request.files['audio']
    audio_file.save('sound_file.wav')

    return 'File uploaded and saved', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

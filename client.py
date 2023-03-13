import requests
import pandas as pd
import numpy as np
from os.path import exists

# song_path = '/Users/stanislavnevyazhsky/My Drive/Colab Notebooks/Project/pneumonia_files/audio_files/20210913-101254-767927efd97ec9bc-spine06.wav'
song_path = input('enter the file path ')
if not exists(song_path):
  song_path = input('enter the correct file path ')


url = 'http://127.0.0.1:5000'

url_full = "{}/predict_pneumonia?path={}.format(url, song_path)
response = requests.get(url_full)
result = str(response.content).replace("b'", "").replace("'", "")


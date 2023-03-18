from os.path import exists
import os
import requests

### Entering the file
# song_path = '/Users/stanislavnevyazhsky/Downloads/20200908-104836-1bc13a1e6697da55-spine04.wav'
song_path = input('enter the file path ')
if not exists(song_path):
  song_path = input('enter the correct file path ')
dir_path, file_name = os.path.split(song_path)

### uploading the file to server
start = requests.get('http://13.48.3.28:3000/submit_file')
command = 'nc 13.48.3.28 5000 < {}'.format(song_path)
os.system(command)

### predicting the result
url = '13.48.3.28:3000'
url_full = "http://{}/predict_pneumonia?path={}".format(url, file_name)
response = requests.get(url_full)
result = str(response.text)

if int(result) == 1:
    print("Go to doctor :-/")
elif int(result) == 0:
    print("You're in good shape :-)")
else:
    print('Bad file! :-(')

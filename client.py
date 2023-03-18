import requests
from os.path import exists
import os

import subprocess

# song_path = '/Users/stanislavnevyazhsky/My Drive/Colab Notebooks/Project/pneumonia_files/audio_files/20210913-101254-767927efd97ec9bc-spine06.wav'
# song_path = input('enter the file path ')
# if not exists(song_path):
#   song_path = input('enter the correct file path ')
# dir_path, file_name = os.path.split(song_path)

IP = '13.48.3.28'
PORT = '3000'

url = f'http://{IP}:{PORT}'

# command = 'scp -i <ec2_instance_key_file> {} <ec2_instance_username>@<ec2_instance_ip>:<remote_file_path>'.format(song_path)
# file_send = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(file_send.stdout.decode('utf-8'))


# file_send = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(file_send.stdout.decode('utf-8'))

url_full = "{}/predict_pneumonia".format(url)
response = requests.get(url_full)
print(response.text)
result = str(response.text)

if result == 1:
    print("Go to doctor")
elif result==0:
    print("You're in good shape")
else:
    print('Something went wrong')



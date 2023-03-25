from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import numpy as np

# import seaborn as sns

from sklearn import preprocessing

from sklearn.model_selection import train_test_split

import librosa


# df_files = pd.read_csv('/content/drive/MyDrive/ITC/Lung_project/selected_records.csv')
# df_files['Date'] = df_files['time'].str.slice(start=0, stop=8)
# df_files['Time'] = df_files['time'].str.slice(start=9, stop=11) + ':' + df_files['time'].str.slice(start=11, stop=13)
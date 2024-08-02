
# Pneumonia detection
## Authors

- Leonid
- [@snevyazh] (https://github.com/snevyazh/)
- Yosef Schoen (https://github.com/YosefSchoen/)



## Features

- Take the recorded auscultation and returns pneumonia diagnosis 
- Trained on hundreds of records labeled by professional doctors
- Works in real-time
- Works with any smartphone that can record an audio
- Tells of the recording is good (Future Version)


## About the project

[Article](https://medium.com/@snevyazh/to-pneumonia-or-not-to-pneumonia-that-is-the-question-a932b8b7520a )


- Lung auscultation - one of the most basic diagnostic tools used for diagnosing respiratory diseases
- Other basic diagnostics (body temperature, blood pressure, pulse) can be taken by the patient himself
- Lung auscultation requires the participation of a doctor
Our instrument allows for self-diagnosis based on the lung auscultation:
- Improve the early diagnosis of pneumonia 
- Save unnecessary visits to the doctor - reduce load to Healthcare System, saves patient's time

## Files to use

- You need just inference.py, model.pkl and requirements.txt
- The rest of the files are working material on the project

## API Reference 

#### Submit audio for prediction

```http
  GET /predict_pneumonia?path={audio_path}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `path`      | `string` | **Required**. path to audio file |

#### returns 
1 in case of positive for pneumonia and 0 in case of negative




## References

[https://towardsdatascience.com/learning-from-audio-the-mel-scale-mel-spectrograms-and-mel-frequency-cepstral-coefficients-f5752b6324a8]

[https://surfboard.readthedocs.io/_/downloads/en/latest/pdf/]

[https://librosa.org/]

[https://en.wikipedia.org/wiki/Mel-frequency_cepstrum]



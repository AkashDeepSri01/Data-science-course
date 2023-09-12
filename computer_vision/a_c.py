import mediapipe as mp

AudioClassifier = mp.tasks.audio.AudioClassifier
AudioClassifierOptions = mp.tasks.audio.AudioClassifierOptions
AudioClassifierResult = mp.tasks.audio.AudioClassifierResult
AudioRunningMode = mp.tasks.audio.RunningMode
BaseOptions = mp.tasks.BaseOptions

# Load the audio classification model

# Initialize the MediaPipe Audio class
audio = mp.solutions.Audio()

# Read the audio file
audio_file = 'D:\DS.py\computer_vision\yamnet.tflite'

with open(audio_file, 'rb') as f:
    audio_data = f.read()

# Perform audio classification
results = audio.process(audio_data)
classification = results.classification[0]

# Print the predicted label and score
print('Label:', classification.label)
print('Score:', classification.score)

# Release resources
audio.close()

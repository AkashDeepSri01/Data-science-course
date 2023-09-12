import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import audio
import cv2

path='D:\DS.py\computer_vision\yamnet.tflite'


AudioClassifier = mp.tasks.audio.AudioClassifier
AudioClassifierOptions = mp.tasks.audio.AudioClassifierOptions
AudioClassifierResult = mp.tasks.audio.AudioClassifierResult
AudioRunningMode = mp.tasks.audio.RunningMode
BaseOptions = mp.tasks.BaseOptions

results=[]

def print_result(result: AudioClassifierResult, timestamp_ms: int):
    results.appens(result)

options = AudioClassifierOptions(
    base_options=BaseOptions(model_asset_path=path),
    running_mode=AudioRunningMode.AUDIO_STREAM,
    max_results=5,
    result_callback=print_result)

with AudioClassifier.create_from_options(options) as classifier:
  # The classifier is initialized. Use it here.
  # ...
  
  import numpy as np

AudioData = mp.tasks.components.containers.AudioData

# Read microphone data as np arrays, then call

audio_data = AudioData.create_from_array(
    buffer.astype(float) / np.iinfo(np.int16).max, sample_rate)
    
# Send live audio data to perform audio classification.
# Results are sent to the `result_callback` provided in the `AudioClassifierOptions`
classifier.classify_async(audio_data, timestamp_ms)
    
  
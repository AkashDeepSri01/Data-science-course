import cv2
import pyaudio
import wave
video_capture = cv2.VideoCapture(0)  # Change the parameter to the appropriate camera index if needed
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Adjust the parameters as per your requirements
while True:
    # Capture video frame
    ret, frame = video_capture.read()

    # Capture audio frame
    audio_frame = stream.read(1024)

    # Write video frame
    video_out.write(frame)

    # Process and integrate audio and video frames as per your requirements

    # Display the resulting frame
    cv2.imshow('Security Recorder', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
video_capture.release()
video_out.release()
cv2.destroyAllWindows()
stream.stop_stream()
stream.close()
audio.terminate()

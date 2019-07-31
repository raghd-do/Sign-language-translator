import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
from moviepy.editor import VideoFileClip
import cv2 # this an external packege, you shuld write this command in cmd to install it for python.
# $pip install opencv-python

# for more information about this packege, go and visite "opencv.org"
# if you work with Anaconda3 other pckeges will be installed already

headers = {
    # Request headers
    'Prediction-Key': '<enter your predection kay>',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-id': '<enter your Subscription id>'
}

params = urllib.parse.urlencode({
    # Request parameters
    'application': '<enter your service name>'
})

file_path = "<put your video file_path>"

def video_length(filePath):
    clip = VideoFileClip(filePath)
    clip.reader.close()
    clip.audio.reader.close_proc()
    return clip.duration

# request body
frames = 0
seconds = 0
cap = cv2.VideoCapture(0)
while(cap.isOpened):
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    cv2.imwrite('frame.jpg', frame)
    image = open("frame.jpg", 'rb').read()
    if frames < video_length(file_path):
        if round(frames,1) == round(seconds,1):
            try:
                conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com') # use your endpoint here as this example
                conn.request("POST", "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/<enter your project id>/classify/iterations/<enter your iteratin name>/image?%s"
                    % params, image, headers)
                    response = conn.getresponse()
                    data = response.read()
                    print(data)
                    conn.close()
                except Exception as e:
                    print("[Errno {0}] {1}".format(e.errno, e.strerror))
                    seconds += 0.60
        frames += 0.10

    if cv2.waitKey(1) == ord('q'): # when you press q button it will stop all of these stuff
        break
cap.release()

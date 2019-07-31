import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import cv2
from moviepy.editor import VideoFileClip


headers = {
    # Request headers
    'Prediction-Key': 'c050c0027657450f9fdf7e3fe9425eea',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'a5042ce3-1cea-40cf-9079-dad485f3d81f'
}

params = urllib.parse.urlencode({
    # Request parameters
    'application': 'hand\'s signe'
})

file_path = "C:/Users/Raghad/Desktop/AEC/D/custom-vision/Hello.mp4"

def video_length(filePath):
    clip = VideoFileClip(filePath)
    clip.reader.close()
    clip.audio.reader.close_proc()
    return clip.duration

#request body
#image1 = open("C:/Users/Raghad/Desktop/AEC/D/custom-vision/hand2.jpg", 'rb').read()

frames = 0
seconds = 0
cap = cv2.VideoCapture(0)
while(cap.isOpened):
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    cv2.imwrite('frame.jpg', frame)
    image = open("frame.jpg", 'rb').read()

    if frames < video_length(file_path): #أعتقد من هنا تبدا المشكلة
        if round(frames,1) == round(seconds,1):
            try:
                conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
                conn.request("POST", "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/46f2b819-45a2-47ee-93fc-f165fb611af1/classify/iterations/signs/image?%s"
                    % params, image, headers)
                response = conn.getresponse()
                data = response.read()
                print(data)
                conn.close()
            except Exception as e:
                print("[Errno {0}] {1}".format(e.errno, e.strerror))
            seconds += 0.60
        frames += 0.10

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()

#try:
#    conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
#    conn.request("POST", "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/46f2b819-45a2-47ee-93fc-f165fb611af1/classify/iterations/signs/image?%s"
#        % params, image, headers)
#    response = conn.getresponse()
#    data = response.read()
#    print(data)
#    conn.close()
#except Exception as e:
#    print("[Errno {0}] {1}".format(e.errno, e.strerror))

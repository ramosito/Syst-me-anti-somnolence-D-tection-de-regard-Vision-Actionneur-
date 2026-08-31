import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision as mp_vision
import serial
import time
import math
import os
import urllib.request

MODEL_PATH = "face_landmarker.task"
MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/face_landmarker/"
             "face_landmarker/float16/1/face_landmarker.task")

if not os.path.exists(MODEL_PATH):
    print("Téléchargement du modèle...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)
except serial.SerialException:
    print("Erreur : Vérifie ton port COM.")
    arduino = None

print("Arduino OK." if arduino else "Arduino NON connecté (vérifie le port COM).")

base_options = mp_python.BaseOptions(model_asset_path=MODEL_PATH)
options = mp_vision.FaceLandmarkerOptions(
    base_options=base_options,
    running_mode=mp_vision.RunningMode.VIDEO,
    num_faces=1,
)
landmarker = mp_vision.FaceLandmarker.create_from_options(options)

def distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

def get_ear(eye_points, landmarks):
    v1 = distance(landmarks[eye_points[1]], landmarks[eye_points[5]])
    v2 = distance(landmarks[eye_points[2]], landmarks[eye_points[4]])
    h = distance(landmarks[eye_points[0]], landmarks[eye_points[3]])
    return (v1 + v2) / (2.0 * h)

LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

EAR_THRESHOLD = 0.2  # <-- on va ajuster cette valeur ensemble

cap = cv2.VideoCapture(0)
closed_start_time = 0
alarm_on = False

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    rgb_frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    timestamp_ms = int(time.time() * 1000)
    result = landmarker.detect_for_video(mp_image, timestamp_ms)

    if result.face_landmarks:
        landmarks = result.face_landmarks[0]
        left_ear = get_ear(LEFT_EYE, landmarks)
        right_ear = get_ear(RIGHT_EYE, landmarks)
        ear = (left_ear + right_ear) / 2.0

        # Affiche la valeur EAR en direct à l'écran pour calibration
        cv2.putText(image, f"EAR: {ear:.3f}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if ear < EAR_THRESHOLD:
            if closed_start_time == 0:
                closed_start_time = time.time()
            elif time.time() - closed_start_time > 2.0:
                if not alarm_on:
                    print("DANGER : ENDORMISSEMENT !")
                    if arduino:
                        arduino.write(b'1')
                    alarm_on = True
        else:
            closed_start_time = 0
            if alarm_on:
                print("Réveil confirmé.")
                if arduino:
                    arduino.write(b'0')
                alarm_on = False
    else:
        cv2.putText(image, "Visage non detecte", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Détecteur Somnolence', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
landmarker.close()
if arduino:
    arduino.close()

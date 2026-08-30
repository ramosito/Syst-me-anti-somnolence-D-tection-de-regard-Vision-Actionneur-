import cv2
import mediapipe as mp
import serial
import time
import math

# 1. Connexion à l'Arduino
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2) # Laisse le temps à l'Arduino de redémarrer
except:
    print("Erreur : Vérifie ton port COM.")
    arduino = None

# 2. Chargement du modèle IA MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Fonction mathématique pour l'EAR (Eye Aspect Ratio)
def distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

def get_ear(eye_points, landmarks):
    # Distances verticales et horizontales de l'oeil
    v1 = distance(landmarks[eye_points[1]], landmarks[eye_points[5]])
    v2 = distance(landmarks[eye_points[2]], landmarks[eye_points[4]])
    h = distance(landmarks[eye_points[0]], landmarks[eye_points[3]])
    return (v1 + v2) / (2.0 * h)

# Indices des points des yeux pour MediaPipe
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

cap = cv2.VideoCapture(0)
closed_start_time = 0
alarm_on = False

# 3. Boucle principale de traitement vidéo
while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # MediaPipe a besoin d'images en RGB
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark
            
            # Calcul du taux d'ouverture moyen des deux yeux
            left_ear = get_ear(LEFT_EYE, landmarks)
            right_ear = get_ear(RIGHT_EYE, landmarks)
            ear = (left_ear + right_ear) / 2.0

            # Si le taux passe sous 0.2 (yeux fermés)
            if ear < 0.2:
                if closed_start_time == 0:
                    closed_start_time = time.time()
                elif time.time() - closed_start_time > 2.0: # Plus de 2 secondes
                    if not alarm_on:
                        print("DANGER : ENDORMISSEMENT !")
                        if arduino:
                            arduino.write(b'1') # Envoie l'ordre de sonner
                        alarm_on = True
            else:
                closed_start_time = 0 # Réinitialise le chrono
                if alarm_on:
                    print("Réveil confirmé.")
                    if arduino:
                        arduino.write(b'0') # Envoie l'ordre de couper le son
                    alarm_on = False
                    
    # Affiche la webcam
    cv2.imshow('Détecteur Somnolence', image)
    if cv2.waitKey(5) & 0xFF == 27: # Appuie sur 'Echap' pour quitter
        break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
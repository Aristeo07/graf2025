import cv2
import mediapipe as mp
import math

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Captura de video
cap = cv2.VideoCapture(0)

# Tamaño inicial del rectángulo
lado = 100

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # capturamos las coordenadas del pulgar y del índice
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            h, w, _ = frame.shape
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)

            # dibujar puntos de los dedos
            cv2.circle(frame, (thumb_x, thumb_y), 8, (255, 0, 0), -1)
            cv2.circle(frame, (index_x, index_y), 8, (0, 255, 0), -1)

            # calculo de la distancia entre dedos
            distancia = math.hypot(index_x - thumb_x, index_y - thumb_y)

            # escalamiento de el rectangulo
            lado = int(distancia)

            # centro de pantalla
            cx, cy = w // 2, h // 2

            # dibujar rectangulo
            x1 = cx - lado // 2
            y1 = cy - lado // 2
            x2 = cx + lado // 2
            y2 = cy + lado // 2

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)



    cv2.imshow("Salida", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import mediapipe as mp
import cv2
import math

t= 0
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
cam = cv2.VideoCapture(0)
lengua = cv2.imread('lengua.png',cv2.IMREAD_UNCHANGED)
# separar canales de nuestro png
b, g, r, a = cv2.split(lengua)

# crear mascara alpha
alpha = a / 255.0
alpha = alpha[..., None]
h_l, w_l = lengua.shape[:2]  # guardar tama;o original de imagen
print(lengua.shape)



#inicializamos nuestro modelo face mesh
with mp_face_mesh.FaceMesh(
    static_image_mode=False, max_num_faces=1,
    min_detection_confidence=0.5) as face_mesh:

    #bucle principal de captura de video
    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(frame_rgb)
        alto,ancho,_ = frame.shape



        if results.multi_face_landmarks is not None:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(frame, face_landmarks,
                                      mp_face_mesh.FACEMESH_CONTOURS,
                                        mp_drawing.DrawingSpec(color=(0, 255, 0),thickness=1,circle_radius=1),
                                mp_drawing.DrawingSpec(color=(0, 0, 255),thickness=1,circle_radius=1))

                puntoax = int(face_landmarks.landmark[13].x * ancho)
                puntoay = int(face_landmarks.landmark[13].y * alto)
                puntobx = int(face_landmarks.landmark[14].x * ancho)
                puntoby = int(face_landmarks.landmark[14].y * alto)
                puntocx = int(face_landmarks.landmark[234].x * ancho)
                puntocy = int(face_landmarks.landmark[234].y * alto)
                puntodx = int(face_landmarks.landmark[454].x * ancho)
                puntody = int(face_landmarks.landmark[454].y * alto)
                eucl = int(cv2.norm((puntoax, puntoay), (puntobx, puntoby)))
                eucl_ancho = int(cv2.norm((puntocx,puntocy), (puntodx, puntody)))
                #cv2.line(frame,(puntoax,puntoay),(puntobx,puntoby),(255,0,0),2,1)

                factor = eucl/eucl_ancho
                print (eucl)

                if eucl > 20:
                    #frame= lengua
                    # redimensionar la lengua
                    nuevo_ancho = int(w_l * factor)
                    nuevo_alto = int(h_l * factor)
                    lengua_resized = cv2.resize(lengua, (nuevo_ancho, nuevo_alto), interpolation=cv2.INTER_AREA)

                    #extraer mascara alpha de imagen resized
                    b, g, r, a = cv2.split(lengua_resized)
                    alpha_resized = a / 255.0
                    alpha_resized = alpha_resized[..., None]

                    # caluclar posicion centrada de la boca
                    x = int((puntoax + puntobx) / 2 - nuevo_ancho / 2)
                    y = int((puntoay + puntoby) / 2)

                    # evitar que nuestro png salga del frame
                    x = max(0, min(x, ancho - nuevo_ancho))
                    y = max(0, min(y, alto - nuevo_alto))

                    # superponer la lengua
                    region = frame[y:y + nuevo_alto, x:x + nuevo_ancho]
                    region[:] = (1 - alpha_resized) * region + alpha_resized * lengua_resized[..., :3]




                    print(face_landmarks.landmark[14].x, face_landmarks.landmark[14].y)

        cv2.imshow('ventana', frame)
        esc = cv2.waitKey(1) & 0xFF
        if esc == 27:
            break

    cv2.destroyAllWindows()



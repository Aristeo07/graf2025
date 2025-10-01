import cv2
import numpy as np


camara = cv2.VideoCapture(0)

# Creamos un lienzo vacío
ret, cuadro = camara.read()
lienzo = np.zeros_like(cuadro)

# Rango del color rojo en HSV
u_bajo = np.array([0, 150, 50])
u_alto = np.array([10, 255, 255])


#Colores para dibujar

colorazul = (255,0,0)
colorrojo = (0,0,255)
colorverde = (0,255,0)
colormorado = (255,0,204)
coloramarillo = (0,255,255)
color = (0,255,0)


punto_anterior = None
umbral_distancia = 50  # para evitar trazos largos falsos

while True:
    ret, cuadro = camara.read()
    if not ret:
        break

    
    hsv = cv2.cvtColor(cuadro, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, u_bajo, u_alto)

    # Momentos de la máscara (para calcular el centroide)
    momentos = cv2.moments(mascara)
    if momentos["m00"] > 0:  # hay píxeles del color buscado
        cx = int(momentos["m10"] / momentos["m00"])
        cy = int(momentos["m01"] / momentos["m00"])
        punto_actual = (cx, cy)

        # Dibujar punto en la cámara
        cv2.circle(cuadro, punto_actual, 5, (0, 0, 255), -1)

       

        punto_anterior = punto_actual
    else:
        punto_anterior = None

    combinado = cv2.add(cuadro, lienzo)

    #Invertir la camara modo espejo
    invertido = cv2.flip(combinado,1)

    cv2.rectangle(invertido,(585,10),(635,60),(255,0,0), 1)
    cv2.rectangle(invertido,(530,10),(580,60),(0,0,255),1)
    cv2.rectangle(invertido,(475,10),(525,60),(0,255,0),1)
    cv2.rectangle(invertido,(420,10),(470,60),(255,0,204),1)
    cv2.rectangle(invertido,(365,10),(415,60),(0,255,255),1)
    
    
    




    #Codigo para encontrar los contornos de el color de nuestra mascara
    contornos,_ = cv2.findContours(mascara,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos,key=cv2.contourArea,reverse=True)[:1]


 # Dibujar línea en el lienzo si el salto no es muy grande
    if punto_anterior is not None:
            distancia = np.linalg.norm(np.array(punto_actual) - np.array(punto_anterior))
            if distancia < umbral_distancia:
                cv2.line(lienzo, punto_anterior, punto_actual, color , 5)


    #codigo para encontrar coordenadas de la mancha de color de nuestra mascara y dibujar
    #rectangulo alrededor, no lo ocupé así que lo comento para que no aparezca en pantalla
    #for c in contornos: 
     #   area = cv2.contourArea(c)
      #  if area > 1000:
       #     x,y,w,h= cv2.boundingRect(c)
        #    cv2.rectangle(invertido,(x,y),(x+w,y+h),(255,0,0),1 )

        #else: 
         #   x1 = None
          #  y1 = None    




    #condicion para cambiar de color al entrar el centro de la mancha en un recuadro de color
    if cx is not None:

        if 10 < cx < 60 and 10 < cy < 60:
            color = colorazul

        if 120 < cx < 170 and 10 < cy < 60:
            color = colorverde

        if 65 < cx < 115 and 10 < cy < 60:
            color = colorrojo

        if 175 < cx < 255 and 10 < cy < 60:
            color = colormorado

        if 230 < cx < 280 and 10 < cy < 60:
            color = coloramarillo   

        #NOTA: la inversion de la camara no afectó estas coordenadas cx y cy asi que tuve que cuadrarlas
        #  con las coordenadas de los rectangulos de colores de forma inversa 
          



        
                

    

    cv2.imshow("Dibujo en vivo", invertido)
    cv2.imshow("Mascara de color", mascara)
    cv2.imshow("Lienzo", lienzo)
    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:  # ESC para salir
        break
    elif tecla == ord('c'):  # limpiar lienzo
        lienzo = np.zeros_like(cuadro)

ancho = int(camara.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Resolucion: {ancho}, {alto}")

camara.release()
cv2.destroyAllWindows()
## Código de detección facial con Haarcascades

Al inicio de nuestro código importamos las librerias necesarias, el modelo de haarcascades que requerimos y también definimos las variables que usaremos a lo largo del programa con sus respectivos valores 
```
import cv2 as cv   
import math  
import time     
  
rostro = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')  
mascarilla = cv.imread('mascarilla.png',cv.IMREAD_UNCHANGED)  
r,g,b,a = cv.split(mascarilla)  
cap = cv.VideoCapture(0)  
velx,vely = 5,4  
mascarilla = cv.resize(mascarilla,(250,250))  
alto_mask = 200  
ancho_mask = 200  
  
posx,posy=0,0  
posx2,posy2=0,0  
t = 0  
enfriamientoojos = 0  
  
print('las dimensiones del png: ', mascarilla.shape)  
  
  
ultimo_parpadeo = time.time()  
parpadeando = False
```

En el bucle principal de nuestro código es donde agregaremos nuestros elementos visuales, ya sean primitivas de dibujo de openCV o imagenes png, además configuraremos el comportamiento de cada uno de estos elementos de acuerdo a los requisitos establecidos por el profesor.

```
while True:  
    ret, img = cap.read()  
    gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
    fondo = cv.cvtColor(img, cv.COLOR_BGR2BGRA)  
    img = cv.cvtColor(img,cv.COLOR_BGR2BGRA)  
      
    rostros = rostro.detectMultiScale(gris, 1.3, 5)  
    for(x,y,w,h) in rostros:  
        factorescaladoooor = w / 200    
        ojo1_cx, ojo1_cy = x + int(w * 0.3), y + int(h * 0.4)  
        ojo2_cx, ojo2_cy = x + int(w * 0.7), y + int(h * 0.4)  
        radio = int(5 * factorescaladoooor)  
        ojo_radio = int(20 * factorescaladoooor)  
        t += 0.2  
        if posx == 0 and posy == 0:  
            posx, posy = ojo1_cx, ojo1_cy  
            posx2, posy2 = ojo2_cx, ojo2_cy  
  
        blanco = (255,255,255)  
        negro = (0,0,0)    
  
        res = int((w+h)/8)  
        img = cv.rectangle(img, (x,y), (x+w, y+h), (234, 23,23), 5)  
        img = cv.rectangle(img, (x,int(y+h/2)), (x+w, y+h), (0,255,0),5 )  
  
        # el control de los parpadeos  
        if time.time() - ultimo_parpadeo >= 2:  # cada 2 segundos  
            parpadeando = True  
            ultimo_parpadeo = time.time()  
        if parpadeando:  
            # ojos cerrados  
            cv.line(img, (ojo1_cx - ojo_radio, ojo1_cy),  
                    (ojo1_cx + ojo_radio, ojo1_cy), (0,0,0), 4)  
            cv.line(img, (ojo2_cx - ojo_radio, ojo2_cy),  
                    (ojo2_cx + ojo_radio, ojo2_cy), (0,0,0), 4)  
            # corta el parpadeo rapidamente  
            if time.time() - ultimo_parpadeo >= 0.3:  
                parpadeando = False  
            continue  # salta el resto del dibujo durante el parpadeo  
  
        # ojos abiertos normales        cv.circle(img, (ojo1_cx, ojo1_cy), ojo_radio + 1, (0, 0, 0), 2)  
        cv.circle(img, (ojo1_cx, ojo1_cy), ojo_radio, (255, 255, 255), -1)  
        cv.circle(img, (ojo2_cx, ojo2_cy), ojo_radio + 1, (0, 0, 0), 2)  
        cv.circle(img, (ojo2_cx, ojo2_cy), ojo_radio, (255, 255, 255), -1)  
  
        cv.circle(img, (int(posx), int(posy)), radio, (0, 0, 255), -1)  
        cv.circle(img, (int(posx2), int(posy2)), radio, (0, 0, 255), -1)  
        img = cv.rectangle(img, (x+ int(w*0.40), y+int(h*0.50)),(x+ int(w*0.60),y+ int(h*0.60)),(0,255,255), -1)  
        cv.circle(img, (ojo1_cx, ojo1_cy), ojo_radio + 1, blanco, 2)  
  
        posx += velx  
        posy += vely  
        posx2 += velx  
        posy2 += vely  
  
        # if posx - ojo1_cx > ojo_radio - radio or posx - ojo1_cx < -(ojo_radio - radio):  
        #     velx *= -1        # if posy - ojo1_cy > ojo_radio - radio or posy - ojo1_cy < -(ojo_radio - radio):        #     vely *= -1        # if posx2 - ojo2_cx > ojo_radio - radio or posx2 - ojo2_cx < -(ojo_radio - radio):        #     velx *= -1        # if posy2 - ojo2_cy > ojo_radio - radio or posy2 - ojo2_cy < -(ojo_radio - radio):        #     vely *= -1  
        #  agregamos un tipo de rebote circular, ya que el anterior era rectangular        dist1 = math.hypot(posx - ojo1_cx, posy - ojo1_cy)  
        if dist1 + radio > ojo_radio:  
            nx = (posx - ojo1_cx) / dist1  
            ny = (posy - ojo1_cy) / dist1  
            dot = velx * nx + vely * ny  
            velx -= 2 * dot * nx  
            vely -= 2 * dot * ny  
            posx = ojo1_cx + nx * (ojo_radio - radio)  
            posy = ojo1_cy + ny * (ojo_radio - radio)  
  
        dist2 = math.hypot(posx2 - ojo2_cx, posy2 - ojo2_cy)  
        if dist2 + radio > ojo_radio:  
            nx = (posx2 - ojo2_cx) / dist2  
            ny = (posy2 - ojo2_cy) / dist2  
            dot = velx * nx + vely * ny  
            velx -= 2 * dot * nx  
            vely -= 2 * dot * ny  
            posx2 = ojo2_cx + nx * (ojo_radio - radio)  
            posy2 = ojo2_cy + ny * (ojo_radio - radio)  
 

```
Toda la sección anterior de código está dedicada a trazar y modificar el comportamiento de nuestros ojos creados a partir de cv2.circle, dibujamos los ojos y añadimos pupilas que se estarán moviendo de un lado a otro con un rebote circular, y también agregamos función de parpadeo cada 2 segundos


         
  ```
  img = cv.rectangle(img, (x+ int(w*0.05), y+int(h*0.30)),(x+ int(w*0.10),y+ int(h*0.60)),(0,0,255), -1)  
        img = cv.rectangle(img, (x+ int(w*0.95),y+ int(h*0.30)),(x+ int(w*0.90), y+int(h*0.60)),(0,0,255), -1)  
        cv.ellipse(img, (x+ int(w*.50),y+ int(h*0.80)), (int(80*factorescaladoooor), int(50*factorescaladoooor)), 0, 0, 360, (0, 0, 0), -1)  
          
          
        tamanolengua= 25  
        tamanovariacion = 20  
        lengua = int((tamanolengua + tamanovariacion * abs(math.sin(t))) * factorescaladoooor)  
  
        centroboca = (x+ int(w*.50),y+ int(h*0.80))  
        cv.ellipse(img,centroboca,(int(50*factorescaladoooor), lengua),0,0,360,(0,0,255),-1)  
  
  
    #todo el codigo de la mascarilla, se pone al final para que quede encima de los demas elementos  
        png = mascarilla  
        print('datos img', img.shape)  
        columna = x+ int(w*.10)  
        fila = y+ int(h*0.40)  
        if y + alto_mask <= fondo.shape[0] and x + ancho_mask <= fondo.shape[1]:  
             for i in range(mascarilla.shape[0]):  
                for j in range (mascarilla.shape[1]):  
                    if (mascarilla[i,j][3]!= 0):  
                        img[i+fila,j+columna] = mascarilla[i,j]  
  
        enfriamientoojos+=2  
  
        if enfriamientoojos > 100:  
            color = negro  
  
        if enfriamientoojos > 150:  
            color = blanco  
  
        if enfriamientoojos > 200:  
            enfriamientoojos = 0      
              
cv.imshow('img', img)  
    cv.imshow('fondo',fondo)  
    if cv.waitKey(1)== ord('q'):  
        break
  ```
En esta parte del código agregamos los demás elementos visuales, como la nariz, las orejas, la boca y lengua, teniendo esta última una especie de animación en la que cambia de tamaño simulando movimiento, por último agregamos nuestra imagen en formato png con transparencia sobre la boca.        

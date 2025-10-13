import cv2 as cv 
import math

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
        cv.circle(img, (ojo1_cx, ojo1_cy), ojo_radio + 1, (0, 0, 0), 2)
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

        if posx - ojo1_cx > ojo_radio - radio or posx - ojo1_cx < -(ojo_radio - radio):
            velx *= -1
        if posy - ojo1_cy > ojo_radio - radio or posy - ojo1_cy < -(ojo_radio - radio):
            vely *= -1

        if posx2 - ojo2_cx > ojo_radio - radio or posx2 - ojo2_cx < -(ojo_radio - radio):
            velx *= -1
        if posy2 - ojo2_cy > ojo_radio - radio or posy2 - ojo2_cy < -(ojo_radio - radio):
            vely *= -1

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
    
cap.release()
cv.destroyAllWindows()
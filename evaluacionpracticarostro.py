import cv2 as cv 

rostro = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()
    gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    radio = 5
    velx, vely = 60,70
    
    rostros = rostro.detectMultiScale(gris, 1.3, 5)
    for(x,y,w,h) in rostros:
        posx, posy = x+ int(w*.50), y+ int(h*0.80)
        
        res = int((w+h)/8)
        img = cv.rectangle(img, (x,y), (x+w, y+h), (234, 23,23), 5)
        img = cv.rectangle(img, (x,int(y+h/2)), (x+w, y+h), (0,255,0),5 )
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 21, (0, 0, 0), 2 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 21, (0, 0, 0), 2 )
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 20, (255, 255, 255), -1 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 20, (255, 255, 255), -1 )
        img = cv.circle(img, (x + int(w*0.3),y + int(h*0.4)) , radio, (0, 0, 255), -1 )
        
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) ,radio, (0, 0, 255), -1 )
        img = cv.rectangle(img, (x+ int(w*0.05), y+int(h*0.30)),(x+ int(w*0.10),y+ int(h*0.60)),(0,0,255), -1)
        img = cv.rectangle(img, (x+ int(w*0.95),y+ int(h*0.30)),(x+ int(w*0.90), y+int(h*0.60)),(0,0,255), -1)
        cv.ellipse(img, (x+ int(w*.50),y+ int(h*0.80)), (50, 25), 0, 0, 360, (0, 0, 0), -1)
        cv.ellipse(img,(x+ int(w*.50),y+ int(h*0.80)),(40,60),0,0,180,(0,0,255),-1)
        posx += velx; posy+= vely
        


        

    cv.imshow('img', img)
    if cv.waitKey(1)== ord('q'):
        break
    
cap.release
cv.destroyAllWindows()
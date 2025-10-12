import cv2
import numpy as np

ancho, alto = 600, 400      


x, y = 100, 100
velx, vely = 5, 3
radio = 30


x2, y2 = 300.0, 200.0   
velx2, vely2 = 0.0, 0.0 
radio2 = 20
esquivando = False       

while True:
    frame = np.zeros((alto, ancho, 3), dtype=np.uint8)

    
    cv2.circle(frame, (int(round(x)), int(round(y))), radio, (255, 255, 255), -1) 
    cv2.circle(frame, (int(round(x2)), int(round(y2))), radio2, (0, 0, 255), -1)   

    cv2.imshow("Pelotas programa", frame)

    x += velx
    y += vely
    if x - radio <= 0 or x + radio >= ancho:
        velx = -velx
    if y - radio <= 0 or y + radio >= alto:
        vely = -vely

    
    dx, dy = x2 - x, y2 - y
    dist = np.hypot(dx, dy)

    
    if dist < radio + radio2 + 10 and not esquivando:
        esquivando = True
        
        if abs(dx) > abs(dy):
            velx2 = 8 if dx > 0 else -8  
            vely2 = 0
        else:
            vely2 = 8 if dy > 0 else -8  
            velx2 = 0

   
    if esquivando:
        x2 += velx2
        y2 += vely2

        
        if dist > radio + radio2 + 80:
            velx2, vely2 = 0, 0
            esquivando = False

        
        if x2 - radio2 <= 0 or x2 + radio2 >= ancho:
            velx2 = -velx2

        if y2 - radio2 <= 0 or y2 + radio2 >= alto:
            vely2 = -vely2

    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
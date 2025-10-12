import cv2
import numpy as np

ancho, alto = 600, 400     
x, y = 100, 100               
velx, vely = 5, 3                 
radio = 30                   

while True:
    frame = np.zeros((alto, ancho, 3), dtype=np.uint8)   
   
    cv2.circle(frame, (x, y), radio, (255, 255, 255), -1)    
   
   
    cv2.imshow("Círculo en movimiento", frame)            
   
    x += velx; y += vely                                      
   
    if x - radio <= 0 or x + radio >= ancho: velx = -velx   
   
    if y - radio <= 0 or y + radio >= alto: vely = -vely  
   
   
   
   
    if cv2.waitKey(30) & 0xFF == ord('q'):                      
        break
cv2.destroyAllWindows()
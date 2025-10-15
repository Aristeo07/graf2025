import numpy as np
import cv2 as cv
import math

#IMAGEN2 ESCALAR 2 ROTAR 45 FILTRO BILINEAL

imagen1 = cv.imread('kingcrimson.jpeg',3)


x,y,_ = imagen1.shape
lienzo = np.zeros((x,y,3),dtype=np.uint8)
teta = math.radians(45)

coseno = math.cos(teta)
seno = math.sin(teta)

#coordenadas centro
cx, cy = x//2 , y//2





escala_x, escala_y, = 2,2

imagen_escalada = np.zeros((int(x * escala_x), int(y * escala_y),3), dtype=np.uint8)


#escalado modo raw en factor de 2
for i in range(x):
    for j in range(y):


        imagen_escalada[i*2:(i+1)*2, j*2:(j+1)*2] = imagen1[i,j]

    




new_x = int(abs(x * coseno) + abs(y * seno))
new_y = int(abs(x * seno) + abs(y * coseno))

lienzo = np.zeros((new_x, new_y, 3), dtype=np.uint8)


cx, cy = x // 2, y // 2
new_cx, new_cy = new_x // 2, new_y // 2

for i in range(new_x):
    for j in range(new_y):
       
        x_shifted = i - new_cx
        y_shifted = j - new_cy

    
        src_x = x_shifted * coseno + y_shifted * seno + cx
        src_y = -x_shifted * seno + y_shifted * coseno + cy

        src_x = int(round(src_x))
        src_y = int(round(src_y))

       
        if 0 <= src_x < x and 0 <= src_y < y:
            lienzo[i, j] = imagen1[src_x, src_y]

imagen_bilinear2 = cv.bilateralFilter(lienzo,9,100,100)    

cv.imshow('IMAGEN1',imagen_bilinear2)

cv.waitKey(0)
cv.destroyAllWindows

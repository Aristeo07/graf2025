import cv2 as cv
import numpy as np
import math


#IMAGEN 3 TRASLADAR AL CENTRO ROTAR 90 GRADOS ESCALAR 2 FILTRO BILINEAL
img = cv.imread('kingcrimson.jpeg', 0)


x, y = img.shape
teta = math.radians(90)

coseno = math.cos(teta)
seno = math.sin(teta)

cx, cy = x//2 , y//2


translated_img = np.zeros((x, y), dtype=np.uint8)


dx, dy = x//2, y//2

#traslado al centro
for i in range(x):
    for j in range(y):
        new_x = i + dx
        new_y = j + dy
        if 0 <= new_x < x and 0 <= new_y < y:
            translated_img[new_x, new_y] = img[i, j]


new_x = int(abs(x * coseno) + abs(y * seno))
new_y = int(abs(x * seno) + abs(y * coseno))

lienzo = np.zeros((new_x, new_y, 3), dtype=np.uint8)


cx, cy = x // 2, y // 2
new_cx, new_cy = new_x // 2, new_y // 2

#rotacion de 90 grados
for i in range(new_x):
    for j in range(new_y):
       
        x_shifted = i - new_cx
        y_shifted = j - new_cy

    
        src_x = x_shifted * coseno + y_shifted * seno + cx
        src_y = -x_shifted * seno + y_shifted * coseno + cy

        src_x = int(round(src_x))
        src_y = int(round(src_y))

       
        if 0 <= src_x < x and 0 <= src_y < y:
            lienzo[i, j] = img[src_x, src_y]

imagen_filtro = cv.bilateralFilter(lienzo,9,75,75)





cv.imshow('traslado',translated_img)
cv.imshow('rotar',lienzo)
cv.imshow('IMAGEN3',imagen_filtro)
cv.waitKey(0)
cv.destroyAllWindows
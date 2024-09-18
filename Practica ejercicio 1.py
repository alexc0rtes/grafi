import cv2 as cv
import numpy as np
import math

# Cargar la imagen en escala de grises
img = cv.imread('img.png', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Crear una imagen vacía para almacenar el resultado
mod_img = np.zeros((x*2, y*2), dtype=np.uint8)
xx, yy = mod_img.shape

# Calcular el centro de la imagen
cx, cy = int(x  // 2), int(y  // 2)

# Ángulo de rotación 60°
angle = 60
theta = math.radians(angle)

# Desplazamiento de 10 pixeles
dx, dy = 10, 10

# Factor de escala 1/5
scale_x, scale_y = 0.2, 0.2

# Modificar la imagen: rotar 60°, trasladar 10 pixeles y escalar a 1/5
for i in range(x):
    for j in range(y):
        new_x = int(((j - cx) * math.cos(theta) - (i - cy) * math.sin(theta) + cx + dx) * scale_x)
        new_y = int(((j - cx) * math.sin(theta) + (i - cy) * math.cos(theta) + cy + dy) * scale_y)
        if 0 <= new_x < yy and 0 <= new_y < xx:
            mod_img[new_y, new_x] = img[i, j]

# Mostrar la imagen original y la modificada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen modificada', mod_img)
cv.waitKey(0)
cv.destroyAllWindows()
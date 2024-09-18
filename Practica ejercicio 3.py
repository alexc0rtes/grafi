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

# Ángulo de rotación 70°
angle = 70
theta = math.radians(angle)

# Desplazamiento de 20 pixeles
dx, dy = 20, 20

# Factor de escala 2
scale_x, scale_y = 2, 2

# Modificar la imagen: rotar 70° escalar a 2 y trasladar 20 pixeles
for i in range(x):
    for j in range(y):
        new_x = int(((j - cx) * math.cos(theta) - (i - cy) * math.sin(theta) + cx) * scale_x) + dx
        new_y = int(((j - cx) * math.sin(theta) + (i - cy) * math.cos(theta) + cy) * scale_y) + dy
        if 0 <= new_x < yy and 0 <= new_y < xx:
            mod_img[new_y, new_x] = img[i, j]

# Mostrar la imagen original y la modificada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen modificada', mod_img)
cv.waitKey(0)
cv.destroyAllWindows()
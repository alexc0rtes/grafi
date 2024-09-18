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

# Ángulo de rotación 30° y -60°
angle_1 = 30
theta_1 = math.radians(angle_1)
angle_2 = -60
theta_2 = math.radians(angle_2)

# Factor de escala 2
scale_x, scale_y = 2, 2

# Modificar la imagen: rotar 30°, rotar -60° y escalar a 2
for i in range(x):
    for j in range(y):
        new_x = int(((j - cx) * math.cos(theta_1) - (i - cy) * math.sin(theta_1) + cx))
        new_y = int(((j - cx) * math.sin(theta_1) + (i - cy) * math.cos(theta_1) + cy))
        new_x = int(((j - cx) * math.cos(theta_2) - (i - cy) * math.sin(theta_2) + cx) * scale_x)
        new_y = int(((j - cx) * math.sin(theta_2) + (i - cy) * math.cos(theta_2) + cy) * scale_y)
        if 0 <= new_x < yy and 0 <= new_y < xx:
            mod_img[new_y, new_x] = img[i, j]

# Mostrar la imagen original y la modificada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen modificada', mod_img)
cv.waitKey(0)
cv.destroyAllWindows()
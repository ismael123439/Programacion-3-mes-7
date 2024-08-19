import time
from PIL import Image
import numpy as np

# Crear una imagen en escala de grises para pruebas
def crear_imagen_prueba(tamano, tono):
    imagen = Image.new('L', tamano, tono)
    return imagen

# Pruebas de tiempo
def medir_tiempo(imagen_path, tono):
    start_time = time.time()
    resultado = busqueda_en_imagen(imagen_path, tono)
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    return resultado

# Crear imágenes y probar
tamano = (100, 100)
tono = 128
imagen = crear_imagen_prueba(tamano, tono)
imagen_path = 'imagen_prueba.png'
imagen.save(imagen_path)

# Medir tiempo de ejecución
resultado = medir_tiempo(imagen_path, tono)
print(f"Cantidad de píxeles encontrados: {len(resultado)}")

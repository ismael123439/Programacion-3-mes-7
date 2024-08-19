from PIL import Image

def busqueda_en_imagen(imagen_path, tono):

    imagen = Image.open(imagen_path).convert('L')  
    ancho, alto = imagen.size
    pixeles = imagen.load()
    
    resultado = {}
    
    for y in range(alto):
        for x in range(ancho):
            if pixeles[x, y] == tono:
                resultado[(x, y)] = tono
    
    return resultado

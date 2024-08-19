import random
import time

# Crear listas de diferentes tamaños
tamanos = [10, 100, 1000, 10000]
elemento_a_buscar = 500  # Elemento que se buscará en las listas

for tamano in tamanos:
    lista = sorted(random.sample(range(1, 10000), tamano))
    
    # Prueba de búsqueda lineal
    inicio = time.time()
    indice_lineal = busqueda_lineal(lista, elemento_a_buscar)
    fin = time.time()
    tiempo_lineal = fin - inicio
    
    # Prueba de búsqueda binaria
    inicio = time.time()
    indice_binaria = busqueda_binaria(lista, elemento_a_buscar)
    fin = time.time()
    tiempo_binaria = fin - inicio
    
    print(f"Lista de tamaño {tamano}:")
    print(f"  Búsqueda lineal tomó {tiempo_lineal:.6f} segundos.")
    print(f"  Búsqueda binaria tomó {tiempo_binaria:.6f} segundos.\n")

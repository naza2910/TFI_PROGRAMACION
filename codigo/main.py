#Tecnicatura Universitaria en Programación-Facultad Tecnologica Nacional
# Cátedra: programación I
# Comision: 5
# Docente: [Cinthia Rigoni]
# Tutor: [Walter Pintos]
# Alumno: [Leandro Torres Galarzo]
# Dni :41.694.490

# Alumno: [Nazareno Romero]
# Dni : 47.629.746
# Trabajo Integrador: Algoritmos de Ordenamiento y Búsqueda en Python


def bubble_sort(arr):
    """
    Implementación del algoritmo de ordenamiento Bubble Sort.
    Ordena una lista de números de forma ascendente, comparando y
    intercambiando elementos adyacentes hasta que la lista esté ordenada.

    Parámetros:
    arr (list): La lista de números que se desea ordenar.

    Retorna:
    list: La lista original, pero ahora ordenada de forma ascendente.
          (Nota: Bubble Sort modifica la lista en el lugar).
    """
    n = len(arr)
    # Bucle exterior: controla las pasadas por la lista.
    # En cada pasada, el elemento más grande restante "burbujea" a su posición final.
    for i in range(n - 1):
        # Bandera para optimización: si no hay intercambios en una pasada, la lista está ordenada.
        intercambio_realizado = False
        # Bucle interior: compara elementos adyacentes y los intercambia si están en el orden incorrecto.
        # El "-i" es porque los últimos 'i' elementos ya están en su posición final.
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Intercambio de elementos
                intercambio_realizado = True
        
        # Si no hubo ningún intercambio en esta pasada, la lista ya está ordenada.
        if not intercambio_realizado:
            break
    return arr

def insertion_sort(arr):
    """
    Implementación del algoritmo de ordenamiento Insertion Sort.
    Construye la lista ordenada un elemento a la vez. Cada elemento nuevo se inserta
    en su posición correcta dentro de la sublista ya ordenada.

    Parámetros:
    arr (list): La lista de números que se desea ordenar.

    Retorna:
    list: La lista original, pero ahora ordenada de forma ascendente.
          (Nota: Insertion Sort modifica la lista en el lugar).
    """
    # Recorremos la lista desde el segundo elemento (índice 1) hasta el final.
    # El primer elemento (índice 0) se considera una sublista ya ordenada.
    for i in range(1, len(arr)):
        clave = arr[i] # Almacenamos el elemento actual que queremos insertar.
        j = i - 1      # Iniciamos la comparación con el elemento anterior.

        # Movemos los elementos de la sublista ordenada que son mayores que 'clave'
        # una posición adelante de su posición actual para hacer espacio para 'clave'.
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j] # Mueve el elemento hacia la derecha
            j -= 1              # Se mueve a la izquierda para comparar con el siguiente elemento
        
        arr[j + 1] = clave # Inserta la 'clave' en su posición correcta.
    return arr

def selection_sort(arr):
    """
    Implementación del algoritmo de ordenamiento Selection Sort.
    En cada pasada, encuentra el elemento mínimo de la parte no ordenada de la lista
    y lo coloca al principio de la parte ordenada.

    Parámetros:
    arr (list): La lista de números que se desea ordenar.

    Retorna:
    list: La lista original, pero ahora ordenada de forma ascendente.
          (Nota: Selection Sort modifica la lista en el lugar).
    """
    n = len(arr)
    # Recorremos la lista desde el primer elemento hasta el penúltimo.
    # En cada iteración 'i', estamos buscando el elemento más pequeño para colocarlo en la posición 'i'.
    for i in range(n - 1):
        # Asumimos que el elemento actual es el mínimo.
        indice_minimo = i

        # Buscamos el verdadero elemento mínimo en la parte no ordenada de la lista.
        # Empezamos desde el elemento siguiente al actual (i + 1).
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j # Actualizamos el índice del mínimo si encontramos uno menor.
        
        # Una vez que encontramos el elemento mínimo en la parte no ordenada,
        # lo intercambiamos con el elemento en la posición actual 'i'.
        # Esto coloca el elemento más pequeño en su posición correcta.
        if indice_minimo != i: # Solo intercambiamos si el mínimo no es el mismo que el actual.
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]
    return arr

def busqueda_binaria(arr, elemento_a_buscar):
    """
    Implementación del algoritmo de búsqueda binaria.
    Este algoritmo es altamente eficiente para encontrar un elemento
    específico en una lista que DEBE estar previamente ordenada.

    Funciona dividiendo repetidamente por la mitad la porción de la lista
    donde podría estar el elemento.

    Parámetros:
    arr (list): La lista de números en la que se buscará.
                ¡Importante! Esta lista debe estar ORDENADA.
    elemento_a_buscar: El valor que se desea encontrar en la lista.

    Retorna:
    int: El índice (posición) del 'elemento_a_buscar' si se encuentra.
         Si el elemento no está en la lista, retorna -1.
    """
    bajo = 0                    # El índice del inicio de la sublista actual a buscar.
    alto = len(arr) - 1         # El índice del final de la sublista actual a buscar.

    # El bucle continúa mientras el rango de búsqueda sea válido (bajo no ha cruzado alto).
    while bajo <= alto:
        medio = (bajo + alto) // 2  # Calcula el índice del elemento central.
                                    # Usamos división entera (//) para asegurar un índice válido.

        # Comparamos el elemento del medio con el que estamos buscando.
        if arr[medio] == elemento_a_buscar:
            return medio  # ¡Elemento encontrado! Retornamos su índice.
        
        # Si el elemento del medio es menor que el que buscamos,
        # significa que el elemento (si existe) debe estar en la mitad derecha.
        elif arr[medio] < elemento_a_buscar:
            bajo = medio + 1  # Ajustamos el límite inferior para buscar en la mitad derecha.
        
        # Si el elemento del medio es mayor que el que buscamos,
        # significa que el elemento (si existe) debe estar en la mitad izquierda.
        else: # arr[medio] > elemento_a_buscar
            alto = medio - 1  # Ajustamos el límite superior para buscar en la mitad izquierda.
            
    return -1 # Si el bucle termina, el elemento no se encontró en la lista.

# --- Bloque principal para demostrar el uso de los algoritmos ---
if __name__ == "__main__":
    print("--- Demostración de Algoritmos de Ordenamiento y Búsqueda ---")

    # --- Bubble Sort ---
    print("\n--- Demostración de Bubble Sort ---")
    datos_bubble = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista original (Bubble Sort): {datos_bubble}")
    # Es crucial usar .copy() para que la función ordene una copia y no modifique la lista original de este ejemplo.
    lista_bubble_ordenada = bubble_sort(datos_bubble.copy())
    print(f"Lista después de Bubble Sort: {lista_bubble_ordenada}")

    # --- Insertion Sort ---
    print("\n--- Demostración de Insertion Sort ---")
    datos_insertion = [12, 11, 13, 5, 6]
    print(f"Lista original (Insertion Sort): {datos_insertion}")
    lista_insertion_ordenada = insertion_sort(datos_insertion.copy())
    print(f"Lista después de Insertion Sort: {lista_insertion_ordenada}")

    # --- Selection Sort ---
    print("\n--- Demostración de Selection Sort ---")
    datos_selection = [64, 25, 12, 22, 11]
    print(f"Lista original (Selection Sort): {datos_selection}")
    lista_selection_ordenada = selection_sort(datos_selection.copy())
    print(f"Lista después de Selection Sort: {lista_selection_ordenada}")

    # --- Búsqueda Binaria ---
    # Para la búsqueda binaria, la lista DEBE estar ordenada.
    # Usaremos una lista ya ordenada para este ejemplo. En un caso real,
    # usarías una de las listas que ordenaste previamente.
    print("\n--- Demostración de Búsqueda Binaria (sobre lista ordenada) ---")
    # Nota: Asegúrate de que esta lista esté realmente ordenada para que la búsqueda binaria funcione.
    lista_para_busqueda_binaria = [5, 11, 12, 19, 22, 23, 25, 32, 34, 45, 62, 88, 90]
    print(f"Lista ordenada para búsqueda binaria: {lista_para_busqueda_binaria}")

    # Búsqueda de elemento existente
    elemento_existente = 23
    posicion = busqueda_binaria(lista_para_busqueda_binaria, elemento_existente)
    if posicion != -1:
        print(f"'{elemento_existente}' encontrado en la posición (índice): {posicion}")
    else:
        print(f"'{elemento_existente}' no encontrado en la lista.")

    # Búsqueda de elemento no existente
    elemento_no_existente = 100
    posicion = busqueda_binaria(lista_para_busqueda_binaria, elemento_no_existente)
    if posicion != -1:
        print(f"'{elemento_no_existente}' encontrado en la posición (índice): {posicion}")
    else:
        print(f"'{elemento_no_existente}' no encontrado en la lista.")

    print("\n--- Fin de la demostración ---")
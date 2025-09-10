###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

# nlist = mensaje[7:14]
# print(nlist)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# Intercambia la primera y la última posición utilizando solo asignación por índice.
# numeros = [10, 20, 30, 40, 50]
# print(numeros[4],numeros[1],numeros[2],numeros[3],numeros[0])

#otro metodo

# numeros[0] = 50
# numeros[-4] = 10
# print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:

# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# sandwich = pan + ingredientes + pan_abajo

# print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
# nueva_lista = lista + lista
# nueva_lista = lista + [1,2,3]
# nueva_lista = lista * 2

# print(nueva_lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
# lista = [10, 20, 30, 40, 50]
# centro = lista[2]
# print(f"El centro es {centro}")

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
# lista = [1, 2, 3, 4, 5, 6]
# n = len(lista)
# print(len(lista))
# mitad = n // 2
# reversa_parcial = lista[:mitad][::-1] + lista[mitad:]
# print(reversa_parcial)
import os

os.system("clear")

lista1 = [1, 2, 3, 4, 5]

lista2 = ["manzana", "banana", "cereza"]


lista_vacia = []

lista_de_listas = [[1, 2], ['calcetin', 4]] # type: ignore

matrix = [[1, 2], [2, 3], [4, 5]]

print("Acceso a elementos por indice")

print(lista2[0])  # Primer elemento
print(lista2[1])  # Segundo elemento
print(lista2[-1])  # tercer elemento
print(lista2[-2])  # segundo elemento


print(lista_de_listas[1][0]) # type: ignore

print(lista1[1:4])
print(lista1[:3])
print(lista1[3:])
print(lista1[:])
print(lista1[::2])
print(lista1[::-1])

#modificar listas

lista1[0] = 10
print(lista1)

lista1 = [1 , 2 , 3]
lista1 = lista1 + [4 , 5, 6]
lista1 += [7 , 8, 9]

print(len(lista1))
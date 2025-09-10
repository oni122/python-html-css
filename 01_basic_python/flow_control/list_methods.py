import os 
#limpiar pantalla#
os.system("cls")

#agregar elementos a una lista#
lista1 = ['a', 'b', 'c', 'd']

lista1.append('e')

print(lista1)

lista1.insert(1,'@')

print(lista1)

lista1.extend(['f','g','h'])
print(lista1)


lista1.remove('@')

print(lista1)

lista1.pop()

print(lista1)

lista1.insert(1,'@')

print(lista1)

#eliminar elementos de una lista#
lista1.pop(-1)

print(lista1)

del lista1[1]
print(lista1)

lista1.clear()

lista1 = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
del lista1[0:1]
print(lista1)

#ordenar listas#
numbers = [1, 3, 2]
numbers.sort()
print(numbers)

numbers = [1, 3, 2]
sorted_numbers=sorted(numbers)
print(numbers)


frutas = ['banana', 'apple', 'cherry']
sorted_frutas=sorted(frutas)
print(sorted_frutas)

frutas = ['banana', 'apple', 'cherry']
frutas.sort(key=str.lower)
print(frutas)

print(len(frutas))
print(frutas.count('banana'))
import os
os.system('cls')

# frutas = ["manzana", "banana", "cereza"]

# for fruta in frutas:
#     print(fruta)


# cadena = "Hola"
# for c in cadena:
#     print(c)

# for index, fruta in enumerate(frutas):
#     print(f"indice: {index}, {fruta}")



# letras = ['a', 'b', 'c']
# numeros = [1, 2, 3]

# for letra in letras:
#     for numero in numeros:
#         print(f"{letra}{numero}")


# animales = ["perro", "gato", "pez"]
# for idx, animal in enumerate(animales):
#     print(animal)
#     if animal == "perro":
#         print(f"El indice del perro es: {idx}")
#         break

animales = ["perro", "gato", "pez"]
animales_mayus = [a.upper() for a in animales]
print(animales_mayus)

pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)
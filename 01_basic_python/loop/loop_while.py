
# contador = 0

# while contador < 5 :
#     print(contador)
#     contador += 1

# while True:
#     print("Ciclo infinito")
#     contador += 1
#     if contador == 5:
#         break

# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue

#     print(contador)


# contador = 0

# while contador < 5 :
#     print(contador)
#     contador += 1
# else:
#     print("El ciclo ha finalizado")


numero = -1
while numero <= 0:
    try:
        numero = int(input("Ingrese un numero positivo: "))
        if numero <= 0:
            print("El numero debe ser positivo")
    except:
            print("Debes ingresar un numero !")

print(f"El numero ingresado es: {numero}")
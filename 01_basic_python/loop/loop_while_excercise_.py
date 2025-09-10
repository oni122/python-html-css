import os
os.system('cls')
###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# n = 10
# while n > 0:
#     print(n)
#     n -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# suma = 0
# n = 1
# while n <= 20:
#     if n % 2 == 0:
#         suma += n
#     n += 1
# print(f"La suma de los números pares entre 1 y 20 es: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# numero = int(input("Ingrese un número entero positivo: "))
# factorial = 1
# contador = 1
# while contador <= numero:
#     factorial *= contador
#     contador += 1
# print(f"El factorial de {numero} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# contraseña = ""
# while len(contraseña) < 8:
#     contraseña = input("Ingrese una contraseña (mínimo 8 caracteres): ")
#     if len(contraseña) < 8:
#         print("La contraseña es demasiado corta. Inténtalo de nuevo.")
# else:
#     print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# numero = 0

# while numero < 1:
#     try:
#         numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
#         contador = 1
#         while contador <= 10:
#             resultado = numero * contador
#             print(f"{numero} x {contador} = {resultado}")
#             contador += 1
#     except:
#         print("Debes ingresar un número")


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

# n = int(input("Introduce un número entero positivo N: "))

# numero = 2
# while numero <= n:
#   es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
#   divisor = 2
#   while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
#     if numero % divisor == 0:
#       es_primo = False  # Si encontramos un divisor, no es primo
#       break  # Salimos del bucle interior
#     divisor += 1
#   if es_primo:
#     print(numero)

#   numero += 1


###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
# numero1 = int(input("Introduce el primer número: "))
# numero2 = int(input("Introduce el Segundo número: "))
# if numero1 > numero2:
#     print(f"el numero mayor es: {numero1}")
# elif numero2 > numero1:
#     print(f"el numero mayor es : {numero2}")
# else :
#     print("los numeros son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
# num1 = float(input("Introduce el primer número: "))
# num2 = float(input("Introduce el Segundo número: "))
# operacion = input("Introduce la operación (+, -, *, /): ")
# if operacion == "+" or "suma" or "sumar":
#     print(f"el resultado de la sumas es: {num1 + num2}")
# elif operacion == "-" or "resta" or "restar":
#     print(f"el resultado de la resta es: {num1 - num2}")
# elif operacion == "*" or "multiplicacion" or "multiplicar":
#     print(f"el resultado de la multiplicacion es: {num1 * num2}")
# elif operacion == "/" or "division" or "dividir":
#     if num2 != 0:
#         print(f"el resultado de la division es: {num1 / num2}")
#     else:
#         print("Error: División entre cero no está permitida.")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
# año = int(input("introduce un año: "))

# if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#     print(f"el año {año} es bisiesto")
# else:
#     print(f"el año {año} no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# edad = int(input("Introduce una edad: "))
# if edad >=0 and edad <=2:
#     print("Es un Bebe!")
# elif edad >=3 and edad <=12:
#     print("Es un Niño!")
# elif edad >=13 and edad <=17:
#     print("Es un Adolescente!")
# elif edad >=18 and edad <=64:
#     print("Es un Adulto!")
# elif edad >=65:
#     print("Es un Adulto mayor!")
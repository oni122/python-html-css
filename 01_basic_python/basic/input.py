nombre = input("ingresa tu nombre:")
apellido = input("ingresa tu apellido:")

print(f"Hola {nombre} {apellido}, un gusto saludarte")

edad = int(input("ingresa tu edad:"))
print(f"El año que viene tendrás {edad + 1} años")

#multiples inputs

ciudad, pais = input("ingresa ciudad y pais").split(" ")
print(f"Vives en {ciudad} que está en {pais}") 

ciudad, pais = input("ingresa ciudad y pais").split(",")
print(f"Vives en {ciudad} que está en {pais}")


# def saludar():
#     print("Hola, ¿cómo estás?")

# saludar()

# def saludar_a(nombre: str): 
#     print(f" Hola {nombre}")

# saludar_a("María")

# def sumar(a:int, b:int):
#     sumar = a + b
#     return sumar

# resultado = sumar(3, 5)
# print(resultado)

# def restar(a:int, b:int):

#     return a - b

# def multiplicar(a:int, b = 2): # type: ignore
#     return a * b

# print(multiplicar(2))

# def persona(nombre: str, edad:int, ciudad:str):
#     print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# persona("Ana", 25, "Madrid")
# persona(ciudad="Barcelona", nombre="Luis", edad=30)

def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma
print(sumar_numeros(1,2,3,4,5))

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=28, ciudad="Valencia")
mostrar_info(producto="Laptop", precio=1200, stock=30)
mostrar_info(nombre="Laura", profesion=True, pais="Chile")
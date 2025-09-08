import os 
os.system("clear")

edad = 18
permiso = False
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


if edad >= 18 and permiso:
    print("Puedes conducir")
else:
    print("No puedes conducir")

if edad >= 18 or permiso:
    print("Puedes conducir")
else:
    print("No puedes conducir")


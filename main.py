# Autor: Gastán Tomás Huete
# Date: 18/09/2022

# variables globales a las que accedera el usuario
gender = input("Que eres, ¿hombre o mujer?: ")
name = ""

if gender == "hombre".lower():
    name = input("Muy bien, bienvenido... como deberias llamarte viajero? -> ")

if gender == "mujer".lower():
    name = input("Muy bien, bienvenida... como deberias llamarte viajera? -> ")

# nombre ya inputeado
print("Muy bien " + name + ", seras el ", end="")
print("heroe", end="") if gender == "hombre".lower() else print("heroina", end="")
print(" de esta leyenda.")

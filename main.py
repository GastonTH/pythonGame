# Autor: Gastán Tomás Huete
# Date: 18/09/2022

# variable that the user can modify
name = ""
gender = ""
# TODO ourHero = HeroClass.Hero

# add the hero in the code
gender = input("Dime que eres, un hombre o una mujer: ")  # <-- Error that i dont understand XD
print("Perfecto")

if gender == "hombre".lower():
    name = input("Muy bien, bienvenido... como deberias llamarte viajero? -> ")

if gender == "mujer".lower():
    name = input("Muy bien, bienvenida... como deberias llamarte viajera? -> ")

# nombre ya inputeado
print("Muy bien " + name + ", seras el ", end="")
print("heroe", end="") if gender == "hombre".lower() else print("heroina", end="")
print(" de esta leyenda.")

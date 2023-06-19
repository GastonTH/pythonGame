# Autor: Gastán Tomás Huete
# Date: 18/06/2023

################################FIXFIXFIXFIXFIXFIXFIXFIXFIXFIXFIX#############################################
import os
import sys

# Add the father's directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
##############################################################################################################

# imports from the game
from lib.HeroClass import Hero
from utils.utils import *
from data.info_class import *
import time
# ----------------------

# variable that the user can modify
ourHero = Hero
select_character_class = ""

# add the hero in the code

print("Dime que eres, un hombre o una mujer")

while True:
    ourHero.gender = input(" -> ").lower()
     
    if ourHero.gender == "hombre".lower():
        ourHero.name = input("Muy bien, bienvenido... como deberias llamarte viajero? -> ")
        break
    elif ourHero.gender == "mujer".lower():
        ourHero.name = input("Muy bien, bienvenida... como deberias llamarte viajera? -> ")
        break
    else:
        print("No entiendo, intentalo de nuevo")

print("Perfecto")
time.sleep(1)

# whit params
print("Muy bien " + ourHero.name + ", seras el ", end="")
print("novato", end="") if ourHero.gender == "hombre" else print("novata", end="")
print(" de esta leyenda.")

print("Ahora decidiras tu estilo de combate.")
print("Estas son las clases a las que puedes optar ", end="")
print("novato") if ourHero.gender == "hombre".lower() else print("novata")
time.sleep(1)
warrior_info()
time.sleep(1)
mage_info()
time.sleep(1)
archer_info()
time.sleep(1)
print("Y por ultimo, pero no menos importante.")
rogue_info()
time.sleep(1)
print("Y bien... que decides") 
time.sleep(0.5)

while True:
        select_character_class = input(" -> ")
        if select_character_class.lower() == "guerrero" or select_character_class.lower() == "guerrera":
            if ourHero.gender == "hombre":
                print("Perfecto, seras un guerrero")
            else:
                print("Perfecto, seras una guerrera")
            break
        elif select_character_class.lower() == "arquero" or select_character_class.lower() == "arquera":
            if ourHero.gender == "hombre":
                print("Perfecto, seras un arquero")
            else:
                print("Perfecto, seras una arquera")
            break
        elif select_character_class.lower() == "asesino" or select_character_class.lower() == "asesina":
            if ourHero.gender == "hombre":
                print("Perfecto, seras un asesino")
            else:
                print("Perfecto, seras una asesina")
            break
        elif select_character_class.lower() == "mago" or select_character_class.lower() == "maga":
            if ourHero.gender == "hombre":
                print("Perfecto, seras un mago")
            else:
                print("Perfecto, seras una maga")
            break
        else:
            print("No contemplo esa opcion, prueba otra vez...")

print("Ahora, te asignaremos las estadisticas en funcion a tu eleccion...")
ourHero.setStats()
loading_animation()
# ----------------------------------------------------------------------------------------------
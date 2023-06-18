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
from utils.utils import clear_console
from data.info_class import *
import time
# ----------------------

# variable that the user can modify
ourHero = Hero
select_character_class = ""

# add the hero in the code
ourHero.gender = input("Dime que eres, un hombre o una mujer: ")
print("Perfecto")

if ourHero.gender == "hombre".lower():
    ourHero.name = input("Muy bien, bienvenido... como deberias llamarte viajero? -> ")

if ourHero.gender == "mujer".lower():
    ourHero.name = input("Muy bien, bienvenida... como deberias llamarte viajera? -> ")

# nombre ya inputeado
print("Muy bien " + ourHero.name + ", seras el ", end="")
print("novato", end="") if ourHero.gender == "hombre".lower() else print("novata", end="")
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
print("Y bien...", end="") 
time.sleep(0.5)
select_character_class = input(" que decides")

while True:
        if select_character_class.lower() == "guerrero" or select_character_class.lower() == "guerrera":
            print("Perfecto, seras")
            break
        elif select_character_class.lower() == "arquero" or select_character_class.lower() == "arquera":
            print()
            break
        elif select_character_class.lower() == "asesino" or select_character_class.lower() == "asesina":
            print()
            break
        elif select_character_class.lower() == "mago" or select_character_class.lower() == "maga":
            print()
            break
        else:
            print("No contemplo esa opcion, prueba otra vez...")
# ----------------------------------------------------------------------------------------------
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
from objs.HeroClass import Hero

# variable that the user can modify
ourHero = Hero

# add the hero in the code
ourHero.gender = input("Dime que eres, un hombre o una mujer: ")
print("Perfecto")

if ourHero.gender == "hombre".lower():
    ourHero.name = input("Muy bien, bienvenido... como deberias llamarte viajero? -> ")

if ourHero.gender == "mujer".lower():
    ourHero.name = input("Muy bien, bienvenida... como deberias llamarte viajera? -> ")

# nombre ya inputeado
print("Muy bien " + ourHero.name + ", seras el ", end="")
print("heroe", end="") if ourHero.gender == "hombre".lower() else print("heroina", end="")
print(" de esta leyenda.")

# ----------------------------------------------------------------------------------------------
import os

def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

# Ejemplo de uso
clear_console()
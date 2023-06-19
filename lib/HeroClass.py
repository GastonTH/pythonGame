

class Hero:

    # construct from this class
    def __init__(self, name: str, gender: str, character_class: str):
        self.name = name
        self.gender = gender
        self.character_class= character_class
        self.level = 0
        self.experience = 0
        self.experience_t = 0
        self.vit_point_t, self.vit_point = 0, 0
        self.mana_point_t, self.mana_point = 0, 0
        self.strength = 0
        self.dexterity = 0   # critic chance -> (+2%) * dextry point
        self.intelligence = 0
        self.phy_armor = 0
        self.magic_armor = 0
    
    # set stats from this class
    def setStats(self):
        if  self.character_class == "guerrero" or self.character_class == "guerrera":

            self.vit_point_t, self.vit_point   = 350, 350
            self.mana_point_t, self.mana_point = 100, 100
            self.strength     = 200
            self.dexterity    = 1
            self.intelligence = 0
            self.phy_armor    = 100
            self.magic_armor  = 100
            self.level = 1

        elif self.character_class == "arquero" or self.character_class == "arquera":

            self.vit_point_t, self.vit_point   = 200, 200
            self.mana_point_t, self.mana_point = 250, 250
            self.strength     = 220
            self.dexterity    = 5
            self.intelligence = 5
            self.phy_armor    = 75
            self.magic_armor  = 75
            self.level = 1
            

        elif self.character_class == "asesino" or self.character_class == "asesina":

            self.vit_point_t, self.vit_point   = 250, 250
            self.mana_point_t, self.mana_point = 200, 200
            self.strength     = 260
            self.dexterity    = 10
            self.intelligence = 5
            self.phy_armor    = 75
            self.magic_armor  = 75            
            self.level = 1

        elif self.character_class == "mago" or self.character_class == "maga":

            self.vit_point_t, self.vit_point   = 150, 150
            self.mana_point_t, self.mana_point = 300, 300
            self.strength     = 50
            self.dexterity    = 2
            self.intelligence = 20
            self.phy_armor    = 50
            self.magic_armor  = 50
            self.level = 1
            
        else:
            print()
        

    # output string from this class
    def stats_sheet(self):

        cadena = ""
        cadena += "Soy " + self.name + ", " + self.character_class + " de nivel " + self.level + ".\n"

        cadena += "_____________________________________________\n"
        cadena += "|                                            \n"
        cadena += "|             ESTADÍSTICAS DEL PERSONAJE     \n"
        cadena += "|                                            \n"
        cadena += "|  Nombre:          ["+ self.name + "]\n"
        cadena += "|  Nivel:           ["+ self.level + "]\n"
        cadena += "|  Salud:           ["+ self.vit_point + " / " + self.vit_point_t + "]\n"
        cadena += "|  Mana :           ["+ self.mana_point + " / " + self.mana_point_t + "]\n"
        cadena += "|  Fuerza:          ["+ self.strength + "]\n"
        cadena += "|  Destreza:        ["+ self.dexterity + "]\n"
        cadena += "|  Inteligencia:    ["+ self.intelligence + "]\n"
        cadena += "|  Defensa Fisica:  ["+ self.phy_armor + "]\n"
        cadena += "|  Defensa Magica:  ["+ self.magic_armor + "]\n"
        cadena += "|                                           \n"
        cadena += "|  Firmado :                X               \n"
        cadena += "|___________________________________________\n"

        print(cadena)

    

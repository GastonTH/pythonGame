

class Hero:

    # construct from this class
    def __init__(self, name: str, gender: str, character_class: str, level: int, vit_point: int, mana_point: int, strength: int, dexterity: int, intelligence: int
                 ,phy_armor: int, magic_armor: int):
        self.name = name
        self.gender = gender
        self.character_class= character_class
        self.level = level
        self.vit_point = vit_point
        self.mana_point = mana_point
        self.strength = strength
        self.dexterity = dexterity   # critic chance -> (+2%) * dextry point
        self.intelligence = intelligence
        self.phy_armor = phy_armor
        self.magic_armor = magic_armor
    
    # set stats from this class
    def setStats(self):
        if  self.character_class == "guerrero" or self.character_class == "guerrera":
            self.vit_point    = 350
            self.mana_point   = 100
            self.strength     = 200
            self.dexterity    = 1
            self.intelligence = 0
            self.phy_armor    = 100
            self.magic_armor  = 100

        elif self.character_class == "arquero" or self.character_class == "arquera":
            self.vit_point    = 200
            self.mana_point   = 250
            self.strength     = 220
            self.dexterity    = 5
            self.intelligence = 5
            self.phy_armor    = 75
            self.magic_armor  = 75
            

        elif self.character_class == "asesino" or self.character_class == "asesina":
            self.vit_point    = 250
            self.mana_point   = 200
            self.strength     = 260
            self.dexterity    = 10
            self.intelligence = 5
            self.phy_armor    = 75
            self.magic_armor  = 75            

        elif self.character_class == "mago" or self.character_class == "maga":
            self.vit_point    = 150
            self.mana_point   = 300
            self.strength     = 50
            self.dexterity    = 2
            self.intelligence = 20
            self.phy_armor    = 50
            self.magic_armor  = 50
        else:
            print()

        # common stats
        self.level = 1

    # output string from this class
    def __str__(self):
        return f""

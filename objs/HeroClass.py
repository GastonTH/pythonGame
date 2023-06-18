class Hero:

    # constructo por defecto clase heroe
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

    def __str__(self):
        return f"{self.name}({self.gender})"

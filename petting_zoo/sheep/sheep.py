from datetime import date

class Sheep:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

floof = Sheep("Floof", "sheep", "midday")
print (f'{floof.name} the {floof.species} is available for pets during {floof.shift}')
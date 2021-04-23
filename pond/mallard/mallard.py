from datetime import date

class Mallard():
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
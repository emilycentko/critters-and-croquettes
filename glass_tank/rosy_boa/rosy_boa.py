from datetime import date

class RosyBoa():
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
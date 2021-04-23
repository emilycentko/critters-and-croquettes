from datetime import date

class Llama():
    def __init__(self, name, species, date_added):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


miss_fuzz = Llama("Miss Fuzz", "llama", "2020-04-23")
print(miss_fuzz)
print(miss_fuzz.name)


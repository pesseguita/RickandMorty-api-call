class Character:
    def __init__(self, name, status, species, gender, origin, location, number_of_episodes):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.location = location
        self.number_of_episodes = number_of_episodes

    def show_characters(self):
        return self.name, self.status, self.species, self.gender, self.origin, self.location, self.number_of_episodes



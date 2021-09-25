class Animal:
    def __init__(self, name, category, noise, food):
        self.name = name
        self.category = category
        self.noise = noise
        self.food = food

    @classmethod
    def animal_feature(cls, name, category, noise, food):
        if species == 'Lion':
            return cls(name, category, noise, food)
        elif species == 'Tiger':
            return cls(name, category, noise, food)
        elif species == "Giraffe":
            return cls(name, category, noise, food)
        else:
            return cls(name, category, noise, food)

    def feed_food(self):
        print(self.food)

    def make_noise(self):
        print(self.noise)

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Animal.create_animal_object({},{},{},{}'.format(self.name, self.food, self.category, self.noise)


class Lion(Animal):
    def __init__(self, name, category, noise, food):
        super().__init__(name, category, noise, food)

    def __str__(self):
        return f"{self.name}"


class Tiger(Animal):
    def __init__(self, name, category, noise, food):
        super().__init__(name, category, noise, food)

    def __str__(self):
        return f"{self.name}"


class Giraffe(Animal):
    def __init__(self, name, category, noise, food):
        super().__init__(name, category, noise, food)

    def __str__(self):
        return f"{self.name}"


class Deer(Animal):
    def __init__(self, name, category, noise, food):
        super().__init__(name, category, noise, food)

    def __str__(self):
        return f"{self.name}"


class Zoo:
    def __init__(self):
        self.list = []

    def add_animal(self, newspecies):
        self.list.append(newspecies)

    def get_animal(self):
        return self.list


if __name__ == "__main__":
    list = ['Lions', 'Tiger', 'Giraffe', 'Deer']
    Home = Zoo()

    for species in list:
        count = int(input(f"Enter count of {species}: \n"))
        for i in range(1, count + 1):
            name = input(f"Enter the name of {species} {i}: ")
            category = input(f"Enter the category of {species} {i}: ")
            noise = input(f"Enter Noise made by {species} {i}: ")
            food = input(f"Enter Food Loved by {species} {i}: ")
            print("")
            add = Animal.animal_feature(name, category, noise, food)
            # print(add.__str__)
            Home.add_animal(add)

    zoo_list = Home.get_animal()
    print(repr(zoo_list))

    print(str(zoo_list))
    dict = {}
    food = ""
    voices = ""
    for species in zoo_list:  # [L1,carni,roor,meat,L2]
        dict[str(species)] = species.category
        food = food + f"{str(species)}: {species.food}\n"
        voices = voices + f"{str(species)}: {species.noise}\n"
    print(f"Zoo Animals Dictionary: {dict}")
    print(f"Food:\n{food}")
    print(f'Voices: \n{voices}')

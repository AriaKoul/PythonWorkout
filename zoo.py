class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    
    def __repr__(self):
        return f"{self.color} {self.species}, {self.number_of_legs} legs"

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage():
    def __init(self, id_number): 
        self.id_number = id_number
        self.animals = []
    
    def add_animals(self, *animals):
        for animal in animals:
            self.animals.append(animal)
    
    def __repr__(self):
        output = f"Cage {self.id_number}\n"
        output += '\n'.join('\t' + str(animal) for animal in self.animals)
        return output


class Zoo():
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)

    def __repr__(self):
        return '\n'.join(str(cage) for cage in self.cages)

    def animals_color(self, color):
        return [animal for cage in self.cages
                        for animal in cage.animal
                        if animal.color == color]

    def animals_legs(self, number_of_legs):
        return [animal for cage in self.cages   
                        for animal in cage.animal
                        if animal.number_of_legs == number_of_legs]

    def number_of_legs(self):
        return sum(animal.number_of_legs
                    for cage in self.cages
                    for animal in cage.animals)

wolf = Wolf('gray')
sheep = Sheep('white')
snake = Snake('green')
parrot = Parrot('red')

print(wolf)
print(sheep)
print(snake)
print(parrot)

c1 = Cage()
c1.add_animals(wolf, sheep)

c2 = Cage()
c2.add_animals(snake, parrot)

z = Zoo()
z.add_cages(c1, c2)

print(z)
print(z.animals_color('gray'))
print(z.animals_legs(4))
print(z.number_of_legs())
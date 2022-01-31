class Animal:
    
    def __init__(self, name):
        self.class_name = name
        self.population = []

    def add_new(self, animal_object):
        self.population.append(animal_object)
            
    class Human:
        
        def __init__(self, name):
            self.name = name
            self.number_of_legs = 2
            self.intellect_level = 100
        
        def __repr__(self):
            return f"Человек {self.name}: количество ног = {self.number_of_legs} уровень интеллекта = {self.intellect_level}"
     
    class Pinguin:
        
        def __init__(self, name):
            self.name = name
            self.number_of_legs = 2
            self.intellect_level = 15
            
        def __repr__(self):
            return f"Пингвин {self.name}: количество ног = {self.number_of_legs} уровень интеллекта = {self.intellect_level}"       
        
Human_Oleg = Animal.Human("Олег")
Human_Oleg.intellect_level = 101
print(Human_Oleg)
print(Animal.Human("Вася"))
Earth_animals = Animal("Животные")
Earth_animals.add_new(Human_Oleg)
Earth_animals.add_new(Animal.Human("Пётр"))
Earth_animals.add_new(Animal.Pinguin("Саня"))
print(Earth_animals.__dict__)

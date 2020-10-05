#!/usr/bin/python3
### Class Examples Methods ###

class Dog():
    species = "mammal"
    def __init__(self,breed,name):
        #assign using self.attribute_name
        self.breed = breed
        self.name = name

    #methods ...actions
    def bark(self):
        print("WOOF!")

my_dog = Dog(breed='Lab',name="Bear Bear")

print(type(my_dog))

print(my_dog.breed)
print(my_dog.name)

my_dog.bark()
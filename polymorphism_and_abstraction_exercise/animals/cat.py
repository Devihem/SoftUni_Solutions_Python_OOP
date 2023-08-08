from oop.polymorphism_and_abstraction_exercise.animals.animal import Animal


class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {__class__.__name__}"

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...


class Cat(Animal):
    def make_sound(self):
        return 'Meow'


class Dog(Animal):
    def make_sound(self):
        return 'woof'


class Chicken(Animal):
    def make_sound(self):
        return 'Clock'


class Cow(Animal):
    def make_sound(self):
        return 'Mooo'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Cow(), Chicken()]
animal_sound(animals)

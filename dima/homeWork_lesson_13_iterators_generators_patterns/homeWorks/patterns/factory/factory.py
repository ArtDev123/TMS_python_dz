from .animal import Animal
from .animals.cat import Cat
from .animals.dog import Dog


class AnimalFactory:
    @staticmethod
    def create_animal(name: str, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

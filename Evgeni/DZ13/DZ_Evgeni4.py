from abc import ABC, abstractmethod


class Animal(ABC):
    """Абстрактный класс животного."""

    @abstractmethod
    def speak(self) -> str:
        """Возвращает звук животного."""


class Dog(Animal):
    """Класс собаки."""

    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    """Класс кошки."""

    def speak(self) -> str:
        return "Meow!"


class AnimalFactory:
    """Фабрика животных."""

    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        """Создает животное по его типу."""
        animal_type = animal_type.lower()

        if animal_type == "dog":
            return Dog()

        if animal_type == "cat":
            return Cat()

        raise ValueError(f"Неизвестный тип животного: {animal_type}")


def main() -> None:
    """Запуск программы."""
    animal_type = input("Введите тип животного (dog/cat): ")

    animal = AnimalFactory.create_animal(animal_type)

    print(animal.speak())


if __name__ == "__main__":
    main()
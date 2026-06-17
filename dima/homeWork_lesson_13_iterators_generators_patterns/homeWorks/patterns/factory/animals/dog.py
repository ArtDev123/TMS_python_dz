from dima.homeWork_lesson_13_iterators_generators_patterns.homeWorks.patterns.factory.animal import Animal


class Dog(Animal):
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"Песик {self.name} говорит: 'Все мои братья делают ААуууфф!'"

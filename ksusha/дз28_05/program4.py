class Animal:
    def speak(self) -> str:
        return ""


class Dog(Animal):
    def speak(self) -> str:
        return "Гав"


class Cat(Animal):
    def speak(self) -> str:
        return "Мяу"


class AnimalFactory:
    def create_animal(self, name: str) -> Animal:
        if name == "dog":
            return Dog()
        elif name == "cat":
            return Cat()
        else:
            raise ValueError("Неизвестный тип")


ss = AnimalFactory()
ddd = ss.create_animal("dog")
print(ddd.speak())

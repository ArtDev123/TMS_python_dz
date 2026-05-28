class Soda:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_taste(self) -> None:
        taste = input(f"Введите вкус {self.name} или просто нажмите Enter, \
        если у газировки нет вкуса: ")
        self.taste = taste

    def print_soda_taste(self) -> None:
        if self.taste == "":
            print(f"{self.name} имеет обычный вкусом")
        else:
            print(f"{self.name} имеет вкус: {self.taste}")


sodas: list[Soda] = []
count = int(input("Введите количество газировок, которые хотите добавить: "))


for i in range(count):
    name = input("Введите название газировки: ")
    sodas.append(Soda(name))

for soda in sodas:
    soda.get_taste()

for soda in sodas:
    soda.print_soda_taste()

class Soda:
    def __init__(self, name: str, taste: str | None) -> None:
        self.name = name
        self.taste = taste

    def __str__(self) -> str:
        if self.taste:
            return f"{self.name} имеет вкус: {self.taste}"
        return f"{self.name} имеет обычный вкусом"


sodas: list[Soda] = []
count = int(input("Введите количество газировок, которые хотите добавить: "))

for i in range(count):
    name = input("Введите название газировки: ")
    taste = input("Введите вкус газировки или нажмите пробел:")
    sodas.append(Soda(name, taste))

for soda in sodas:
    print(soda)

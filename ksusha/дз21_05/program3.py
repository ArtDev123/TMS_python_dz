class Car:

    def __init__(self, name: str) -> None:
        self.name = name

    def start_car(self) -> None:
        print(f"Автомобиль {self.name} заведен")

    def stop_car(self) -> None:
        print(f"Автомобиль {self.name} заглушен")

    def get_color(self, color: str) -> None:
        self.color = color

    def get_type(self, type: str) -> None:
        self.type = type

    def get_year(self, year: int) -> None:
        self.year = year


while (True):
    print("Меню\n1. Присвоить автомобилю имя\n"
          "2. Присвоить автомобилю цвет\n"
          "3. Присвоить автомобилю тип\n"
          "4. Присвоить автомобилю год\n"
          "5. Завести автомобиль\n"
          "6. Заглушить автомобиль\n"
          "7. Выход из программы")
    choice = input("Введите номер того, что хотите сделать: ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Неверный ввод, введите целое число от 1 до 7")
        continue

    match choice:
        case "1":
            name = input("Введите модель машины: ")
            object_car = Car(name)

        case "2":
            color = input("Введите цвет машины: ")
            object_car.get_color(color)

        case "3":
            type = input("Введите тип машины: ")
            object_car.get_type(type)

        case "4":
            year = int(input("Введите год машины: "))
            object_car.get_year(year)

        case "5":
            object_car.start_car()

        case "6":
            object_car.stop_car()

        case "7":
            break
    print("\n")

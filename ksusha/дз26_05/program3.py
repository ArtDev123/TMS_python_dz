class Bus:

    i = 0

    def __init__(self, speed: float, max_speed: float, max_places: int):
        self.speed = speed
        self.max_speed = max_speed
        self.max_places = max_places
        self.place = 0
        self.passangers = []
        self.seats = {seat: None for seat in range(1, self.max_places + 1)}
        self.free_seats = True

    def boarding_unboarding(self, count: int) -> None:
        self.place += count
        if count >= 0:
            if self.place > self.max_places:
                self.place = self.max_places
                print("Часть пассажирова не быть добавлена: не хватает мест")
        else:
            if self.place < 0:
                self.place = 0
                print("Ошибка! Вы хотите высадить больше человек,"
                " чем находится в автобусе(вес пассажиры высажены) ")
        print(f"Сейчас в вавтобусе: {self.place} мест занято, осталось свободно:"
              "{self.max_places - self.place}")
        if self.place == self.max_places:
            self.free_seats = False

    def more_less_speed(self, speed: float) -> None:
        self.speed += speed
        if speed > 0:
            if self.speed > self.max_speed:
                self.speed = self.max_speed
                print("Вы пытаетесь добавить слишком много. Установлена максимальная скорость")
        else:
            if self.speed < 0:
                self.speed = 0
                print("Ошибка. Вы пытаетесь опустить скорость ниже нуля. Автобус остановлен.")
        print(f"Сейчас скорость автобуса: {self.speed}")

    def __contains__(self, name: str) -> bool:
        return name in self.passangers

    def __add__(self, name: str) -> 'Bus':
        if name not in self:
            self.passangers.append(name)
            for seat_num, passenger in self.seats.items():
                if passenger == "":
                    self.seats[seat_num] = name
                    break
            print(f"{name} зашел в автобус")
            return self
        else:
            print(f"{name} уже в автобусе")
            return self

    def __isub__(self, name: str) -> 'Bus':
        if name in self:
            self.passangers.remove(name)
            for seat_num, passenger in self.seats.items():
                if passenger == name:
                    self.seats[seat_num] = ""
                    break
            print(f"{name} вышел из автобуса")
            return self
        else:
            print(f"{name} нет в автобусе")
            return self


ss = Bus(89, 90, 23)
ss.boarding_unboarding(5)
ss.boarding_unboarding(-9)
ss.more_less_speed(-90)

ss += "Рита"
ss += "LLlll"
ss += "ffff"
ss += "dddc"
ss += "dddc"

ss -= "ffff"
ss -= "dddc"
ss -= "dddc"

print(ss.passangers)

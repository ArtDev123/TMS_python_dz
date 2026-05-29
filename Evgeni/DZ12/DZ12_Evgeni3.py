from typing import List, Dict, Optional, Union


class Bus:
    def __init__(
        self,
        max_seats: int,
        max_speed: float,
        speed: float = 0.0,
    ) -> None:
        if max_seats <= 0:
            raise ValueError("Максимальное количество мест должно быть положительным")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительной")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if speed > max_speed:
            raise ValueError("Скорость не может превышать максимальную")

        self._max_seats: int = max_seats
        self._max_speed: float = max_speed
        self._speed: float = speed

        self._passengers: List[str] = []
        self._seats: Dict[int, Optional[str]] = {
            i: None for i in range(1, max_seats + 1)
        }

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def max_seats(self) -> int:
        return self._max_seats

    @property
    def max_speed(self) -> float:
        return self._max_speed

    @property
    def passengers(self) -> List[str]:
        """Список фамилий пассажиров"""
        return self._passengers.copy()

    @property
    def has_free_seats(self) -> bool:
        """Флаг наличия свободных мест"""
        return len(self._passengers) < self._max_seats

    @property
    def seats(self) -> Dict[int, Optional[str]]:
        """Словарь мест, ключ — номер места, значение — фамилия пассажира или None"""
        return self._seats.copy()

    def board(self, passenger_names: Union[str, List[str]]) -> None:
        """
        Посадить одного или нескольких пассажиров.
        passenger_names — либо строка (фамилия одного пассажира),
        либо список фамилий.
        """
        if isinstance(passenger_names, str):
            passenger_names = [passenger_names]

        for name in passenger_names:
            if not self.has_free_seats:
                print(f"Нет свободных мест для {name}")
                continue
            if name in self._passengers:
                print(f"Пассажир {name} уже в автобусе")
                continue
            free_seat = next(
                seat for seat, occupant in self._seats.items() if occupant is None
            )
            self._seats[free_seat] = name
            self._passengers.append(name)

    def disembark(self, passenger_names: Union[str, List[str]]) -> None:
        """
        Высадить одного или нескольких пассажиров.
        passenger_names — либо строка (фамилия одного пассажира),
        либо список фамилий.
        """
        if isinstance(passenger_names, str):
            passenger_names = [passenger_names]

        for name in passenger_names:
            if name not in self._passengers:
                print(f"Пассажир {name} не найден в автобусе")
                continue
            self._passengers.remove(name)
            for seat, occupant in self._seats.items():
                if occupant == name:
                    self._seats[seat] = None
                    break

    def increase_speed(self, delta: float) -> None:
        """Увеличить скорость на delta."""
        if delta < 0:
            raise ValueError("delta должен быть неотрицательным")
        self._speed = min(self._speed + delta, self._max_speed)

    def decrease_speed(self, delta: float) -> None:
        """Уменьшить скорость на delta."""
        if delta < 0:
            raise ValueError("delta должен быть неотрицательным")
        self._speed = max(self._speed - delta, 0.0)

    def __contains__(self, passenger_name: object) -> bool:
        """Позволяет писать: if 'Иванов' in bus"""
        if not isinstance(passenger_name, str):
            return False
        return passenger_name in self._passengers

    def __iadd__(self, passenger_name: str) -> Bus:
        """Операция += для посадки пассажира."""
        if not isinstance(passenger_name, str):
            raise TypeError("Можно добавлять только пассажира по фамилии (str)")
        self.board(passenger_name)
        return self

    def __isub__(self, passenger_name: str) -> Bus:
        """Операция -= для высадки пассажира."""
        if not isinstance(passenger_name, str):
            raise TypeError("Можно удалять только пассажира по фамилии (str)")
        self.disembark(passenger_name)
        return self

    def __repr__(self) -> str:
        return (
            f"Bus(speed={self._speed:.1f}, max_speed={self._max_speed:.1f}, "
            f"max_seats={self._max_seats}, passengers={self._passengers})"
        )


if __name__ == "__main__":
    bus = Bus(max_seats=3, max_speed=100, speed=50)
    bus.board("Иванов")
    bus += "Петров"
    print("Пассажиры:", bus.passengers)  #
    print("Свободные места есть?", bus.has_free_seats)
    bus.board(["Сидоров", "Козлов"])
    print("Пассажиры после посадки:", bus.passengers)
    print("Скорость:", bus.speed)
    bus.increase_speed(30)
    print("Скорость после увеличения:", bus.speed)
    bus -= "Петров"
    print("Пассажиры после высадки Петрова:", bus.passengers)
    print("Места:", bus.seats)

from math import pi, pow
from typing import Optional, Tuple


class Sphere:
    def __init__(
        self,
        radius: Optional[float] = None,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
    ) -> None:
        """Инициализация сферы.

        Если radius не задан, по умолчанию 1.0.
        Центр по умолчанию (0,0,0).
        """
        if radius is None:
            radius = 1.0
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius: float = float(radius)
        self._center: Tuple[float, float, float] = (float(x), float(y), float(z))

    def get_volume(self) -> float:
        """Возвращает объем шара, V = 4/3 * pi * r^3."""
        return (4.0 / 3.0) * pi * pow(self._radius, 3)

    def get_square(self) -> float:
        """Возвращает площадь поверхности сферы, S = 4 * pi * r^2."""
        return 4.0 * pi * pow(self._radius, 2)

    def get_radius(self) -> float:
        """Возвращает радиус сферы."""
        return self._radius

    def get_center(self) -> Tuple[float, float, float]:
        """Возвращает координаты центра сферы."""
        return self._center

    def set_radius(self, radius: float) -> None:
        """Задаёт новый радиус сферы."""
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = float(radius)

    def set_center(self, x: float, y: float, z: float) -> None:
        """Задаёт новые координаты центра сферы."""
        self._center = (float(x), float(y), float(z))

    def is_point_inside(self, x: float, y: float, z: float) -> bool:
        """Проверяет, находится ли точка (x, y, z) внутри сферы (включая границу)."""
        cx, cy, cz = self._center
        dist_sq = (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2
        return dist_sq <= self._radius**2


if __name__ == "__main__":
    s1 = Sphere()
    s2 = Sphere(2.5)
    s3 = Sphere(3, 1, 2, 3)

    print("Объем s1:", s1.get_volume())
    print("Площадь s1:", s1.get_square())
    print("Центр s3:", s3.get_center())
    print("Радиус s3:", s3.get_radius())

    s3.set_radius(4.0)
    s3.set_center(0, 0, 0)
    print("Новый радиус s3:", s3.get_radius())
    print("Новый центр s3:", s3.get_center())

    print("Точка (1,1,1) внутри s3?", s3.is_point_inside(1, 1, 1))
    print("Точка (5,0,0) внутри s3?", s3.is_point_inside(5, 0, 0))

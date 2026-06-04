from math import pi


class Sphere:
    def __init__(self, radius: float = 1, x: float = 0,
                 y: float = 0, z: float = 0) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self) -> float:
        v: float  = (4*pi*(self.radius**3))/3
        return v

    def get_square(self) -> float:
        s: float = 4*pi*(self.radius**2)
        return s

    def get_radius(self) -> float:
        return self.radius

    def get_center(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def set_radius(self, new_radius: float) -> None:
        self.radius = new_radius

    def set_center(self, x_new: float, y_new: float, z_new: float) -> None:
        self.x = x_new
        self.y = y_new
        self.z = z_new

    def is_point_inside(self, x_point: float, y_point: float, z_point: float) -> bool:
        dd = (self.x-x_point)**2 + (self.y-y_point)**2 + (self.z-z_point)**2 < self.radius**2
        return dd

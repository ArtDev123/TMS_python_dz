# 1
numbers = [1, 2, 3, 4, 5, 6,]
print(list(map(lambda x: str(x), numbers)))

# 2
numbers_1  = [0, 5, 8, -2, 6, -7, 9]
print(list(filter(lambda x: x >0, numbers_1)))

#3
some_str = ["abcddcba", "yaroslav", "cars", "aaaaaaaa"]
print(list(filter(lambda s: s == s[::-1], some_str)))

# 4 
import time 
from typing import Callable

def time_of_function(func: Callable) -> Callable:
    def wrapper() -> None:
            t_1 = time.time()
            func()
            t_2 = time.time()
            result = t_2 - t_1
            print(f"работа заняла {result}, секунд")
    return wrapper

@time_of_function
def func_one():
    my_list = [ i for i in range (1, 10000)]

@time_of_function    
def func_two():
    my_list = [i for i in range(1, 1000000)]

func_one()
func_two()

# 5
from functools import reduce

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

areas = list(map(lambda room: room["length"] * room["width"], rooms))
print(f"Площадь каждой комнаты", areas)

areas = [24, 24.75, 20, 44.1]
houm_areas = reduce(lambda a,b: a + b, areas)
print(f"Площадь квартиры", houm_areas)



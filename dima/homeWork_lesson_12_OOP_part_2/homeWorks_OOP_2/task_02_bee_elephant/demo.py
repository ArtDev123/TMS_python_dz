from homeWorks_OOP_2.task_02_bee_elephant.bee_elephant import BeeElephant
from homeWorks_OOP_2.task_02_bee_elephant.meal import Meal


# ===== Создание объекта =====
bee_elephant = BeeElephant(_elephant_part=60, _bee_part=40)

print("Начальное состояние:")
print(f"Bee: {bee_elephant.bee_part}")
print(f"Elephant: {bee_elephant.elephant_part}")
print()

# ===== Проверка fly() =====
print("Проверка fly():")
print(bee_elephant.fly())
print()

# ===== Проверка trumpet() =====
print("Проверка trumpet():")
print(bee_elephant.trumpet())
print()

# ===== Проверка eat('nectar') =====
print("Проверка eat('nectar', 20):")

bee_elephant.eat(Meal.NECTAR, 20)

print(f"Bee: {bee_elephant.bee_part}")
print(f"Elephant: {bee_elephant.elephant_part}")
print()

# ===== Проверка eat('grass') =====
print("Проверка eat('grass', 10):")

bee_elephant.eat(Meal.GRASS, 10)

print(f"Bee: {bee_elephant.bee_part}")
print(f"Elephant: {bee_elephant.elephant_part}")
print()

# ===== Проверка ограничения до 100 =====
print("Проверка верхней границы:")

bee_elephant.eat(Meal.NECTAR, 100)

print(f"Bee: {bee_elephant.bee_part}")
print(f"Elephant: {bee_elephant.elephant_part}")
print()

# ===== Проверка ограничения до 0 =====
print("Проверка нижней границы:")

bee_elephant.eat(Meal.GRASS, 100)

print(f"Bee: {bee_elephant.bee_part}")
print(f"Elephant: {bee_elephant.elephant_part}")
print()

# ===== Проверка ошибки =====
print("Проверка неправильной еды:")

try:
    bee_elephant.eat(Meal("pizza"), 10)
except ValueError as error:
    print(f"Ошибка: {error}")

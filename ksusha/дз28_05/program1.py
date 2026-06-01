def generation(number: int):
    if number >= 1:
        yield 0
    if number >= 2:
        yield 1
    curent1 = 0
    curent2 = 1
    number -= 2
    while number > 0:
        curent  = curent1 + curent2
        curent1 = curent2
        curent2 = curent
        yield curent
        number -=1


count = int(input("Введите количество чисел для вывода: "))
result = list(generation(count))
print(", ".join(str(i) for i in result))

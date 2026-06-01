from typing import Any

def sequence(count: int) -> Any:
    i = -1
    while count > 0:
        count -= 1
        i += 1
        i %= 4
        if i == 0:
            i += 1
        yield i


count = int(input("Введите количество чисел для вывода: "))
result = list(sequence(count))
print("-".join(str(i) for i in result))

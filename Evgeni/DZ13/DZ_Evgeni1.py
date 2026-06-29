from collections.abc import Generator


def fibonacci(count: int) -> Generator[int, None, None]:
    """Генератор последовательности Фибоначчи."""
    first = 0
    second = 1

    for _ in range(count):
        yield first
        first, second = second, first + second


def main() -> None:
    """Запуск программы."""
    count = int(input("Введите количество чисел Фибоначчи: "))

    if count <= 0:
        print("Количество должно быть больше нуля.")
        return

    for number in fibonacci(count):
        print(number)


if __name__ == "__main__":
    main()
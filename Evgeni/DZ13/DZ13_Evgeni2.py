from collections.abc import Generator


def cycle_numbers() -> Generator[int, None, None]:
    """Генератор бесконечной циклической последовательности."""
    while True:
        yield 1
        yield 2
        yield 3


def main() -> None:
    """Запуск программы."""
    count = int(input("Введите количество чисел: "))

    if count <= 0:
        print("Количество должно быть больше нуля.")
        return

    generator = cycle_numbers()

    for _ in range(count):
        print(next(generator))


if __name__ == "__main__":
    main()

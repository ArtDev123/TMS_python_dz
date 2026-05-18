import json
import csv
from typing import List, Dict, Any


def load_json(filename: str) -> List[Dict[str, Any]]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Ожидался список словарей в JSON")
    return data


def save_json(data: List[Dict[str, Any]], filename: str) -> None:
    """Сохранение данных в JSON файл."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def json_to_csv(json_data: List[Dict[str, Any]], csv_filename: str) -> None:
    """Преобразование JSON данных в CSV и сохранение."""
    if not json_data:
        print("Нет данных для записи.")
        return

    headers = list(json_data[0].keys())
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for person in json_data:
            row: List[str] = []
            for key in headers:
                value = person[key]
                # Упрощаем логику!
                if isinstance(value, list):
                    # Все элементы привести к строке, если не строка
                    value_str = ", ".join(str(v) for v in value)
                elif isinstance(value, bool):
                    value_str = "true" if value else "false"
                else:
                    value_str = str(value)
                row.append(value_str)
            writer.writerow(row)


def add_employee_to_json(json_filename: str) -> None:
    """Добавление нового сотрудника в JSON-файл."""
    data: List[Dict[str, Any]] = load_json(json_filename)

    name: str = input("Имя и фамилия: ")
    birthday: str = input("День рождения (ДД.ММ.ГГГГ): ")
    height: float = float(input("Рост: "))
    weight: float = float(input("Вес: "))
    car_input: str = input("Есть ли у сотрудника машина? (да/нет): ").lower()
    car: bool = car_input == "да"
    languages_input: str = input("Языки программирования (через запятую): ")
    languages: List[str] = [lang.strip() for lang in languages_input.split(",")]

    new_employee: Dict[str, Any] = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages,
    }

    data.append(new_employee)
    save_json(data, json_filename)
    print("Сотрудник добавлен в JSON.")


def add_employee_to_csv(csv_filename: str) -> None:
    """Добавление нового сотрудника в CSV-файл."""
    name = input("Имя и фамилия: ")
    birthday = input("День рождения (ДД.ММ.ГГГГ): ")
    height = float(input("Рост: "))
    weight = float(input("Вес: "))
    car_input = input("Есть ли у сотрудника машина? (да/нет): ").lower()
    car = car_input == "да"
    languages_input = input("Языки программирования (через запятую): ")
    languages = [lang.strip() for lang in languages_input.split(",")]

    row = [
        name,
        birthday,
        height,
        weight,
        "true" if car else "false",
        ", ".join(languages),
    ]

    with open(csv_filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)
    print("Сотрудник добавлен в CSV.")


def find_employee_by_name(json_filename: str) -> None:
    """Поиск сотрудника по имени."""
    data = load_json(json_filename)
    name_to_find = input("Введите имя для поиска: ").strip()

    found = False
    for person in data:
        if person["name"].lower() == name_to_find.lower():
            print(person)
            found = True
            break
    if not found:
        print("Сотрудник с таким именем не найден.")


def filter_by_language(json_filename: str) -> None:
    """Фильтрация сотрудников по языку программирования."""
    data = load_json(json_filename)
    language = input("Введите язык программирования: ").strip().lower()

    results = [
        person
        for person in data
        if any(lang.lower() == language for lang in person.get("languages", []))
    ]

    if results:
        for person in results:
            print(person)
    else:
        print("Нет сотрудников с таким языком программирования.")


def filter_by_year(json_filename: str) -> None:
    """Вывод среднего роста сотрудников, родившихся до заданного года."""
    data = load_json(json_filename)
    try:
        year_input = int(input("Введите год рождения: "))
    except ValueError:
        print("Некорректный ввод года.")
        return

    heights: List[float] = []
    for person in data:
        birthday_str = person.get("birthday", "")
        try:
            day, month, year = map(int, birthday_str.split("."))
        except (ValueError, AttributeError):
            continue
        if year < year_input:
            heights.append(person.get("height", 0.0))

    if heights:
        average_height = sum(heights) / len(heights)
        print(
            f"Средний рост сотрудников, родившихся раньше {year_input}: {average_height:.2f} см"
        )
    else:
        print("Нет сотрудников, родившихся до этого года.")


def main() -> None:
    filename_json = "employees.json"
    filename_csv = "employees.csv"

    try:
        load_json(filename_json)
    except FileNotFoundError:
        print("Создаем новый JSON-файл с исходными данными.")
        data = [
            {
                "name": "John Smith",
                "birthday": "02.10.1990",
                "height": 175,
                "weight": 76.5,
                "car": True,
                "languages": ["C++", "Python"],
            },
            {
                "name": "Alexey Alexeev",
                "birthday": "05.06.1986",
                "height": 197,
                "weight": 101.2,
                "car": False,
                "languages": ["Pascal", "Delphi"],
            },
            {
                "name": "Maria Ivanova",
                "birthday": "28.08.1998",
                "height": 165,
                "weight": 56.1,
                "car": True,
                "languages": ["C#", "C++", "C"],
            },
        ]
        save_json(data, filename_json)

    while True:
        print("\nМеню:")
        print("1. Прочитать JSON и преобразовать в CSV")
        print("2. Добавить нового сотрудника в JSON")
        print("3. Добавить нового сотрудника в CSV")
        print("4. Поиск сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Средний рост сотрудников, родившихся до года")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            json_data = load_json(filename_json)
            json_to_csv(json_data, filename_csv)
            print("Данные успешно сохранены в CSV.")
        elif choice == "2":
            add_employee_to_json(filename_json)
        elif choice == "3":
            add_employee_to_csv(filename_csv)  # <--- Исправлено
        elif choice == "4":
            find_employee_by_name(filename_json)
        elif choice == "5":
            filter_by_language(filename_json)
        elif choice == "6":
            filter_by_year(filename_json)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()

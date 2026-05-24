import json

from typing import cast


def filter_by_language(json_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as json_file:
        employees: list[dict[str, object]] = json.load(json_file)

    search_user_by_lang = input("Введите язык программирования: ").strip().lower()

    filtered_employees: list[dict[str, object]] = []

    for employee in employees:

        employee_languages = cast(list[str], employee["languages"])

        employee_langs = [lang.lower() for lang in employee_languages]

        if search_user_by_lang in employee_langs:

            filtered_employees.append(employee)

    if not filtered_employees:

        print("Сотрудники не найдены")

    else:

        for employee in filtered_employees:

            languages = ", ".join(cast(list[str], employee["languages"]))

            print(f"{employee['name']} - {languages}")


def average_height_by_year(json_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as json_file:
        employees = json.load(json_file)

    while True:
        try:
            search_year = int(input("Год рождения: "))
            break
        except ValueError:
            print("Ошибка: Неверно введены значения!")

    heights: list[int] = []

    for employee in employees:

        birthday = employee["birthday"]

        day, month, birth_year = birthday.split(".")

        birth_year = int(birth_year)

        if birth_year < search_year:
            heights.append(employee["height"])

    if not heights:
        print("Подходящих сотрудников нет")
    else:
        average = sum(heights) / len(heights)
        print(
            f"Средний рост сотрудников, родившихся до {search_year} года: "
            f"{average:.2f} cm"
        )

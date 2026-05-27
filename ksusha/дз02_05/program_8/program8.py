import os
import json
import csv


now_folder = os.getcwd()
json_path = os.path.join(now_folder, "ksusha", "дз02_05", "program_8", "employees.json")
csv_path = os.path.join(now_folder, "ksusha", "дз02_05", "program_8", "res.csv")


def transformation(json_path: str, csv_path: str) -> None:
    with open(json_path, "r", encoding="utf-8") as empl:
        data = json.load(empl)
        with open(csv_path, "w+", encoding="utf-8") as res:
            file_writer = csv.writer(res, delimiter=",")
            headers = data[0].keys()
            file_writer.writerow(headers)
            for item in data:
                file_writer.writerow(item.values())


def new_json(json_path: str) -> None:
    with open(json_path, "r", encoding="utf-8") as empl:
        data = json.load(empl)
        headers = data[0].keys()
    with open(json_path, "a", encoding="utf-8") as empl:
        new_person: dict[str, str | list[str]] = {}
        for item in headers:
            if item == "languages":
                try:
                    count = int(input("Введите количество языков программирования: "))
                except ValueError:
                    print("Ошибка: введите число")
                    return
                languages = []
                for i in range(count):
                    language = input("Введите язык программирования: ")
                    languages.append(language)
                new_person[item] = languages
            else:
                if item != "languages":
                    new_person[item] = input(f"Введите {item}: ")
        data.append(new_person)
    with open(json_path, "w", encoding="utf-8") as empl:
        json.dump(data, empl, indent=4)


def new_csv(csv_path: str) -> None:
    with open(csv_path, "r", encoding="utf-8") as empl:
        reader = csv.DictReader(empl, delimiter=",")
        headers = reader.fieldnames
        if headers is None:
            print("CSV файл не содержит заголовков")
            return
    with open(csv_path, "a", encoding="utf-8", newline="") as empl:
        writer = csv.DictWriter(empl, fieldnames=headers, delimiter=",")
        data: dict[str, str] = {}
        for i in headers:
            if i == "languages":
                n = int(input("Введите количество языков"))
                languages = []
                for k in range(n):
                    language = input("Введите язык программирования: ")
                    languages.append(language)
                data[i] = ", ".join(languages)
            else:
                data[i] = input(f"Введите {i}")
        writer.writerow(data)


def information(json_path: str) -> None:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    emploer = input("Введите имя сотрудника: ")
    found = False
    for i in data:
        if i["name"] == emploer:
            print(i)
            found = True
    if not found:
        print(f"Сотрудник с именем {emploer} не найден")


def language_from_user(json_path: str) -> None:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    language = input("Введите язык для фильтрации: ")
    found = False
    for i in data:
        if language in i["languages"]:
            print(i["name"])
            found = True
    if not found:
        print(f"Нет сотрудников, знающих язык {language}")


def middle_height(json_path: str) -> None:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    year = input("Введите год рождения: ")
    count = 0
    sum_height = 0
    for i in data:
        if year > i["birthday"][-4:]:
            count += 1
            sum_height += i["height"]
    if count == 0:
        print(f"Нет сотрудников, родившихся ранее {year} года")
    else:
        print(f"Средний рост = {sum_height / count}")


# transformation(json_path)
# new_json(json_path)
# new_csv(csv_path)
# json_to_csv(json_path, csv_path)
# information(json_path)
# language_from_user(json_path)
# middle_height(json_path)

while True:
    print(
        "\nМеню\n1. Считать данные из исходного JSON-файла и преобразовать их в формат CSV"
        "\n3. Добавить информацию о новом сотруднике в JSON-файл\n"
        "4. Добавить информацию о новом сотруднике в CSV-файл\n5. Вывести информацию об "
        "одном сотруднике по имени\n"
        "6. Вывести список всех сотрудников, кто владеет заданным языком программирования"
        "(язык вводит"
        "ся с клавиатуры)\n"
        "7. Вывести средний рост сотрудников, которые "
        "родились ранее заданного года(год вводится с кла"
        "виатуры)\n"
        "8. Завершение программы"
    )
    choice = input("Введите номер того, что хотите сделать: ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Неверный ввод, введите число от 1 до 7")
        continue

    match choice:
        case "1":
            transformation(json_path, csv_path)

        case "2":
            new_json(json_path)

        case "3":
            new_csv(csv_path)

        case "4":
            information(json_path)

        case "5":
            language_from_user(json_path)

        case "6":
            middle_height(json_path)

        case "7":
            break

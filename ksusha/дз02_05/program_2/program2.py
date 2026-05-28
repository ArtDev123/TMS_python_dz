import re

text = input("Введите текст")
fio = input("Введите ФИО")
fio = fio.title()
replacement = r"[А-ЯЁ][а-яё]+(-[А-ЯЁ][а-яё]+)?\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+"

text = re.sub(replacement, fio, text, count=1)

print(text)

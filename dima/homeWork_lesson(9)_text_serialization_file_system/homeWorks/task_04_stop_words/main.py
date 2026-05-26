import os
import re

current_folder = os.getcwd()

text_file_name = input("Введите название файла: ")

text_file_path = os.path.join(current_folder, text_file_name)
stop_words_path = os.path.join(current_folder, "stop_words.txt")
result_path = os.path.join(current_folder, "result.txt")

with open(stop_words_path, "r", encoding="utf-8") as file:
    stop_words = file.read().split()

with open(text_file_path, "r", encoding="utf-8") as file:
    text = file.read()

pattern = re.compile("|".join(map(re.escape, stop_words)), re.IGNORECASE)
result = pattern.sub(lambda match: "*" * len(match.group()), text)

with open(result_path, "w", encoding="utf-8") as file:
    file.write(result)

print(result)

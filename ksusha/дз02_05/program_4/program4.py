import os
import re

now_folder = os.getcwd()
stop_file = os.path.join(now_folder, "дз02_05", "program_4", "stop_words.txt")
text_file = os.path.join(now_folder, "дз02_05", "program_4", "text_for_program4.txt")

with open(stop_file, "r", encoding="utf-8") as stop:
    stop_words = stop.read()
    stop_words = stop_words.split()
    print(stop_words)

with open(text_file, "r", encoding="utf-8") as text:
    text = text.read()
    print(text)

with open(
    os.path.join(now_folder, "дз02_05", "program_4", "result.txt"),
    "w+",
    encoding="utf-8",
) as res:
    for word in stop_words:
        replacment = "*" * len(word)
        text = re.sub(word, replacment, text, flags=re.IGNORECASE)
    res.write(text)

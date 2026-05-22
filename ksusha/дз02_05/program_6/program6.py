import os
import re

now_folder = os.getcwd()
text_path = os.path.join(now_folder, "дз02_05", "program_6", "text_for_program6.txt")
with open(text_path, "r", encoding="utf-8") as f:
    text = f.read()

numbers = re.findall(r"\d+", text)
total = sum(int(n) for n in numbers)
print(total)

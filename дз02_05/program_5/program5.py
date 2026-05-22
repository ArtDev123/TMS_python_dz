import os

now_file = os.getcwd()
fil = os.path.join(now_file, "дз02_05", "program_5", "children")
with open(fil, "r", encoding="utf-8") as f:
    text = f.readlines()

print("Учащиеся, оценка которых меньше 3")

for item in text:
    name, last_name, grade = item.split()
    grade = int(grade)
    if grade < 3:
        print(name, last_name)

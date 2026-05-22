import os
import sys

now_folder = os.getcwd()
os_name = os.name
sys_name = sys.platform
print(f"Имя ос: {os_name} или {sys_name}")
print(f"Вы находитесь  в папке: {now_folder}")

expansions = []
conter_new = {}

items = os.path.join(now_folder, "дз12_05", "program_1")
files_items = os.listdir(items)

for item in files_items:
    expansion = "." + item.split(".")[-1]
    expansions.append(expansion)

expansions = set(expansions)
print(expansions)

for item in expansions:
    if not os.path.exists(os.path.join(items, item)):
        os.makedirs(os.path.join(items, item))

for item in files_items:
    full_path = os.path.join(items, item)
    if not os.path.isfile(full_path):
        continue
    if item == "program1.py":
        continue

    name, ext = os.path.splitext(item)
    if not ext:
        continue
    name, ext = os.path.splitext(item)
    os.replace(os.path.join(items, item), os.path.join(items, ext, item))
    conter_new[ext] = conter_new.get(ext, 0) + 1


for item in expansions:
    new_path = os.path.join(items, item)
    count = 0
    for n in os.listdir(new_path):
        if os.path.isfile(os.path.join(new_path, n)):
            count += 1
    print(f"Файлов в папке {item}: {count}")

for ext, cout in conter_new.items():
    print(f"В папку {ext} перемещен {cout} файл")


before = os.path.join(items, ".txt", "ff.txt")
after = os.path.join(items, ".txt", "rename_.txt")
os.rename(before, after)

print(f"{os.path.basename(before)} был переименован в {os.path.basename(after)}")

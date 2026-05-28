import os
from collections import Counter

now_file = os.getcwd()
fil = os.path.join(now_file, "ksusha", "дз02_05", "program_3", "text_for_program3")
with open(fil, "r", encoding="utf-8") as f:
    text = f.readlines()

with open(
    os.path.join(now_file, "ksusha", "дз02_05", "program_3", "result"), "w", encoding="utf-8"
) as file_res:
    count_lines = 1
    for item in text:
        words = item.lower().split()
        counter = Counter(words)
        word, count = counter.most_common(1)[0]
        print(f"Слово '{word}' повторяется {count} раза в {count_lines} строке")
        file_res.write(
            f"Слово '{word}' повторяется {count} раза в {count_lines} строке\n"
        )
        count_lines = count_lines + 1

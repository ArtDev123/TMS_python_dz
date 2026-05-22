import os, re

now_folder = os.getcwd()
text_path = os.path.join(now_folder, "дз02_05", "program_7", "text.txt")
with open(text_path, "r", encoding="utf-8") as f:
    text = f.readlines()

count = 1
for item in text:
    s = item.lower()
    n_s = len(s)
    alphabet = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    n_alphabet = len(alphabet)
    s2 = []
    shift = count
    for i in range(n_s):
        found = False
        for k in range(n_alphabet):
            if s[i] == alphabet[k]:
                found = True
                x = (k + shift) % n_alphabet
                s2.append(alphabet[x])
                break
        if not found:
            s2.append(s[i])
    print("".join(s2), end="")
    count += 1

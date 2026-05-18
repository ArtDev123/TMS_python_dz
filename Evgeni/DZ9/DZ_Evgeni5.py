import re

filename = "input.txt"

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

numbers = re.findall(r"\d+", content)

total_sum = sum(int(num) for num in numbers)

print(total_sum)

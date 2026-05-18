import re
from collections import Counter

input_filename = "input.txt"

output_filename = "output.txt"

with open(input_filename, "r", encoding="utf-8") as infile, open(
    output_filename, "w", encoding="utf-8"
) as outfile:
    for line in infile:

        line = line.strip().lower()

        words = re.findall(r"\b\w+\b", line)
        if words:

            counter = Counter(words)

            most_common_word, count = counter.most_common(1)[0]

            outfile.write(f"{most_common_word} {count}\n")
        else:

            outfile.write("\n")

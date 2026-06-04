import re
from typing import List, Match

filename = input("Введите название файла: ")


with open("stop_words.txt", "r", encoding="utf-8") as f:
    stop_words = f.read().split()


stop_words = [word.lower() for word in stop_words]


with open(filename, "r", encoding="utf-8") as f:
    content = f.read()


def replace_forbidden_words(text: str, forbidden_list: List[str]) -> str:
    def replacer(match: Match[str]) -> str:
        word = match.group()

        core_word = re.sub(r"^\W+|\W+$", "", word)
        if core_word.lower() in forbidden_list:
            return "*" * len(word)
        return word

    pattern = r"\b\W*\w+\W*\b"
    return re.sub(pattern, replacer, text)


result = replace_forbidden_words(content, stop_words)


print(result)

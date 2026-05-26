def caesar_cipher(text: str, shift: int) -> str:

    result = ""
    for char in text:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result


filename = "Input.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    line = line.rstrip("\n")
    shift = i
    encrypted_line = caesar_cipher(line, shift)
    print(encrypted_line)

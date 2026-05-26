filename = "students.txt"

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        surname, name = parts[0], parts[1]
        grade_str = parts[2]

        try:
            grade = float(grade_str)
        except ValueError:
            continue

        if grade < 3:
            print(f"{surname} {name} - оценка: {grade}")

import os


current_directory = os.getcwd()
students_file_path = os.path.join(current_directory, 'students.txt')

with open(students_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        students = line.split()

        if len(students) != 3:
            continue

        student_surname, student_name, student_marks = students

        try:
            grade = int(student_marks)
        except ValueError:
            continue

        if grade < 3:
            print(f"{student_surname} {student_name} - '{student_marks}'")

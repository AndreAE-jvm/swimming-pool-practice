def average_grade(filename):
    grades = {}
    with open(filename, "r", encoding="utf-8") as f:
        next(f)  # пропускаем заголовок
        for line in f:
            name, grade = line.strip().split(",")
            grade = int(grade)
            if name not in grades:
                grades[name] = []
            grades[name].append(grade)
    result = {}
    for name, marks in grades.items():
        result[name] = sum(marks) / len(marks)
    return result

print(average_grade("students.csv"))  # {'Alice': 4.5, 'Bob': 4.0}
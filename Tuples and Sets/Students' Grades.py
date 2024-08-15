students_count = int(input())
students_dict = {}

for _ in range(students_count):
    name, grade = input().split()
    grade = float(grade)

    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

for name, grades in students_dict.items():
    print(f"{name} -> {' '.join([f'{x:.2f}' for x in grades])} (avg: {sum(grades) / len(grades):.2f})")

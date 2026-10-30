# Задача 11: Студенти с оценка над 4.50 и среден успех на всички

students = {
    "Иван Петров": 5.75,
    "Мария Георгиева": 4.20,
    "Георги Иванов": 4.50,
    "Елена Димитрова": 6.00,
    "Петър Николов": 3.80,
}

print("Студенти с оценка над 4.50:")
for name, grade in students.items():
    if grade > 4.50:
        print(f"  {name} – {grade:.2f}")

average = sum(students.values()) / len(students)
print(f"Среден успех на всички студенти: {average:.2f}")

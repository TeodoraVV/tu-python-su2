# Задача 7: Всички индекси, на които се среща числото x в списък

numbers = list(map(float, input("Въведете числа, разделени с интервал: ").split()))
x = float(input("Въведете търсеното число x: "))

indices = [i for i, value in enumerate(numbers) if value == x]

if indices:
    print(f"Числото {x:g} се среща на индекси: {indices}")
else:
    print(f"Числото {x:g} не се среща в списъка.")

# Задача 9: Сума, средна аритметична стойност и кортеж с четните числа

numbers = tuple(map(int, input("Въведете цели числа, разделени с интервал: ").split()))

if not numbers:
    print("Кортежът е празен.")
else:
    total = sum(numbers)
    average = total / len(numbers)
    evens = tuple(x for x in numbers if x % 2 == 0)

    print("Кортеж:", numbers)
    print("Сума:", total)
    print(f"Средна аритметична стойност: {average:.2f}")
    print("Четни числа:", evens)

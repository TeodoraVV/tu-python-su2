# Задача 6: Премахване на повторенията от списък с 10 случайни числа,
# като се запазва редът на първата поява

import random

numbers = [random.randint(1, 10) for _ in range(10)]
print("Първоначален списък:", numbers)

unique = []
for x in numbers:
    if x not in unique:
        unique.append(x)

print("Без повторения:     ", unique)

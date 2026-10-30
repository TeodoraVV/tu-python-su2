# Задача 2: Списък от случайни числа; между всеки два съседни елемента
# се вмъква нов елемент, равен на тяхната сума

import random

N = 6  # брой на случайните числа
numbers = [random.randint(1, 50) for _ in range(N)]
print("Първоначален списък:", numbers)

result = []
for i in range(len(numbers)):
    result.append(numbers[i])
    if i < len(numbers) - 1:              # след последния елемент няма съсед
        result.append(numbers[i] + numbers[i + 1])

print("Резултат:           ", result)

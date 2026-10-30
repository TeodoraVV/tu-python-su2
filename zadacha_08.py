# Задача 8: Общи елементи на два списъка, без повторения

import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print("Първи списък: ", list1)
print("Втори списък: ", list2)
print("Общи елементи:", common)

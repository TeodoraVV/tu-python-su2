# Задача 14: Множество от уникалните елементи на списък; брой различни числа
# и числата, които се срещат повече от веднъж

numbers = list(map(int, input("Въведете числа, разделени с интервал: ").split()))

unique = set(numbers)
repeated = {x for x in unique if numbers.count(x) > 1}

print("Уникални елементи:", unique)
print("Брой различни числа:", len(unique))
if repeated:
    print("Срещат се повече от веднъж:", sorted(repeated))
else:
    print("Няма числа, които се срещат повече от веднъж.")

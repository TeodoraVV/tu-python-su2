# Задача 4: Списък с числата от 1 до n и речник {число: число в обратен ред}

n = int(input("Въведете положително цяло число n: "))
while n <= 0:
    n = int(input("Числото трябва да е положително. Въведете отново: "))

numbers = list(range(1, n + 1))
result = dict(zip(numbers, numbers[::-1]))

print("Списък:", numbers)
print("Речник:", result)

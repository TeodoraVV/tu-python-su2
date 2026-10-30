# Задача 15: Речник с ключове от 1 до n и стойности (квадрат, куб) на ключа

n = int(input("Въведете n: "))

result = {k: (k ** 2, k ** 3) for k in range(1, n + 1)}

print(result)

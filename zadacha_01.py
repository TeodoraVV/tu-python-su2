# Задача 1: Два кортежа от цифрите на число – в прав и в обратен ред

n = int(input("Въведете цяло число: "))


digits = tuple(int(ch) for ch in str(abs(n)))
reversed_digits = digits[::-1]

print("Цифри в прав ред:   ", digits)
print("Цифри в обратен ред:", reversed_digits)

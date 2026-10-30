# Задача 5: Най-малък и най-голям елемент на списък и броят на срещанията им

numbers = list(map(int, input("Въведете цели числа, разделени с интервал: ").split()))

if not numbers:
    print("Списъкът е празен.")
else:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"Най-малък елемент: {smallest}, среща се {numbers.count(smallest)} път(и)")
    print(f"Най-голям елемент: {largest}, среща се {numbers.count(largest)} път(и)")

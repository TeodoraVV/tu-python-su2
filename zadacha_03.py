# Задача 3: Речник с броя на срещанията на всеки символ в текст

text = input("Въведете текст: ")

counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

print(counts)

# Задача 10: Речник с броя на срещанията на всяка дума в изречение
# (без разлика между главни и малки букви)

import string

sentence = input("Въведете изречение: ")

counts = {}
for word in sentence.lower().split():
    word = word.strip(string.punctuation + "„“…–")   # махаме препинателните знаци
    if word:
        counts[word] = counts.get(word, 0) + 1

print(counts)

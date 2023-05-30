# Задача 3. Даны две строки. 
# Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
substring = input('Введите строку: ')
phrase = input('Bведите фразу: ')
count = []
simbols = []

len_substr = len(substring)
length_phrase = len(phrase)

for i in range(length_substr):
    num = 0
simbols.append(substring[i])
for j in range (length_phrase):
    if substring[i] == phrase[j]:
        num += 1
count.append(num)
print(f'{simbols[i]} - {count[i]}', end=', ')
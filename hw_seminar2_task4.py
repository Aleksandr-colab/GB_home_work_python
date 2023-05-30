# Задача 4. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
n = int(input('Введите число: '))
length = n * 2 + 1
array = []
for i in range(length):
    array.append(-n + i)
print(array)
shift = int(input('Введите число, на которое надо сдвинуть вправо : '))
for j in range(shift):
    temp = array[-1]
    for k in range(length - 1):
        array[-1-k] = array[-2-k]
    array[0] = temp
print(array)
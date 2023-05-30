import random
# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
numbers = [random.randint(1, 10) for i in range (10)]
print(numbers)

result = [0]
    
while len(result) < 2:
    index = random.randint(0, 9)  # случайный индекс, с которого начнем возрастающую последовательность
    result = [numbers[index]]
    for i in numbers[index:]:
        if i > result[len(result)-1]:
            result.append(i)    
        
print(result) 
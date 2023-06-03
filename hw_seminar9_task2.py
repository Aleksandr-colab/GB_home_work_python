# Задача 2. Создайте двумерный массив, 
# размером 5х5. Определите, есть ли в нём одинаковые строки.
import numpy as np
size = (5, 5)
numbers = np.random.randint(0, 2, size)
print(numbers)
    
result = numbers.any(axis=1)
print(result)
result = ~result
print(result)

if True in result:
    print('В масиве есть одинаковые строки')
else:
    print('В масиве нет одинаковых строк')

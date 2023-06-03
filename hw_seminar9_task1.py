# Задача 1. Дан список элементов. Используя библиотеку NumPy, 
# подсчитайте количество уникальных элементов в нём.
import numpy as np
list = (10)
numbers = np.random.randint(1, 10, list)
print(numbers)

uniq_list, uniq_counts = np.unique(numbers, return_counts=True)
print(f'уникальные элементы {uniq_list}')
print(f'их количество       {uniq_counts}')
index_max = np.argmax(uniq_counts)
print(index_max)
print(f'Элемент {uniq_list[index_max]} встречает {uniq_counts[index_max]}')


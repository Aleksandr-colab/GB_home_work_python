# Задача 3. Создайте двумерный массив случайного размера. 
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np
size = (10)
arr1 = np.random.randint(100, size=(5,5))    
print(arr1)
index_min = np.argmin(arr1)
index_max = np.argmax(arr1)
print(f"Минимальный индекс: {index_min}") 
print(f"Максимальный индекс: {index_max}") 
print('Главная диагональ:', np.diag(arr1,k=0))
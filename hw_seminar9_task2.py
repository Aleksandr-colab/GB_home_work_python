# Задача 2. Создайте двумерный массив, 
# размером 5х5. Определите, есть ли в нём одинаковые строки.
import numpy as np
A=np.array([[0, 1, 0, 0, 0,],
            [0, 0, 0, 1, 0,],
            [0, 1, 0, 0, 0,],
            [1, 0, 1, 0, 1,],
            [1, 1, 1, 0, 0,],
            [0, 1, 0, 1, 0,]])
for i in range(len(A)): 
    for j in range(i+1,len(A)): 
        if np.array_equal(A[i],A[j]): 
            if np.array_equal(A[:,i],A[:,j]): 
                print(f'Одинаковые строки {i, j}'),
        else: pass            
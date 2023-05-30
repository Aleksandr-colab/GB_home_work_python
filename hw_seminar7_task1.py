# Задача 1. Создайте пользовательский аналог метода map().
def our_map(func, matrix):
    return (func(el) for el in matrix)

def power(x):
    return x / 2

nums = [1, 2, 3, 12, 22, 16, 20]

print (list(our_map(power, nums)))
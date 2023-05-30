import random
# Задача 1. Задайте список случайных чисел от 1 до 10, 
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8


numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)
numbers = list(filter(lambda x: not (x < 5), numbers))
print(numbers)
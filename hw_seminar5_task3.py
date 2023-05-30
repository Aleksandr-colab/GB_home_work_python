import random
# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
print("Количество повторяющихся элементов ", len(list(filter(lambda x: numbers.count(x) > 1, numbers))))
    # res = list(map(lambda x: numbers.remove(x) , list(filter(lambda x: numbers.count(x) > 1,  numbers))))
result = []
for i in numbers:
    if numbers.count(i) > 1:
            numbers.remove(i)
print("Список уникальных элементов:")
print(numbers)
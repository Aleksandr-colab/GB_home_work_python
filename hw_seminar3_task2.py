# Задача 2. В списке находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
fruits = ["апельсин", "банан", "ананас", "яблоко", "арбуз", "гранат", "груша", "гуава", "мандарин", "манго"]


letter = input('Введите первую букву названия фрукта: ')
    
for fruit in fruits:
    if fruit.startswith(letter):
        print(fruit)
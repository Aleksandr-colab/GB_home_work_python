# Задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение
The_days_of_the_week = int(input('Введите день недели: '))
if The_days_of_the_week == 1:
    print('Это понедельник')
elif The_days_of_the_week == 2:
    print('Это вторник')
elif The_days_of_the_week == 3:
    print('Это среда')
elif The_days_of_the_week == 4:
    print('Это четверг')
elif The_days_of_the_week == 5:
    print('Это пятница')
elif The_days_of_the_week == 6:
    print('Это суббота')
elif The_days_of_the_week == 7:
    print('Это воскресенье')
else:
    print('Такого дня недели нет!!!')
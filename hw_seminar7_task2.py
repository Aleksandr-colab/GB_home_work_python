# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
def start_repeater(count):
    def repeater(func):
        def repeat():
            for num in range(count):
                print(f'Вызов функции №{num+1}')
                func()
                print()
        return repeat
    return repeater
@start_repeater(int(input('Введите кличество повторений ')))
def hello():
    print('Привет')
hello()
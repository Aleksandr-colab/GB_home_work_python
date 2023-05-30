# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import os

os.system('cls')

number_N = int(input('Введите количество элементов списка: '))
nums = []
value = 1
for i in range(1, number_N + 1):
    nums.append(value)
    value *= i + 1
print(nums)
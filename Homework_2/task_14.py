# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input('Введите число: '))
degree = 1
while degree < num:
    print(degree, end=' ')
    degree = degree * 2
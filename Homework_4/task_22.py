# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

qu_1 = int(input("Введите количество элементов первого множества: "))
set_1 = set()
for el in range(qu_1):
    element = int(input("Введите элементы певрого множества: "))
    set_1.add(element)

qu_2 = int(input("Введите количество элементов второго множества: "))
set_2 = set()
for el in range(qu_2):
    element = int(input("Введите элементы второго множества: "))
    set_2.add(element)

set_3 = (sorted(set_1 & set_2))
print(*set_3)
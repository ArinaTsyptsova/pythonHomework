qu_bush = int(input("Введите количество кустов: "))
qu_ber = []
for el in range(qu_bush):
    berry = int(input(f"Введите количество ягод на {el + 1}-ом кусте: "))
    qu_ber.append(berry)

sum_bush = []
for el in range(len(qu_ber)):
    sum_bush.append(qu_ber[el - 2] + qu_ber[el - 1] + qu_ber[el])
print(max(sum_bush))

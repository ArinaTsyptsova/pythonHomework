# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

num_of_coins = int(input('Введите количество монеток: '))
state = []

for i in range(num_of_coins):
    state.append(randint(0, 1))
state_tails, state_eagle = 0, 0
for i in state:
    if i == 0:
        state_tails += 1
    else:
        state_eagle += 1
print(state)
if state_tails > state_eagle:
    print(state_eagle)
else:
    print(state_tails)
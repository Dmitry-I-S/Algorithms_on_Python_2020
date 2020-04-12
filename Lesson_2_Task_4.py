# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите натуральное число: '))
summ = 1
i = 1

while i < n:
    if i % 2 != 0:
        summ -= (1 / 2 ** i)
    else:
        summ += (1 / 2 ** i)
    i += 1

print(summ)

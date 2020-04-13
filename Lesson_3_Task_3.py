# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

a = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(a)

max = a[1]          # сохраняем объекты списка в переменной для сравнения
min = a[1]
max_index = 0       # сохраняем индексы объектов
min_index = 0

for i in range(SIZE):
    if a[i] > max:
        max = a[i]
        max_index = i
    if a[i] < min:
        min = a[i]
        min_index = i

a[max_index], a[min_index] = a[min_index], a[max_index]
print('В массиве a изменены местами минимальный и максимальный элементы:')
print(a)

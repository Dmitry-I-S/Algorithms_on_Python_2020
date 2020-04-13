# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

a = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(a)


for i in range(SIZE):
    if a[i] < 0:
        max_ = a[i]
        for j in a[i:]:
            if max_ < j < 0:
                max_ = j
        break

print(f'В массиве макс. отрицательный элемент это {max_}' if max_ < 0 else 'В массиве нет отрицательных чисел')

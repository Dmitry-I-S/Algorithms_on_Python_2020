# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

SIZE = 99
MIN_ITEM = 2
MAX_ITEM = 100

a = [i for i in range(MIN_ITEM, MAX_ITEM)]
b = [i for i in range(2, 9)]


for i in b:
    max = 0         # переменная для сохранения кол-ва кратных чисел
    for j in a:
        if j % i == 0:
            max += 1
    print(f'числу {i} - кратны {max} чисел из списка')

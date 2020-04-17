# Задача 6 к уроку 4.
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import timeit
import cProfile


# Первая функция для определенния суммы в массиве - стандартное решение без срезов с 2-мя циклами:
def sum_minmax_1(a):
    """Определяет сумму элементов между мин и макс элементами в аргументе(списке)"""
    max_i = 0       # сохраняем индексы объектов
    min_i = 0

    for i in range(len(a)):
        if a[i] > a[max_i]:
            max_i = i
        if a[i] < a[min_i]:
            min_i = i

    sum_ = 0
    if max_i < min_i:       # меняем значения индексов, чтобы идти от меньшего к большему в цикле, складывающем сумму
        max_i, min_i = min_i, max_i
    for k in range(min_i + 1, max_i):
        sum_ += a[k]
    return sum_


# Вторая функция для определенния суммы в массиве - больше встроенных функций, меньше кода:
def sum_minmax_2(a):
    """Определяет сумму элементов между мин и макс элементами в аргументе(списке)"""
    max_i = a.index(max(a))       # используем встроенные функции питона
    min_i = a.index(min(a))

    # Вычисляем сумму элементов между мин. и макс. создавая отдельный срез между элементами:
    between_a = a[min(min_i, max_i) + 1: max(min_i, max_i)]
    sum_ = sum(between_a)
    return sum_


# Третья функция для определенния суммы в массиве - "оптимизированная смесь" со срезом и доп. переменными:
def sum_minmax_3(a):
    """Определяет сумму элементов между мин и макс элементами в аргументе(списке)"""
    max_i = 0       # сохраняем индексы объектов
    min_i = 0
    max_a = float('-inf')       # сохраняем сами объекты в переменной
    min_a = float('inf')

    for i in range(len(a)):
        if a[i] > max_a:
            max_i = i
            max_a = a[i]    # записываем макс. значение в переменную, чтобы не обращаться к индексу при след. сравнении
        if a[i] < min_a:
            min_i = i
            min_a = a[i]    # записываем мин. значение в переменную, чтобы не обращаться к индексу при след. сравнении

    if max_i < min_i:       # меняем значения индексов, чтобы идти от меньшего к большему
        max_i, min_i = min_i, max_i

    sum_ = 0
    for k in a[min_i + 1: max_i]:   # идем циклом for по срезу и суммируем
        sum_ += k
    return sum_

# print(f"алгоритм 1: {sum_minmax_1(a)}, алгоритм 2: {sum_minmax_2(a)}, алгоритм 3: {sum_minmax_3(a)}")


# создаем списки а** с разным кол-вои элементов для тестирования
MIN_ITEM = -10
MAX_ITEM = 10

a5 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(5)]
a10 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(10)]
a15 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(15)]
a20 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(20)]
a25 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(25)]
a1000 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(1000)]
a100000 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(100000)]

# ТЕСТИРОВАНИЕ ПЕРВОГО СПОСОБА:

print(timeit.timeit('sum_minmax_1(a5)', number=50, globals=globals()))  #0.0002052599999999849
print(timeit.timeit('sum_minmax_1(a10)', number=50, globals=globals())) #0.0003258500000000164
print(timeit.timeit('sum_minmax_1(a15)', number=50, globals=globals())) #0.00044259000000002047
print(timeit.timeit('sum_minmax_1(a20)', number=50, globals=globals())) #0.0005494959999999827
print(timeit.timeit('sum_minmax_1(a25)', number=50, globals=globals())) #0.0006829150000000062
print(timeit.timeit('sum_minmax_1(a1000)', number=50, globals=globals())) #0.02270424900000001
print(timeit.timeit('sum_minmax_1(a100000)', number=50, globals=globals())) #2.318791279

cProfile.run('sum_minmax_1(a5)')	#0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_1(a10)')	#0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_1(a15)')	#0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_1(a20)')	#0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_1(a25)')	#0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_1(a1000)') #0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_1(a100000)') #0.000    0.000    0.040    0.040 {built-in method builtins.exec}

# Вывод 1 - зависимость, вероятно, линейная, что ожидаемо от этого алгоритма.
# cProfile с данными списками не позволяет оценить структуру

# ТЕСТИРОВАНИЕ ВТОРОГО СПОСОБА:

print(timeit.timeit('sum_minmax_2(a5)', number=50, globals=globals()))  #0.0001778919999999573
print(timeit.timeit('sum_minmax_2(a10)', number=50, globals=globals())) #0.00020525899999990216
print(timeit.timeit('sum_minmax_2(a15)', number=50, globals=globals())) #0.00023904199999957854
print(timeit.timeit('sum_minmax_2(a20)', number=50, globals=globals())) #0.00025101500000035415
print(timeit.timeit('sum_minmax_2(a25)', number=50, globals=globals())) #0.0003121660000000581
print(timeit.timeit('sum_minmax_2(a1000)', number=50, globals=globals())) #0.004939479999999996
print(timeit.timeit('sum_minmax_2(a100000)', number=50, globals=globals())) #0.480728928

cProfile.run('sum_minmax_2(a5)')	    #0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:41(sum_minmax_2)
cProfile.run('sum_minmax_2(a10)')	    #0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:41(sum_minmax_2)
cProfile.run('sum_minmax_2(a15)')	    #0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:41(sum_minmax_2)
cProfile.run('sum_minmax_2(a20)')	    #0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:41(sum_minmax_2)
cProfile.run('sum_minmax_2(a25)')	    #0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:41(sum_minmax_2)
cProfile.run('sum_minmax_2(a1000)')     #0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:41(sum_minmax_2)
cProfile.run('sum_minmax_2(a100000)')   #0.000    0.000    0.009    0.009 Lesson_4_Task_1.py:41(sum_minmax_2)

# Вывод 2: зависимость линейная. Алгоритм работает лучше, чем первый.
# Т.е. для этой задачи задачи встроенные функции питона дают лучший результат
# Это видно в т.ч. по результатам cProfile.

# ТЕСТИРОВАНИЕ ТРЕТЬЕГО СПОСОБА:

print(timeit.timeit('sum_minmax_3(a5)', number=50, globals=globals()))  #0.0004310450000000188
print(timeit.timeit('sum_minmax_3(a10)', number=50, globals=globals())) #0.00031302099999974686
print(timeit.timeit('sum_minmax_3(a15)', number=50, globals=globals())) #0.0004280510000000959
print(timeit.timeit('sum_minmax_3(a20)', number=50, globals=globals())) #0.0005144320000001201
print(timeit.timeit('sum_minmax_3(a25)', number=50, globals=globals())) #0.0005691670000000926
print(timeit.timeit('sum_minmax_3(a1000)', number=50, globals=globals())) #0.014823144999999815
print(timeit.timeit('sum_minmax_3(a100000)', number=50, globals=globals())) #1.5509780819999999

cProfile.run('sum_minmax_3(a5)')	    #0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_3(a10)')	    #0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_3(a15)')	    #0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_3(a20)')	    #0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_3(a25)')	    #0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_3(a1000)')     #0.000    0.000    0.000    0.000 {built-in method builtins.exec}
cProfile.run('sum_minmax_3(a100000)')   #0.000    0.000    0.030    0.030 {built-in method builtins.exec}

# Вывод 3: Третье решение, как нечто промежуточное между 1 и 2
# - дает средний  по времени результат (линейная зависимость)
# Таким образом, "ручная" частичная оптимизация поиска мин и макс помогла увеличить скорость работы в данном случае,
# но все равно не дотягивает до скорости встроенных функций в автоматизированном методе 2.

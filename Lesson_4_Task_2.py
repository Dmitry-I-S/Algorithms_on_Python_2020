# Написать два алгоритма нахождения i-го по счёту простого числа.
# # Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile

# Метод 1 - без решета Эратосфена
#
def is_simple(n):
    """Определяет, является ли аргумент простым числом"""
    for i in range(2, n):   # ищем остаток от деления в диапазоне до заданного числа
        if n % i == 0:
            return False
    return True


def return_simple(x):
    """Возвращает простое число по его номеру из списка простых чисел"""
    index = 0
    value = 1
    while x > index:
        value += 1
        if is_simple(value):
            index += 1
    return value


# Метод 2 - с решетом.
def sieve(x):
    """Возвращает простое число по его номеру из списка простых чисел"""
    len_ = x * x                    # прогнозиремый размер массива - подсказка найдена в википедии
    arr = [k for k in range(len_)]
    arr[1] = 0
    simple_counter = 1
    for i in range(2, len_):
        if arr[i] != 0:
            if simple_counter == x:
                return arr[i]
            simple_counter += 1
            j = i + i
            while j < len_:
                arr[j] = 0
                j += i

# Тестирование алгоритмов:
# for i in range(2, 100):
#     print(i, '---', return_simplsieve(i))

# Тестирование первого способа:
print(timeit.timeit('return_simple(50)', number=50, globals=globals()))  ## 0.04457890800000001
print(timeit.timeit('return_simple(100)', number=50, globals=globals()))  ## 0.185856348
print(timeit.timeit('return_simple(150)', number=50, globals=globals()))  ## 0.461231855
print(timeit.timeit('return_simple(200)', number=50, globals=globals()))  ## 0.911450692
print(timeit.timeit('return_simple(400)', number=50, globals=globals()))  ## 4.094929026
print(timeit.timeit('return_simple(800)', number=50, globals=globals()))  ## 16.889034661


cProfile.run('return_simple(50)')   # 228    0.001    0.000    0.001    0.000 Lesson_4_Task_2.py:10(is_simple)
cProfile.run('return_simple(100)')  # 540    0.004    0.000    0.004    0.000 Lesson_4_Task_2.py:10(is_simple)
cProfile.run('return_simple(150)')  # 862    0.008    0.000    0.008    0.000 Lesson_4_Task_2.py:10(is_simple)
cProfile.run('return_simple(200)')  # 1222    0.017    0.000    0.017    0.000 Lesson_4_Task_2.py:10(is_simple)
cProfile.run('return_simple(400)')  # 2740    0.076    0.000    0.076    0.000 Lesson_4_Task_2.py:10(is_simple)
cProfile.run('return_simple(800)')  # 6132    0.343    0.000    0.343    0.000 Lesson_4_Task_2.py:10(is_simple)

# Вывод 1 - Зависимость, вероятно, параболическая - два вложенных цикла - в цикл while вложен цикл for. Согласно cProfile программа буксует
# на функции  is_simple, которая определяет, яв-ся ли число простым. Это вполне ожидаемо...

# Тестирование второго способа с решетом:
print(timeit.timeit('sieve(50)', number=50, globals=globals()))  ## 0.07131949700000018
print(timeit.timeit('sieve(100)', number=50, globals=globals()))  ## 0.30583471000000007
print(timeit.timeit('sieve(150)', number=50, globals=globals()))  ## 0.7055815579999996
print(timeit.timeit('sieve(200)', number=50, globals=globals()))  ## 1.2900327349999996
print(timeit.timeit('sieve(400)', number=50, globals=globals()))  ## 5.976309650999999
print(timeit.timeit('sieve(800)', number=50, globals=globals()))  ## 26.050270579000003

cProfile.run('sieve(50)')   # 0.000    0.000    0.002    0.002 {built-in method builtins.exec}
cProfile.run('sieve(100)')  # 0.000    0.000    0.006    0.006 {built-in method builtins.exec}
cProfile.run('sieve(150)')  # 0.000    0.000    0.014    0.014 {built-in method builtins.exec}
cProfile.run('sieve(200)')  # 0.000    0.000    0.026    0.026 {built-in method builtins.exec}
cProfile.run('sieve(400)')  # 0.000    0.000    0.119    0.119 {built-in method builtins.exec}
cProfile.run('sieve(800)')  # 0.000    0.000    0.556    0.556 {built-in method builtins.exec}

# Вывод 2 - Зависимость, вероятно, параболическая - так же, как и в первом случае (графики подтверждают)
# - ее могут давать два воженных цикла. Но в целом, этот алгоритм работает медленнее,
# видимо, из-за создания списка и обращения к нему.
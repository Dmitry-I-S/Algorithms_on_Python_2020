# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

LENGTH = 10
ARR = [random.uniform(0, 49) for _ in range(LENGTH)]
ARR_2 = [random.randint(0, 49) for _ in range(LENGTH)] # массив целых чисел для тестирования и наглядного сравнения
print(ARR, "массив изначально")
print(ARR_2)
print(sorted(ARR), "массив после сортировки sorted")
print(sorted(ARR_2), "массив 2 после сортировки sorted")


def fusion(arr_left, arr_right):
    """Выполняет  слияние и сортировку двух отсортированных массивов - аргументов, возвращает слитый массив"""
    arr_fusion = []
    i = j = 0
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] <= arr_right[j]:
            arr_fusion.append(arr_left[i])
            i += 1
        else:
            arr_fusion.append(arr_right[j])
            j += 1
    sorted_list = arr_fusion + arr_left[i::] + arr_right[j::]
    return sorted_list


def sort_merge(arr_):
    """Выполняет сортировку слиянием заданного массива"""
    if len(arr_) < 2:
        return
    mid = len(arr_) // 2
    arr_left = arr_[0:mid]
    arr_right = arr_[mid:len(arr_)]
    sort_merge(arr_left)
    sort_merge(arr_right)
    arr_sorted = fusion(arr_left, arr_right)
    for i in range(len(arr_)):
        arr_[i] = arr_sorted[i]


def method_check(func, arr):
    """Проверяет, правильно ли сортирует функция заданный массив"""
    array_copy = arr[:]
    func(arr)
    if arr == sorted(array_copy):
        print("Алгоритм работает правильно:")
        print(arr, " - результат сортировки функцией")
        print(sorted(array_copy), " - результат сортировки встроенным sorted()")
        return True
    else:
        print("Алгоритм не работает. Попробуй еще раз")
        return False


# Проверяем работы функции слияния двух списков:
print('Ж' * 100)
print('Результат проверки функции сливания двух списков fusion - ',
      fusion(sorted(ARR), sorted(ARR_2)) == sorted(ARR + ARR_2))
print('Слитый список выглядит так', fusion(sorted(ARR), sorted(ARR_2)))
print('Ж' * 100)

# Проверяем работы функции слияния двух списков используя "универсальную" проверочную функцию:
sort_merge(ARR)
print(ARR)

method_check(sort_merge, ARR)
print('Ж' * 100)
method_check(sort_merge, ARR_2)

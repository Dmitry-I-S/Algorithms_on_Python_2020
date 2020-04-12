# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def summa_1(n):
    """Возвращает сумму всех нат. чисел до n включительно"""
    if n == 0:
        return n
    else:
        return n + summa_1(n - 1)


def summa_2(n):
    """Возвращает сумму всех нат. чисел до n включительно"""
    return int(n * (n - 1) / 2)


n = int(input('Введите натуральное число: '))
s_1 = summa_1(n)
s_2 = summa_2(n)
if s_1 == s_2:
    print(f'Способ расчета summ_1 дал результат {s_1}, как и способ summ_2 - {s_2}')
    print(f'Равенство выполняется')
else:
    print(f'Способ расчета summ_1 дал результат {s_1}, и не совпадает со способом summ_2 (результат {s_2})')
    print(f'Равенство невыполняется')


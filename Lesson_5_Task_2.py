# Задача 2 к уроку 5.
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import defaultdict, deque

SYS_16 = '0123456789ABCDEF'

DICT_to_16 = {} # словарик для перевода цифр hex-системы в числа Dec
for i in range(16):
    DICT_to_16[SYS_16[i]] = i

DICT_from_16 = {} # словарик для перевода в символы hex-системы
for i in range(16):
    DICT_from_16[i] = SYS_16[i]


str_1 = input('Введите первое число: ')
str_2 = input('Введите второе число: ')
result = deque([])

a = [i for i in str_1]
b = [i for i in str_2]
a = deque(a)
b = deque(b)
a.reverse() # разворачиваем числа для упрощения сложения
b.reverse()
if len(a) < len(b):     # делаем список а больше b
    a, b = b, a

for _ in range(len(a) - len(b)):
    b.extend('0')       # добавляем "0" в конец b, чтобы сделать длину b эквивалентной

# Присупаем к вычислениям
in_mind = 0     # единица в уме
for i in range(len(a)):
    sum_ = DICT_to_16[a[i]] + DICT_to_16[b[i]] + in_mind    # двигаемся слева направо, т.к. числа реверсивные
    if sum_ > 15:
        in_mind = 1
        num = abs(sum_ - 16)
        result.append(DICT_from_16[num])
        if i == (len(a) - 1):           # если опреция сложения последняя + единица в первой позиции
            result.append('1')
    else:
        in_mind = 0
        num = abs(sum_ - 16)
        result.append(DICT_from_16[sum_])

result.reverse()    # разворачиваем результат обратно

# Создаем функцию сложения Hex-чисел для проверки работы программы:
def sum_hex(a, b):
    a_16 = int('0x' + a, 16)
    b_16 = int('0x' + b, 16)

    sum_ = str(hex(a_16 + b_16)).upper()
    sum_list = [k for k in sum_[2:]]
    return sum_list


print(f'Результат сложения a и b = {result}, проверочный результат {sum_hex(str_1, str_2)}')


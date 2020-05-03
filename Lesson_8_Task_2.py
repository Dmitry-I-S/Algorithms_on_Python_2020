# 2) Закодируйте любую строку по алгоритму Хаффмана.
import collections


def huffman_chart(lett):
    """Возвращает словарь шифров по алгоритму Хаффмана, принимает на входе словарь частот символов"""
    if len(lett) == 2:
        dict_bin = dict(zip(lett.keys(), ['0', '1']))
        return dict_bin

    # Находим символы с наименьшей частотой для объединения в узел c помощью сортровки словаря
    # Вероятно, можно использовать свойства Счетчика: lett.most_common()[:-2-1:-1]
    # Но в таком случае, словарь все равно придется сортровать словарь, т.к. порядок для Хаффмана нарушается
    # Например, в словаре Counter({'a': 5, 'b': 2, 'r': 2, 'cd': 2}) объединяться будут 'r' и 'cd', но не 'b' и 'r'
    lett_tree = lett.copy()
    sorted_lett = sorted(lett.items(), key=lambda x: x[1])
    l = sorted_lett[0][0]
    r = sorted_lett[1][0]

    left, right, = lett_tree.pop(l), lett_tree.pop(r),
    lett_tree[l + r] = left + right           # добавляем новый узел со значением - сумма частот
    # print(lett_tree)

    bin_dict = huffman_chart(lett_tree)           # рекурсируем функцию на обновленный словарь с узлами
    spam = bin_dict.pop(l + r)
    bin_dict[l], bin_dict[r] = spam + '0', spam + '1'   # добавляем биты в строковом формате
    return bin_dict


def huffman_string(string_1):
    """Возвращает строку преобразованную по алгоритму Хаффмана"""
    letters = collections.Counter(string_1)     # таблица частот - создаем с помощью коллекций
    code = []
    bin_dict = huffman_chart(letters)
    for letter in string_1:                 # собираем строку по словарю
        bin_letter = bin_dict[letter]
        code.append(bin_letter)
    return code


string_1 = 'abracadabra'
letters = collections.Counter(string_1)
print(f'Строка {string_1} дает следующую таблицу частот: \n {letters}')
print(f'Строка после применения алгоритма: \n {huffman_string(string_1)}')
s = ''
print(f'Строка без прбелов: \n {s.join(huffman_string(string_1))}')

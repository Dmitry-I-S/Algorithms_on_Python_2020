# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


abc = int(input('Введите натуральное число: '))
cba = 0

while abc > 0:
    c = abc % 10
    abc = (abc - c) / 10
    cba = int(cba * 10 + c)

print(cba)
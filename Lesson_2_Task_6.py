# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

import random
n = random.randint(1, 100)
i = 0
print('Я загадал число от 1 до 100 и у тебя 10 попыток чтобы угадать его')

while True:
    guess = int(input('Введите отгадку: '))
    if guess == n:
        print('Верно!')
        break
    elif guess > n:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')
    i += 1
    if i == 10:
        print(f'Попытки исчерпаны, правилный ответ {n}')
        break

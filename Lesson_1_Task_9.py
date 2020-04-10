# https://drive.google.com/file/d/1yBFZax1S42wFmKcF8L9hYRgcNu2aN4hj/view?usp=sharing
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b:
    if a < c:
        print(f'Среднее число {a}')
    elif c > b:
        print(f'Среднее число {c}')
    else:
        print(f'Среднее число {b}')
elif b < c:
    print(f'Среднее число {b}')
elif a > c:
    print(f'Среднее число {a}')
else:
    print(f'Среднее число {c}')

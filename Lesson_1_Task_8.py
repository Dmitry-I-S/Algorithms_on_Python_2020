# https://drive.google.com/open?id=1yBFZax1S42wFmKcF8L9hYRgcNu2aN4hj
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите год на проверку високосности: '))


if year % 400 == 0:
    print('Год високосный')
elif year % 100 == 0:
    print('Год невисокосный')
elif year % 4 == 0:
    print('Год високосный')
else:
    print('Год невисокосный')
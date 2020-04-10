# https://drive.google.com/file/d/1yBFZax1S42wFmKcF8L9hYRgcNu2aN4hj/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


n = int(input('Введите трехзначное число: '))

x = n // 100        # цифра сотен
y = n % 100 // 10   # цифра десятков
z = n % 10          # цифра единиц

summ = x + y + z
mult = x * y * z

print(f'Сумма цифр числа = {summ}, произведение цифр числа = {mult}')

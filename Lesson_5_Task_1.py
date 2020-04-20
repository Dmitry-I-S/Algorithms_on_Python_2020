# Задача 1 к уроку 5.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, # чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

quantity = int(input('Введите кол-во компаний: '))

companies = [[] for i in range(quantity)]
total_income = 0            # для подсчета общего дохода сразу при вводе
stats = defaultdict(list)   # используем словарь по умолчанию с функцией list для создания пар Название:[доход]

for i in range(quantity):
    name = input('Введите название компании: ')
    companies[i].append(name)
    for k in range(1, 5):
        qr_income = float(input(f'Введите прибыль за {k}-й квартал '))
        stats[name].append(qr_income)       # пополняем список, присвоенный ключу
        total_income += qr_income           # считаем общий доход

average_income = total_income / quantity    # доход на одну компанию в среднем
print(f'Средняя прибыль по компаниям {average_income}')
above_list = [key for key in stats.keys() if sum(stats[key]) >= average_income]
below_list = [key for key in stats.keys() if sum(stats[key]) < average_income]
print('Компании с доходом выше среднего: ', above_list)
print('Компании с доходом ниже среднего: ', below_list)


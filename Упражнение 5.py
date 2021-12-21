revenue = float(input('Введите размер выручки '))
costs = float(input('Введите размер издержек '))
if costs > revenue:
    print('Фирма работает в убыток')
elif costs == revenue:
    print('Фирма работает вноль')
else:
    print(f'Фирма работает вприбыль, рентабельность составляет {revenue/costs:.2f}')
    members = int(input('Сколько сотрудников на фирме? '))
    print(f'Прибыль фирмы в расчете на одного сотрудника {revenue/members:.2f}')

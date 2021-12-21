a = 2
b = 4
day = 1
while a <= b:
    print(f'{day}-й день: {a:.2f} км')
    day = day+1
    a = float(1.1*a)
print(f'{day}-й день: {a:.2f}')
print(f'на {day}-й день спортсмен достиг результата не менее {b} км')
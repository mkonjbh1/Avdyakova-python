sec_st = int(input('укажите время в секундах '))
hour = int(sec_st / 3600)
min = int((sec_st - 3600*hour)/60)
sec = int(sec_st - 3600*hour - 60*min)


print('{}:{}:{}'. format(hour, min, sec))
print(f'{hour}:{min}:{sec}')
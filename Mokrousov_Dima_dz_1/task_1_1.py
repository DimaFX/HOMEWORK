print('Добро пожаловать в конвертер секунд в дни, часы, минуты')
duration = int(input('Укажите количество секунд: '))
day = duration // 86400 # 1 day = 86400 sec
hour= (duration - (day * 86400)) // 3600 # 1 hour = 3600 sec
minute= (duration - ((day * 86400) + (hour * 3600))) // 60 # 1 min = 60 sec
seconds = duration - ((day * 86400) + (hour * 3600) + (minute * 60))
print('{} дн, {} ч, {} мин, {} сек'.format(day, hour, minute, seconds))
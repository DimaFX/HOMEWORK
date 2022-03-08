percent = input('Укажите количество процентов: ')
if percent[-1] in '1':
    print(percent, 'процент')
elif percent[-1] in '2, 3, 4':
   print(percent, 'процента')
else:
    print(percent, 'процентов')
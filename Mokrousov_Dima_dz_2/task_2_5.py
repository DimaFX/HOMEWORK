commodity = [57.8, 46.51, 97, 32, 84.60, 29.99, 84.50, 26.33, 10.50, 48.8]
for item in commodity:
    rub = int(item)
    kop = (item - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп')

commodity = [57.8, 46.51, 97, 32, 84.60, 29.99, 84.50, 26.33, 10.50, 48.8]
print(id(commodity))
commodity.sort()
print(id(commodity))
for item in commodity:
    rub = int(item)
    kop = (item - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ') 


commodity = [57.8, 46.51, 97, 32, 84.60, 29.99, 84.50, 26.33, 10.50, 48.8]
for item in sorted(commodity)[::-1][:5]:
    rub = int(item)
    kop = (item - int(item)) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')  

print([f'{int(item)} руб {(item - int(item)) * 100:02.0f} коп' for item in sorted(commodity)[::-1][:5]])
# создал список кубов нечетных чисел
my_list = []
for i in range(1, 1001, 2):
    my_list.append(i ** 3)
#print(my_list)
# ------------------------------------
total_sum = 0 # общая сумма чисел
for i in my_list:
    digit_sum = 0 # сумма цифр
    for digit_i in str(i):
        digit_sum += int(digit_i)
    if digit_sum % 7 == 0:
        total_sum += i
print(total_sum)
# ------------------------------------
total_sum = 0
for i in my_list:
    i += 17
    digit_sum = 0
    for digit_i in str(i):
        digit_sum += int(digit_i)
    if digit_sum % 7 == 0:
        total_sum += i
print(total_sum) 
# -------------------------------------
# арифметика
total_sum = 0
for i in my_list:
    digit_i = i 
    digit_sum = 0 
    while digit_i > 0:
        digit_sum += digit_i % 10
        digit_i //= 10
    if digit_sum % 7 == 0:
        total_sum += i
print(total_sum)
# -------------------------------------
total_sum = 0
for i in my_list:
    i += 17
    digit_i = i
    digit_sum = 0 
    while digit_i > 0:
        digit_sum += digit_i % 10
        digit_i //= 10
    if digit_sum % 7 == 0:
        total_sum += i
print(total_sum)

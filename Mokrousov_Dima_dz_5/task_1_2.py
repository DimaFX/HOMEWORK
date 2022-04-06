max_val = 15
odd_nums_gen = (n for n in range(1, max_val + 1, 2))
print(type(odd_nums_gen))
print(next(odd_nums_gen))
print(list(odd_nums_gen))

max_val = 15
odd_nums_gen = (n for n in range(1, max_val + 1) if n % 2 != 0)
print(type(odd_nums_gen))
print(next(odd_nums_gen))
print(list(odd_nums_gen))
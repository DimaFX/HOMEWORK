

def odd_nums(max_value):
    n = 1
    while n <= max_value:
        yield n
        n += 2

odd_to_15 = odd_nums(15)
print(type(odd_to_15))
print(list(odd_to_15))


def odd_nums(max_value):
    n = 1
    while n <= max_value:
        if n % 2 !=0:
            yield n
        n += 1

odd_to_15 = odd_nums(15)
print(type(odd_to_15))
print(list(odd_to_15))





src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])

my_list = []
for x in src:
    if src.count(x) != 1:
        continue
    my_list.append(x)
print(my_list)
lst = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
lst_unique = []

for elem in lst:
    if elem not in lst_unique:
        lst_unique.append(elem)

print(lst_unique)
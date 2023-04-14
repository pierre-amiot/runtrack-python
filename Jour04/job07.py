def count_multiples_of_3(lst):
    count = 0
    for element in lst:
        if element % 3 == 0:
            count += 1
    return count

L = [8, 24, 48, 2, 16]

count = count_multiples_of_3(L)

print("Nombre de multiples de 3 dans la liste :", count)
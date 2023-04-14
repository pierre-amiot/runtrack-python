def tri_croissant(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

# exemple d'utilisation
L = [5, 3, 8, 1, 9, 2]
print("Liste initiale :", L)
L_triee = tri_croissant(L)
print("Liste triée :", L_triee)
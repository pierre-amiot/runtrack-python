def swap_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

L = [1, 2, 3, 4, 5]

print("Avant l'échange :", L)

swap_first_last(L)

print("Après l'échange :", L)
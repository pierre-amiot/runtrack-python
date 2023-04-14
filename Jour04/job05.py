def replace_with_sum(lst, index):
    lst[index] = lst[index-1] + lst[index+1]

L = [1, 2, 3, 4, 5]

print(L[1])

replace_with_sum(L, 3)

print(L[-1])
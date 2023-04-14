string = "abcdefghijklmnopqrstuvwxyz" * 10

n = 1
while (n * (n+1)) // 2 <= len(string):
    for i in range(n):
        print(string[(n-1)*n//2+i], end=" ")
    print()
    n += 1
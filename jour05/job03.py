def draw_carpet(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print("x", end="")
            else:
                print("o", end="")
        print()

draw_carpet(10)
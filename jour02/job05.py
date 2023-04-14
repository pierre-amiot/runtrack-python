def calcule(num1, operator, num2):
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    else:
        print("Opérateur invalide")
    return result

# exemples d'utilisation de la fonction calcule()
print(calcule(5, '+', 3)) # affichera 8
print(calcule(10, '-', 7)) # affichera 3
print(calcule(4, '*', 6)) # affichera 24
print(calcule(15, '/', 5)) # affichera 3.0
print(calcule(11, '%', 3)) # affichera 2
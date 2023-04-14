def CheckNumber(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("Le nombre est égal à 0")

# exemples d'utilisation de la fonction CheckNumber()
CheckNumber(5) # affichera "positif"
CheckNumber(-10) # affichera "negatif"
CheckNumber(0) # affichera "Le nombre est égal à 0"
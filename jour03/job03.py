def afficher_chiffres():
    for chiffre in range(101):
        if chiffre not in [26, 37, 88]:
            print(chiffre)

afficher_chiffres()

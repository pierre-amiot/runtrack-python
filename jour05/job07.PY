import string

def changer_mot(mot):
    # Vérifier si le mot est valide
    if not all(c in string.ascii_lowercase for c in mot):
        print("Le mot doit contenir uniquement des lettres minuscules de l'alphabet.")
        return mot
    
    # Convertir le mot en une liste de caractères
    liste_caract = list(mot)
    
    # Trouver l'indice du dernier caractère qui peut être déplacé
    dernier = len(liste_caract) - 1
    while dernier > 0 and liste_caract[dernier - 1] >= liste_caract[dernier]:
        dernier -= 1
    
    # Si tous les caractères sont dans l'ordre décroissant, retourner le mot original
    if dernier == 0:
        return mot
    
    # Trouver le plus petit caractère à droite du caractère à l'indice "dernier - 1"
    plus_petit = dernier
    for j in range(dernier + 1, len(liste_caract)):
        if liste_caract[j] > liste_caract[dernier - 1] and liste_caract[j] < liste_caract[plus_petit]:
            plus_petit = j
    
    # Échanger les caractères
    liste_caract[dernier - 1], liste_caract[plus_petit] = liste_caract[plus_petit], liste_caract[dernier - 1]
    
    # Trier les caractères restants dans l'ordre croissant
    liste_caract[dernier:] = reversed(liste_caract[dernier:])
    
    # Reconstituer le mot à partir de la liste de caractères modifiée
    nouveau_mot = ''.join(liste_caract)
    
    return nouveau_mot


# Exemple d'utilisation
mot_original = input("Entrez un mot contenant uniquement des lettres minuscules de l'alphabet : ")
nouveau_mot = changer_mot(mot_original)
print(f"Le nouveau mot le plus proche dans l'ordre alphabétique de '{mot_original}' est '{nouveau_mot}'.")
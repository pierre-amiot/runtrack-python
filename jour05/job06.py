def arrondir_notes(notes):
    """
    Cette fonction prend en paramètre une liste de notes et renvoie une liste
    de notes arrondies comme il se doit, selon les critères décrits.
    """
    notes_arrondies = []
    for note in notes:
        if note < 40:  # l'étudiant a échoué
            notes_arrondies.append(note)
        else:  # l'étudiant a réussi
            # on calcule le prochain multiple de 5 supérieur ou égal à la note
            prochain_multiple_5 = (note // 5 + 1) * 5
            # on arrondit la note si elle est à moins de 3 points du prochain multiple de 5
            if prochain_multiple_5 - note < 3:
                notes_arrondies.append(prochain_multiple_5)
            else:
                notes_arrondies.append(note)
    return notes_arrondies
notes = [33, 75, 68, 42, 91, 80]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)
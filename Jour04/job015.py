my_list = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres de la liste
for i in range(len(my_list)):
    my_list[i] = round(my_list[i])

# Trier la liste dans l'ordre croissant
my_list.sort()

# Afficher la liste
print(my_list)
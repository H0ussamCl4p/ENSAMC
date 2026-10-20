"""TP4 ex2 : les deux plus grands éléments d'une liste, en un seul parcours."""

liste = []
n = int(input("Veuillez saisir le nombre d'éléments de la liste : "))

for i in range(n):
    element = int(input(f"Saissez l'élément {i+1} : "))
    liste.append(element)


if len(liste) < 2:
    print("La liste doit contenir au moins 2 éléments.")
else:
    max1 = max2 = float("-inf")
    for nombre in liste:
        if nombre > max1:
            max2 = max1
            max1 = nombre
        elif nombre > max2:
            max2 = nombre
    print(f"Max1 est {max1}, Max2 est {max2}")

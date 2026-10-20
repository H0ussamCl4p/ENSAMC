"""TP5 ex2 : positions de chaque caractère d'une chaîne."""

def indice(chaine):
    d = {}
    for index, char in enumerate(chaine, start=1):
        if char in d:
            d[char].append(index)
        else:
            d[char] = [index]
    return d
chaine = "Mohammed"
resultat = indice(chaine)
print(resultat)

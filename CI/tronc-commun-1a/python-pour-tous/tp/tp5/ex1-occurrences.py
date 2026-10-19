"""TP5 ex1 : occurrences de chaque caractère d'un mot (dictionnaire)."""

def Occurrences(mot):
    d = {}
    exclude_chars = {'.', ',', ';', ':', '!', '?'}
    for char in mot.lower():  
        if char not in exclude_chars:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
    return d

mot = "ENSAM"
resultat = Occurrences(mot)
print(resultat)

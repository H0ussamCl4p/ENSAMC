"""TP5 ex3 : regrouper les anagrammes d'une liste de mots."""

def groupe_anagrammes(liste):
    ponctuation=",;:!?."
    table=str.maketrans('','',ponctuation)
    groupe_ana={}
    mots_presents=set()
    for mot in liste:
        mot_min=mot.lower().translate(table)
        if mot_min in mots_presents:
            continue
        cle=tuple(sorted(mot_min))
        if cle not in groupe_ana:
            groupe_ana[cle]=[]
        groupe_ana[cle].append(mot)
        mots_presents.add(mot_min)
    return groupe_ana        


liste=["listen", "silent", "triangle", "integral", "ENSAM"]
print(groupe_anagrammes(liste))

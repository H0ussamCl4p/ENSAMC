"""TP4 ex3 : vérifier si une chaîne est un palindrome (sans tenir compte des espaces et de la casse)."""

def est_palindrome(chaine):
    chaine = chaine.replace(" ", "").lower()
    return chaine == chaine[::-1]



chaine = input("Entrez une chaîne de caractères : ")
print(f"La chaîne '{chaine}' est un palindrome ? {est_palindrome(chaine)}")

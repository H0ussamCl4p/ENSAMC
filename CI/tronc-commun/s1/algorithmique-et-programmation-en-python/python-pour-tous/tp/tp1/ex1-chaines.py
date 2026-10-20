"""TP1 : fonctions sur les chaînes (compter les mots et les majuscules, palindrome, inverser les mots)."""

def compter_mots(phrase):
    mots = phrase.split()
    return len(mots)

def compter_majuscules(chaine):
    return sum(1 for c in chaine if c.isupper())

def est_palindrome(chaine):
    chaine_nettoyee = ''.join(c.lower() for c in chaine if c.isalnum())
    return chaine_nettoyee == chaine_nettoyee[::-1]

def inverser_mots(phrase):
    mots = phrase.split()
    mots_inverses = mots[::-1]
    return ' '.join(mots_inverses)

# Exemple d'utilisation
if __name__ == "__main__":
    phrase = input("Entrez une phrase : ")
    print(f"Nombre de mots dans la phrase : {compter_mots(phrase)}")
    
    chaine = input("Entrez une chaîne pour compter les majuscules : ")
    print(f"Nombre de lettres majuscules : {compter_majuscules(chaine)}")
    
    palindrome_chaine = input("Entrez une chaîne pour vérifier le palindrome : ")
    if est_palindrome(palindrome_chaine):
        print("C'est un palindrome.")
    else:
        print("Ce n'est pas un palindrome.")
    
    phrase_inverser = input("Entrez une phrase pour inverser l'ordre des mots : ")
    print(f"Phrase avec mots inversés : {inverser_mots(phrase_inverser)}")

"""TP5 ex5 : chiffrer et déchiffrer des données personnelles par décalage de 3 (César)."""

def recueil_donnees():
    carte_nationale = ["Nom", "Prénom", "Numéro de la CINE"]
    valeur = {}
    for i in carte_nationale:
        while True:
            try:
                valeur[i] = input(f"Entrez la valeur de {i} : ")
                break
            except ValueError:
                print("Erreur : Veuillez saisir une valeur valide.")
    return valeur

def chiffrement_donnees(valeur):
    ascii = {}
    for key in valeur:
        texte = ""
        for char in valeur[key]:
            if char.islower():
                texte += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            elif char.isupper():
                texte += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            elif char.isdigit():
                texte += chr((ord(char) - ord('0') + 3) % 10 + ord('0'))
            else:
                texte += char 
        ascii[key] = texte
    return ascii

def dechiffrement_donnees(valeur):
    ascii = {}
    for key in valeur:
        texte = ""
        for char in valeur[key]:
            if char.islower():
                texte += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
            elif char.isupper():
                texte += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
            elif char.isdigit():
                texte += chr((ord(char) - ord('0') - 3) % 10 + ord('0'))
            else:
                texte += char
        ascii[key] = texte
    return ascii


donnees = recueil_donnees()
print("Données originales :", donnees)
donnees_chiffre = chiffrement_donnees(donnees)
print("Données chiffrées :", donnees_chiffre)
donnees_dechiffre = dechiffrement_donnees(donnees_chiffre)
print("Données déchiffrées :", donnees_dechiffre)

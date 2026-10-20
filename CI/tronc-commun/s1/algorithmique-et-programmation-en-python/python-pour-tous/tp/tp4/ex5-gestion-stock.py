"""TP4 ex5 : gestion d'un stock de pièces avec NumPy (ajout, stocks critiques, tri, graphique matplotlib)."""

import numpy as np
import matplotlib.pyplot as plt

def ajouter_piece(tab, ref, nom, quantite, seuil):
    new_line = np.array([[ref, nom, int(quantite), int(seuil)]])
    tab = np.vstack([tab, new_line])
    return tab

def stocks_critiques(tab):
    critiques = []
    for i in range(1, len(tab)):  
        if int(tab[i][2]) <= int(tab[i][3]):
            critiques.append(tab[i])
    return np.array(critiques).reshape(-1, tab.shape[1])

def mettre_a_jour_stock(tab, ref, quantite):
    index = rechercher(tab, ref)
    if index != -1:
        tab[index][2] = str(int(tab[index][2]) + int(quantite))
        return tab
    else:
        print("Référence non trouvée.")
        return tab

def rechercher(tab, ref):
    for i in range(1, len(tab)): 
        if tab[i][0] == ref:
            return i
    return -1

def trier_par_quantite(tab):
    header = tab[0] 
    data = tab[1:] 
    data = data[data[:, 2].astype(int).argsort()]
    return np.vstack([header, data])

def affichage(tab):
    print("Référence\tNom\tQuantité\tSeuil")
    print("-" * 40)
    for i in range(1, len(tab)):
        print(f"{tab[i][0]}\t\t{tab[i][1]}\t{tab[i][2]}\t\t{tab[i][3]}")

def visualisation_graphique(tab):
    noms = tab[1:, 1]
    quantites = tab[1:, 2].astype(int)
    seuils = tab[1:, 3].astype(int)

    x = np.arange(len(noms))

    
    plt.bar(x, quantites, color='blue', label='Quantité en stock')
    plt.plot(x, seuils, color='red', marker='o', label='Seuil minimal')

    plt.xticks(x, noms, rotation=45)
    plt.xlabel('Pièces')
    plt.ylabel('Quantité')
    plt.title('Visualisation des stocks')
    plt.legend()
    plt.tight_layout()
    plt.show()


tab = np.array([["Ref", "Nom", "Quantité", "Seuil"]])

while True:
    print("\nMenu :")
    print("1. Ajouter une pièce")
    print("2. Afficher les stocks critiques")
    print("3. Trier par quantité")
    print("4. Visualiser graphiquement")
    print("5. Quitter")
    choix =input("Veuillez choisir une option : ")
    match choix:
        case "1":
            Ref = input("Veuillez saisir la référence de la pièce : ")
            Nom = input("Veuillez saisir le nom de la pièce : ")
            Quantite = input("Veuillez saisir la quantité de la pièce : ")
            Seuil = input("Veuillez saisir le seuil de la pièce : ")
            tab = ajouter_piece(tab, Ref, Nom, Quantite, Seuil)
            print("Tableau après ajout :")
            affichage(tab)
        case "2":
            print("\nStocks critiques :")
            critiques = stocks_critiques(tab)
            affichage(np.vstack([tab[0], critiques]))
        case "3":
            print("\nTableau trié par quantité :")
            tab = trier_par_quantite(tab)
            affichage(tab)
        case "4":
            print("\nVisualisation graphique des stocks :")
            visualisation_graphique(tab)
        case "5":
            print("Fin")
            break
        case _:
            print("Erreur : Choix invalide. Veuillez réessayer.")

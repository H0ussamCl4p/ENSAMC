---
title: Python-week2
date: 2025-04-28
author: CHOUBIK Houssam
draft: false
tags:
  - Python
  - ENSAMC
---

Les types de variables :
On a deux types de variables , variable **locale** et variable **globale**.
- Les variables locales sont propres à la fonction.
- Les variables globales sont définies à l'extérieur de la fonction et peuvent être utiliser par n'importe quelle fonction.

Exemple de **variable locale** :
```python
def ma_fonction():
x = 10 # Variable locale
print("Dans la fonction, x =", x)
ma_fonction() # Affiche la valeur x
```

Exemple de **variable globale**
```python
y = 20 # Variable globale
def ma_fonction():
print("Dans la fonction, y =", y)
ma_fonction() # Affiche : Dans la fonction, y = 20
print("En dehors de la fonction, y =", y) # Affiche : En dehors de la fonction, y = 20
```

 ## TP3
 Exercice 1 : 
 **Enoncé :**
 Menu d'Options avec Fonctions, match et Boucles
 
	1- Saisie de l'utilisateur : Demandez à l'utilisateur de saisir un nombre entier positif. Gérez les cas d'erreur, par exemple, si l'utilisateur saisit un nombre négatif ou une entrée non valide, en utilisant une boucle FAIRE … TANQUE.
	
	2- Affichage du Menu : Affichez un menu offrant les options suivantes, en plus d'une option pour quitter :
		A. Vérifier et afficher si le nombre est un nombre premier.
		B. Tester si un entier donné en entrée est pair ou impair.
		C. Convertir un nombre décimal non négatif en base b (où b est également saisi par l'utilisateur).
		D. Calculer la factorielle d’un entier non négatif donné en entrée.
		Q. Quitter le menu.
		
	3- Création de Fonctions : Pour chaque action du menu, créez une fonction distincte :
		A. est_premier(nombre)
		B. est_pair_impair(nombre)
		C. convertir_base(nombre, base)
		D. calculer_factorielle(nombre)
		
	4- Traitement du Choix :Utilisez match pour exécuter le bloc de code spécifique selon l'option choisie par l'utilisateur. Assurez-vous d'appeler la fonction correspondante en fonction du choix.
	
	5- Boucle Continue : Le programme doit continuer à exécuter, affichant le menu après chaque action, jusqu'à ce que l'utilisateur choisisse de quitter le programme (utiliser la boucle FAIRE … TANQUE).
	
**Corrigé :**
```python
def est_premier(nombre):

    if nombre > 1:

        for i in range(2, nombre):

            if nombre % i == 0:

                return 0

        return 1

    else:

        return 0

def est_pair_impair(nombre):

    if nombre % 2 == 0:

        return "pair"

    else:

        return "impair"

def convertir_base(nombre, base):  

    if base < 2 or base > 9:

        raise ValueError("La base doit être 2<=b<=9.")

    binaire = ""

    nb = nombre

    if nb == 0:

        binaire = "0"

    else:

        while nb > 0:

            binaire = str(nb % base) + binaire

            nb = nb // base  

    return binaire

def fact(nombre):

    if nombre < 0:

        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")

    if nombre == 0:

        return 1

    else:

        f = 1

        for i in range(1, nombre + 1):

            f = f * i

        return f

  
  

while True:

    x=int(input("Veuillez saisir un entier positif : "))

    if x >0:

        break

  

print("Pour activer le menu, veuillez tapez 1.")

m=int(input())

choice=0

while choice!=5:

    if m==1:

        print("Menu :")

        print("1. Vérifier et afficher si le nombre est un nombre premier.")

        print("2. Tester si un entier donné en entrée est pair ou impair.")

        print("3. Convertir un nombre décimal non négatif en base b (où b est également saisi par l'utilisateur).")

        print("4. Calculer la factorielle d’un entier non négatif donné en entrée.")

        print("5. Quitter le menu.")

        print("Veuillez choisir une option.")

        choice=int(input())

        match choice:

            case 1:

                if est_premier(x):

                    print(f"{x} est un nombre premier.")

                else:

                    print(f"{x} n'est pas un nombre premier.")

            case 2:

                pair_impair = est_pair_impair(x)

                print(f"{x} est un nombre {pair_impair}.")

            case 3:

                b = int(input("Veuillez saisir la base (supérieure ou égale à 2) : "))

                try:

                    binaire = convertir_base(x, b)

                    print(f"Le nombre {x} en base {b} est : {binaire}")

                except ValueError as e:

                    print(e)

            case 4:

                try:

                    f = fact(x)

                    print(f"La factorielle de {x} est : {f}")

                except ValueError as e:

                    print(e)

            case 5:

                print("Au revoir !")

            case _:

                print("Erreur : option invalide.")
```

Exercice 2 :

**Enoncé :**
On souhaite programmer une application simulant le fonctionnement d'un distributeur automatique de billets de banque.

	1.Le programme demande à l'utilisateur de saisir un montant qu'il souhaite retirer.
	
	2.Il vérifie si le montant est un multiple de 100 DH (montant minimal requis pour un retrait).
	
	3.Si le montant est valide, le programme simule la remise des billets en optimisant le nombre de billets distribués (200 DH et 100 DH).
	
	4.Le programme affiche ensuite un récapitulatif du retrait effectué.
	
	Q1. Écrire une fonction pour demander à l'utilisateur le montant à retirer :
	Si le montant n'est pas un multiple de 100 DH, la fonction redemande un montant valide.
	Q2. Écrire une fonction qui vérifie si le montant demandé est inférieur ou égal au solde disponible. Le solde disponible est fixé dans le programme principal (par exemple, 5000 DH) et est affiché à l'utilisateur avant qu'il ne saisisse le montant. Si le montant est supérieur au solde disponible, afficher un message d'erreur. Sinon, valider le montant demandé.
	Q3. Écrire une fonction qui simule la remise des billets en utilisant le minimum de billets : Les billets disponibles sont : 200 DH et 100 DH.
	Par exemple :
	Montant à retirer : 700 DH
	Billets distribués : 3 billet(s) de 200 DH + 1 billet(s) de 100 DH
	ENSAM-Casablanca Programmation Python API-2
	3
	Q4. Écrire une fonction qui met à jour le solde disponible en fonction du montant retiré.
	Q5. Écrire un programme principal pour simuler l’interaction complète avec l’utilisateur, en utilisant les fonctions précédentes :
	1-Demander le montant.
	2-Vérifier la validité du montant et le solde disponible.
	3-Calculer et afficher les billets distribués.
	4-Mettre à jour et afficher le solde après le retrait.




**Corrigé :**

```python
def retirer(montant):

    while montant % 100 != 0:

        print("Le montant doit être un multiple de 100 DH.")

        montant = int(input("Veuillez saisir un montant à retirer : "))

    return montant

  

def verifier_solde(montant, solde):

    if montant > solde:

        print("Montant supérieur au solde disponible.")

        return False

    return True

35

def distribuer_billets(montant):

    billets200 = montant // 200

    montant = montant % 200

    billets100 = montant // 100

    return billets200, billets100

  

def mettre_a_jour_solde(solde, montant):

    return solde - montant

  
  

solde = 5000  

print(f"Solde disponible : {solde} DH")

  

montant = int(input("Veuillez saisir le montant à retirer : "))

  

montant = retirer(montant)

  

if verifier_solde(montant, solde):

    billets200, billets100 = distribuer_billets(montant)

    solde = mettre_a_jour_solde(solde, montant)

    print(f"Billets distribués : {billets200} billet(s) de 200 DH + {billets100} billet(s) de 100 DH")

    print(f"Solde après retrait : {solde} DH")

else:

    print("Retrait annulé.")
```


## TP 4



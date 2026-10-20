"""TP3 ex1 : menu (premier, pair / impair, conversion en base b, factorielle) avec match."""

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

choice=0
while choice!=5:
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

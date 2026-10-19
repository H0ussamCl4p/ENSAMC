"""TP2 ex3 q4 : conversion d'un entier positif en binaire."""

while True:
    n = int(input("Veuillez saisir un entier positif n : "))
    if n < 0:
        print("Le nombre doit être positif. Veuillez réessayer.")
    else:
        break

binaire = ""
nb = n
if nb == 0:
    binaire = "0"
else:
    while nb > 0:
        binaire = str(nb % 2) + binaire 
        nb = nb // 2  

print(f"Le nombre {n} en binaire est : {binaire}")

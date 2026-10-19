m=float(input("Entrez le montant hors taxes d'un article: "))
t=float(input("Entrez le taux de TVA: "))
nb=float(input("Entrez le nombre d'articles: "))

total_ttc=nb*m*(1+t)
print("Le montant total TTC est de: ", total_ttc)
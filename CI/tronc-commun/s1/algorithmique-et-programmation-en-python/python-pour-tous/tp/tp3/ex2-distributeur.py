"""TP3 ex2 : distributeur automatique de billets (200 DH et 100 DH)."""

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

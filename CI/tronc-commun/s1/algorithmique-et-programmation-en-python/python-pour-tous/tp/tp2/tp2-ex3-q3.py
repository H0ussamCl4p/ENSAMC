"""TP2 ex3 q3 : plus grand diviseur de N autre que lui-même."""

def plus_grand_diviseur(n):
    if n <= 1:
        return None
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i

N = int(input("Entrez un entier N > 1 : "))
if N > 1:
    print(f"Le plus grand diviseur de {N} autre que lui-même est : {plus_grand_diviseur(N)}")
else:
    print("Entrez un entier supérieur à 1.")

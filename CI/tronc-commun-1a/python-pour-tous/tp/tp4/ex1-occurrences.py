"""TP4 ex1 : nombre d'occurrences de chaque élément d'une liste."""

# Saisir la liste d'entiers
liste = []
n = int(input("Entrez le nombre d'éléments dans la liste : "))

for i in range(n):
    element = int(input(f"Entrez l'élément {i+1} : "))
    liste.append(element)

occurrences = {}


for nombre in liste:
    if nombre in occurrences:
        occurrences[nombre] += 1
    else:
        occurrences[nombre] = 1


print("\nOccurrences des éléments :")
for key in occurrences:
    print(f"L'élément {key} apparaît {occurrences[key]} fois")

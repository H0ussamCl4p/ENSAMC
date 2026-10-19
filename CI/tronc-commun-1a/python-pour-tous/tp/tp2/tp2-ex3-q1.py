#Partie1

n=int(input("Entrer un entier:"))
s= int(0)
for i in range(1,n+1):
    s=s+i
print("La somme des entiers de 1 à n est: ", s)

#Partie2

nombre_secret = 7 
N = int() 

while True:
    N = int(input("Entrez un nombre : "))  
    if N == nombre_secret:  
        print("Nombre secret trouvé.") 
        break 


## ***Made by Choubik Houssam***

# **(2024-2025)** TD2-Boucles et Tableaux


---

## **Exercice 01 :**  
**Ecrire un Algorithme qui demande deux entiers à l'utilisateur et qui calcul la somme des entiers comprix entre ces deux valeurs.**
Par exemple, si l'on entre 5 et 12, le programme doit afficher 68:
5+6+7+8+9+10+11+12=68
```
ALGORITHME somme_entiers
  a, b, c, S : ENTIER
DEBUT
  AFFICHER("Donner la valeur de a et b:")
  LIRE(a,b)
  SI (a>b) ALORS
    c <- a
    a <- b
    b <- c
  FINSI
  S <- 0
  POUR ( i<-a , i<=b , i<-i+1 )
    S <- a + i
  FINPOUR
  AFFICHER("La somme de a et b est :", S)
FIN

```

## **Exercice 02 :** 
__Ecrire un Algorithme qui affiche les 9 tables de multiplication pour les entiers de 1 à 9.__
```
ALGORITHME table_multiplication
  m, i, j : ENTIER
DEBUT
  POUR (i<-1, i<=9, i<-i+1)
    POUR (j<-1, j<=9, j<-j+1)
      m <- i*j
      AFFICHER(m, ' ')
    FINPOUR
    AFFICHERLN()
  FINPOUR
FIN
```


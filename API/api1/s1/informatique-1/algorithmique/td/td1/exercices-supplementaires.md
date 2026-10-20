---
title: "TD1 Exercices supplémentaires"
date: 2024-10-01
author: CHOUBIK Houssam
tags: [algorithmique, api1]
---

# TD1 Exercices supplémentaires

## **Exercice 01 :**  
**Ecrire un Algorithme qui demande la valeur de n et calcul S=1+1/2+..+1/n**
```
ALGORITHME calcul_somme
  n, i, S : ENTIER
DEBUT
  AFFICHER("Donner la valeur de n:")
  LIRE(n)
  S <- 0 /* Initialisation*/
  POUR ( i<-1 , i<=n , i<-i+1 )
    S <- S + 1/i
  FIN POUR
  AFFICHER("Voici la somme S=", S)
FIN

```

## **Exercice 02 :** 
__Ecrire un Algorithme qui demande la valeur de n et calcul n!=1x2x..xn__
```
ALGORITHME calcul_factorielle
  n, i, F : ENTIER
DEBUT
  AFFICHER("Entrez la valeur de n :")
  LIRE(n)
  F <- 1
  POUR ( i<-1, i<=n , i<-i+1 )
    F <- F*i
  FIN POUR
  AFFICHER("Le factorielle de n=", n,"est F=", F)
FIN
```

## **Exercice 03 :** 
**Soit U<sub>0</sub> = 3 et U<sub>n</sub> = 2 + U<sub>n-1</sub>**

**Ecrire un Algorithme qui calcul U<sub>n</sub> et Somme (i=0 à n) de U<sub>k</sub>**
```
ALGORITHME cacul_termegen_somme
  n, i, S, U : ENTIER
DEBUT
  AFFICHER("Donner la valeur de n :")
  LIRE(n)
  U <- 3
  S <- U
  POUR ( i<1, i<=n, i<-i+1 )
    U <- U + 2
    S <- S + U
  FIN POUR
  AFFICHER("Voici le terme generale Un =", U, " Et La somme S=", S)
FIN
```

## **Exercice 04 :** 
**Soit U<sub>0</sub> = 3 et U<sub>n</sub> = 2 + U<sub>n-1</sub>**

**Ecrire un Algorithme qui donne la plus petite valeur de n tq U<sub>n</sub> > 130**
```
ALGORITHME value_n
  n, U : ENTIER
DEBUT
  U <- 3
  n <- 0
  TANT QUE ( U <= 130 )
    U <- 2 + U
    n <- n+1
  FINTQ
  AFFICHER(La plus petite valeur de n est", n)
FIN
```

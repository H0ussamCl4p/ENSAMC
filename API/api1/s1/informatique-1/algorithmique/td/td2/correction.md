---
title: "TD2 Boucles et tableaux (correction)"
date: 2024-10-15
author: CHOUBIK Houssam
tags: [algorithmique, api1]
---

# TD2 Boucles et tableaux (correction)

## Exercice 01

**Écrire un algorithme qui demande deux entiers à l'utilisateur et qui calcule la somme des entiers compris entre ces deux valeurs.**
Par exemple, si l'on entre 5 et 12, le programme doit afficher 68 : 5+6+7+8+9+10+11+12 = 68

```
ALGORITHME somme_entiers
  a, b, c, i, S : ENTIER
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
    S <- S + i
  FINPOUR
  AFFICHER("La somme des entiers entre a et b est :", S)
FIN
```

## Exercice 02

**Écrire un algorithme qui affiche les 9 tables de multiplication pour les entiers de 1 à 9.**

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

## Exercice 05

**Écrire un algorithme qui affiche le nombre de chiffres d'un entier N (positif ou négatif) introduit par l'utilisateur.**

```
Introduire un nombre: 123
Le nombre 123 a 3 chiffres.
Introduire un nombre: 580499
Le nombre 580499 a 6 chiffres.
```

```
ALGORITHME nombre_chiffres
  N, M, NC : ENTIER
DEBUT
  AFFICHER("Introduire un nombre:")
  LIRE(N)
  M <- N
  NC <- 0
  FAIRE
    M <- M / 10      /* division entière, marche aussi si N est négatif */
    NC <- NC + 1
  TANT QUE (M != 0)
  AFFICHER("Le nombre ", N, " a ", NC, " chiffres.")
FIN
```

## Exercice 10

1. **Écrire un algorithme qui affiche tous les diviseurs d'un entier n introduit par l'utilisateur.**
2. **Écrire un algorithme qui détermine si un nombre n est un carré parfait.**
3. **Écrire un algorithme qui détermine si un nombre n est premier.**

```
ALGORITHME diviseurs
  n, i : ENTIER
DEBUT
  FAIRE
    AFFICHER("Veuillez entrer un nombre:")
    LIRE(n)
  TANT QUE (n<=0)
  POUR (i<-1, i<=n, i<-i+1)
    SI (n%i = 0) ALORS
      AFFICHER(i, ' ')
    FINSI
  FINPOUR
FIN
```

```
ALGORITHME carre_parfait
  n, i : ENTIER
DEBUT
  LIRE(n)
  i <- 0
  TANT QUE (i*i < n)
    i <- i + 1
  FINTQ
  SI (i*i = n) ALORS
    AFFICHER(n, " est un carré parfait (", i, "²)")
  SINON
    AFFICHER(n, " n'est pas un carré parfait")
  FINSI
FIN
```

```
ALGORITHME nombre_premier
  n, i : ENTIER
  premier : BOOLEEN
DEBUT
  LIRE(n)
  premier <- (n >= 2)
  i <- 2
  TANT QUE (premier ET i*i <= n)
    SI (n%i = 0) ALORS
      premier <- FAUX
    FINSI
    i <- i + 1
  FINTQ
  SI (premier) ALORS
    AFFICHER(n, " est premier")
  SINON
    AFFICHER(n, " n'est pas premier")
  FINSI
FIN
```

## Exercice 12

**Écrire un algorithme qui inverse l'ordre des éléments d'un tableau d'entiers : le dernier élément passe en premier, et ainsi de suite.**

Tableau initial :

| 55 | 39 | 47 | 5 | 17 | 29 | 37 | 4 |
|----|----|----|---|----|----|----|---|

Tableau après inversion :

| 4 | 37 | 29 | 17 | 5 | 47 | 39 | 55 |
|---|----|----|----|---|----|----|----|

Le nombre et les éléments du tableau sont introduits par l'utilisateur, et l'algorithme affiche le tableau inversé.

```
ALGORITHME inverser_tableau
  T[100], a, n, i : ENTIER
DEBUT
  AFFICHER("Veuillez saisir le nombre d'éléments:")
  LIRE(n)
  POUR (i<-0, i<n, i<-i+1)
    AFFICHER("T[", i, "] = ")
    LIRE(T[i])
  FINPOUR
  /* on s'arrête au milieu, sinon on remet le tableau dans l'ordre initial */
  POUR (i<-0, i<n/2, i<-i+1)
    a <- T[i]
    T[i] <- T[n-1-i]
    T[n-1-i] <- a
  FINPOUR
  POUR (i<-0, i<n, i<-i+1)
    AFFICHER(T[i], ' ')
  FINPOUR
FIN
```

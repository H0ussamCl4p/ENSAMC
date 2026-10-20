---
title: "Tri par déplacement en tête"
author: CHOUBIK Houssam
tags: [algorithmique, api1, tri]
---

# Tri par déplacement en tête

Tri d'un tableau de n réels (n < 11). À chaque fois que deux voisins sont mal placés, le plus petit est retiré et remis au début du tableau. On recommence tant qu'il y a eu un déplacement.

```
ALGORITHME tri_de_staline
  N[11], t : REEL
  j, m, i, k, n : ENTIER

DEBUT
  AFFICHER("Veuillez saisir le nombre de chiffres (<11) :")
  LIRE(n)
  SI (n<11) ALORS
    AFFICHER("Veuillez entrer vos chiffres:")
    POUR ( i <- 0 , i < n , i <- i + 1 )
      AFFICHER("Chiffre ", i + 1, " : ")
      LIRE(N[i])
    FIN POUR
    j <- 0
    m <- 1  
    TANT QUE ( m != 0 )
      m <- 0
      POUR ( i <- 0 , i < n - 1 - j , i <- i + 1 ) 
        SI ( N[i] > N[i + 1] ) ALORS
          t <- N[i + 1]
          POUR ( k <- i + 1 , k > 0 , k <- k - 1 )
            N[k] <- N[k - 1]
          FIN POUR
          N[0] <- t
          m <- m + 1
        FIN SI
      FIN POUR
      j <- j + 1
    FIN TANT QUE
    AFFICHER("Tableau ordoné : ")
    POUR ( i <- 0 , i < n , i <- i + 1 )
      AFFICHER(N[i], " ")
    FIN POUR
  SINON
    AFFICHER("Le nombre de chiffre invalide !")
FIN.
```

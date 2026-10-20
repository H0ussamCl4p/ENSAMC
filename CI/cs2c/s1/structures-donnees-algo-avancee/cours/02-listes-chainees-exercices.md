---
title: "Listes chaînées : exercices"
date: 2025-09-26
author: CHOUBIK Houssam
tags: [dsa, cs2c]
---

# Listes chaînées : exercices

## Exercice 1 : une liste de trois nœuds à la main

Créer trois nœuds `(10, "A")`, `(20, "B")`, `(30, "C")`, les relier, afficher la liste puis libérer la mémoire.

```
tete --> (10, "A") --> (20, "B") --> (30, "C") --> NULL
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    int n;
    char ch[10];
    struct Node *next;
};

int main(void) {
    struct Node *n1 = malloc(sizeof(struct Node));
    struct Node *n2 = malloc(sizeof(struct Node));
    struct Node *n3 = malloc(sizeof(struct Node));
    if (n1 == NULL || n2 == NULL || n3 == NULL) return 1;

    n1->n = 10;
    strcpy(n1->ch, "A");
    n2->n = 20;
    strcpy(n2->ch, "B");
    n3->n = 30;
    strcpy(n3->ch, "C");

    n1->next = n2;
    n2->next = n3;
    n3->next = NULL;

    for (struct Node *p = n1; p != NULL; p = p->next)
        printf("(%d, \"%s\")\n", p->n, p->ch);

    free(n1);
    free(n2);
    free(n3);
    return 0;
}
```

Sortie :

```
(10, "A")
(20, "B")
(30, "C")
```

## Remarque : point ou flèche

Ces deux écritures sont équivalentes :

```c
(*n1).n = 10;
n1->n = 10;
```

`n1->n` veut dire « le champ `n` de la struct pointée par `n1` ». Les parenthèses de la première forme sont obligatoires, car `.` est prioritaire sur `*`.

## La suite

Les exercices complets (saisie au clavier, insertion, suppression, affichage à l'envers) sont dans [exercices/](../exercices/). Ensuite : [Piles (LIFO)](03-piles-lifo.md).

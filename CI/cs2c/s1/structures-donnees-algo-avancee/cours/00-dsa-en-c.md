---
title: "Les bases du C pour les structures de données"
date: 2025-09-24
author: CHOUBIK Houssam
tags: [dsa, cs2c]
---

# Les bases du C pour les structures de données

Une **structure de données**, c'est une façon de ranger des données en mémoire pour que certaines opérations soient rapides : ajouter, chercher, retirer. Avant les listes, piles et files, il faut être à l'aise avec quatre outils du C : les `struct`, les pointeurs, `malloc` et `free`.

## struct et typedef

Une `struct` regroupe plusieurs valeurs sous un seul nom :

```c
struct Etudiant {
    char nom[30];
    int age;
    float moyenne;
};

struct Etudiant e = {"Sara", 20, 15.5};
printf("%s a %d ans\n", e.nom, e.age);
```

`typedef` évite de répéter le mot `struct` partout :

```c
typedef struct {
    char nom[30];
    int age;
} Etudiant;

Etudiant e;   /* au lieu de struct Etudiant e; */
```

Bonne habitude : déclarer ses `struct` et ses `typedef` en haut du fichier, avant les fonctions qui les utilisent.

## Pointeurs

Un pointeur contient une **adresse** mémoire.

```
  variable x            pointeur p
 +---------+           +-----------+
 |   42    | <-------- |  &x       |
 +---------+           +-----------+
 adresse 0x100          contient 0x100
```

```c
int x = 42;
int *p = &x;     /* p pointe sur x */
*p = 7;          /* on modifie x à travers p : x vaut maintenant 7 */
```

Avec une `struct`, deux écritures équivalentes pour accéder à un champ à travers un pointeur :

```c
Etudiant *pe = &e;
(*pe).age = 21;
pe->age = 21;    /* la flèche, plus lisible */
```

## malloc et free

`malloc` réserve de la mémoire **pendant l'exécution** et renvoie son adresse. C'est ce qui permet aux listes de grandir autant qu'il faut.

```c
#include <stdlib.h>

int *t = malloc(5 * sizeof(int));   /* un tableau de 5 entiers */
if (t == NULL) {                    /* malloc peut échouer : toujours vérifier */
    printf("Plus de mémoire\n");
    return 1;
}
t[0] = 10;
free(t);                            /* rendre la mémoire quand on a fini */
t = NULL;                           /* évite de réutiliser une adresse libérée */
```

Règle simple : **un `malloc`, un `free`**. Oublier le `free` crée une fuite mémoire ; utiliser un pointeur après son `free` est un bug grave.

### Matrice dynamique

Pour une matrice dont la taille n'est connue qu'à l'exécution, on utilise un **pointeur de pointeur** : un tableau de lignes, chaque ligne étant un tableau.

```
 m ---> +------+     +----+----+----+
       | m[0] | ---> |    |    |    |   ligne 0
       +------+     +----+----+----+
       | m[1] | ---> |    |    |    |   ligne 1
       +------+     +----+----+----+
```

```c
int **m = malloc(lignes * sizeof(int *));
for (int i = 0; i < lignes; i++)
    m[i] = malloc(colonnes * sizeof(int));

m[1][2] = 5;

for (int i = 0; i < lignes; i++)    /* on libère dans l'ordre inverse */
    free(m[i]);
free(m);
```

## Lire et écrire des fichiers

On travaille avec un pointeur de type `FILE *`, obtenu avec `fopen(nom, mode)` :

| Mode | Effet |
|---|---|
| `"r"` | Lecture (le fichier doit exister) |
| `"w"` | Écriture (crée le fichier ou efface son contenu) |
| `"a"` | Ajout à la fin du fichier |

```c
FILE *f = fopen("notes.txt", "w");
if (f == NULL) {
    printf("Impossible d'ouvrir le fichier\n");
    return 1;
}
fprintf(f, "%s %.2f\n", "Sara", 15.5);   /* comme printf, mais dans le fichier */
fclose(f);

f = fopen("notes.txt", "r");
char nom[30];
float moy;
while (fscanf(f, "%29s %f", nom, &moy) == 2)   /* comme scanf, depuis le fichier */
    printf("%s : %.2f\n", nom, moy);
fclose(f);
```

`fscanf` renvoie le nombre de valeurs lues : la boucle s'arrête à la fin du fichier.

## Mesurer la rapidité : la notation O

On compare les structures par le **nombre d'étapes** d'une opération quand il y a n éléments :

| Notation | Se lit | Exemple |
|---|---|---|
| O(1) | temps constant | lire `t[3]`, empiler sur une pile |
| O(n) | temps linéaire | chercher une valeur dans une liste |
| O(n²) | temps quadratique | tri à bulles |

Une opération en O(1) prend le même temps avec 10 ou 10 millions d'éléments. C'est ce qu'on cherche pour les opérations les plus fréquentes.

## La suite

1. [Listes chaînées](01-listes-chainees.md)
2. [Listes chaînées : exercices](02-listes-chainees-exercices.md)
3. [Piles (LIFO)](03-piles-lifo.md)
4. [Files (FIFO), et LIFO contre FIFO](04-files-fifo.md)

## Pour aller plus loin

- [Learn DSA in C](https://www.geeksforgeeks.org/c/learn-dsa-in-c/), GeeksforGeeks (en anglais) : le programme complet des structures de données en C.

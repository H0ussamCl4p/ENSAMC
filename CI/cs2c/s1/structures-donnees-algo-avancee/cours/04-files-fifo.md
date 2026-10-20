---
title: "Files (FIFO)"
date: 2025-10-20
author: CHOUBIK Houssam
tags: [dsa, cs2c, file, fifo, queue]
---

# Files : FIFO

## L'idée

Pense à la queue devant un guichet. Les gens arrivent **à la fin**, et on sert toujours **celui qui est devant**. Le premier arrivé est le premier servi.

C'est le principe **FIFO** : *First In, First Out*, premier entré, premier sorti.

```
 sortie                                   entrée
   <--  [ A ] [ B ] [ C ] [ D ]  <--
        avant                arrière
       (front)               (rear)
```

On ajoute à l'**arrière**, on retire à l'**avant**. Deux bouts différents, c'est toute la différence avec une pile.

## Où on en croise dans la vraie vie

- **L'imprimante** : les documents sont imprimés dans l'ordre d'envoi.
- **Un serveur web** : les requêtes attendent dans une file avant d'être traitées.
- **Le clavier et le réseau** : les touches et les paquets arrivent dans un tampon (*buffer*) et sont lus dans l'ordre d'arrivée.
- **Le système d'exploitation** : l'ordonnanceur fait passer les processus chacun leur tour (*round robin*).
- **Le parcours en largeur d'un graphe** (BFS) : on visite les voisins dans l'ordre où on les a découverts.

## Les opérations

| Opération | Rôle | Coût |
|---|---|---|
| `enfiler(x)` (*enqueue*) | Ajoute x à l'arrière | O(1) |
| `defiler()` (*dequeue*) | Retire et renvoie l'élément de l'avant | O(1) |
| `tete()` (*front*, *peek*) | Renvoie l'avant sans le retirer | O(1) |
| `est_vide()` | La file est-elle vide ? | O(1) |

## Version 1 : avec un tableau circulaire

### Le piège du tableau simple

Si on retire à l'avant en avançant un indice `debut`, les cases du début ne servent plus jamais :

```
 après 3 enfilements et 2 défilements :
 +---+---+---+---+---+
 | x | x | C |   |   |      les cases x sont perdues
 +---+---+---+---+---+
           ^
         debut
```

Décaler tout le tableau à chaque `defiler` coûterait O(n). La bonne solution : faire **tourner** les indices avec le modulo `%`. Arrivé au bout, on repart à la case 0.

```
 MAX = 5, debut = 3, 3 éléments :

 indice:   0     1     2     3     4
        +-----+-----+-----+-----+-----+
        |  C  |     |     |  A  |  B  |
        +-----+-----+-----+-----+-----+
                             ^
                           debut      prochain ajout : (3 + 3) % 5 = 1
```

```c
#include <stdio.h>

#define MAX 5

typedef struct {
    int t[MAX];
    int debut;       /* indice de l'avant */
    int taille;      /* nombre d'éléments */
} File;

void init(File *f)            { f->debut = 0; f->taille = 0; }
int est_vide(const File *f)   { return f->taille == 0; }
int est_pleine(const File *f) { return f->taille == MAX; }

int enfiler(File *f, int x) {
    if (est_pleine(f)) return 0;
    int fin = (f->debut + f->taille) % MAX;   /* case libre juste après le dernier */
    f->t[fin] = x;
    f->taille++;
    return 1;
}

int defiler(File *f, int *x) {
    if (est_vide(f)) return 0;
    *x = f->t[f->debut];
    f->debut = (f->debut + 1) % MAX;          /* l'avant avance d'une case, en boucle */
    f->taille--;
    return 1;
}

int main(void) {
    File f;
    int x;
    init(&f);
    for (int i = 1; i <= 5; i++) enfiler(&f, i * 10);   /* 10 20 30 40 50 : pleine */
    defiler(&f, &x);                                    /* sort 10 */
    defiler(&f, &x);                                    /* sort 20 */
    enfiler(&f, 60);                                    /* va dans la case 0 */
    enfiler(&f, 70);                                    /* va dans la case 1 */
    while (defiler(&f, &x))
        printf("%d ", x);                               /* affiche 30 40 50 60 70 */
    printf("\n");
    return 0;
}
```

Garder la **taille** plutôt que l'indice de fin évite le cas ambigu où `debut == fin` pourrait vouloir dire « vide » ou « pleine ».

## Version 2 : avec une liste chaînée

On garde deux pointeurs : **tete** (l'avant, où l'on retire) et **queue** (l'arrière, où l'on ajoute). Grâce au pointeur de queue, l'ajout reste en O(1).

```
  tete                       queue
   |                           |
   v                           v
 [ A ] --> [ B ] --> [ C ] --> [ D ] --> NULL
```

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Noeud {
    int valeur;
    struct Noeud *next;
} Noeud;

typedef struct {
    Noeud *tete;     /* on retire ici */
    Noeud *queue;    /* on ajoute ici */
} FileL;

void init_l(FileL *f) { f->tete = f->queue = NULL; }

int enfiler_l(FileL *f, int x) {
    Noeud *n = malloc(sizeof(Noeud));
    if (n == NULL) return 0;
    n->valeur = x;
    n->next = NULL;
    if (f->queue == NULL)           /* file vide : le nœud est à la fois tête et queue */
        f->tete = n;
    else
        f->queue->next = n;
    f->queue = n;
    return 1;
}

int defiler_l(FileL *f, int *x) {
    if (f->tete == NULL) return 0;
    Noeud *avant = f->tete;
    *x = avant->valeur;
    f->tete = avant->next;
    if (f->tete == NULL)            /* on vient de retirer le dernier élément */
        f->queue = NULL;
    free(avant);
    return 1;
}
```

Le piège le plus courant : oublier de remettre `queue` à `NULL` quand la file se vide. Le prochain `enfiler` écrirait alors dans un nœud déjà libéré.

Une version complète avec des chaînes (`init`, `enqueue`, `dequeue`, `front`, `size`, `clear`) est dans le TP3 : [file avec liste chaînée](../tp/tp3/ex1-file-liste-chainee.c).

## Les cousines de la file

- **File à double entrée** (*deque*) : on peut ajouter et retirer aux deux bouts. Elle peut servir de pile comme de file.
- **File de priorité** : on retire toujours l'élément le plus prioritaire, pas le plus ancien (les urgences d'un hôpital). On l'implémente en général avec un **tas** (*heap*).

## LIFO contre FIFO

Le même scénario dans les deux structures : on ajoute A, puis B, puis C, puis on retire tout.

```
 Pile (LIFO)                      File (FIFO)

 ajout   A, B, C                  ajout   A, B, C
 +---+
 | C | <- sommet                  avant -> [A] [B] [C] <- arrière
 | B |
 | A |
 +---+
 sortie : C, B, A                 sortie : A, B, C
```

| | Pile (LIFO) | File (FIFO) |
|---|---|---|
| Principe | dernier entré, premier sorti | premier entré, premier sorti |
| Ajout | au sommet | à l'arrière |
| Retrait | au sommet | à l'avant |
| Bouts utilisés | un seul | deux |
| Avec un tableau | un indice `sommet` | `debut` et `taille`, avec modulo |
| Avec une liste | un pointeur (la tête) | deux pointeurs (tête et queue) |
| Coût des opérations | O(1) | O(1) |
| Exemples | Ctrl+Z, bouton Retour, appels de fonctions, parenthèses | imprimante, requêtes, tampons, BFS |

**Comment choisir ?** Pose-toi la question : « est-ce que je dois traiter d'abord le **plus récent** ou le **plus ancien** ? »

- Le plus récent (revenir en arrière, finir ce qu'on vient de commencer) : **pile**.
- Le plus ancien (respecter l'ordre d'arrivée, être équitable) : **file**.

## À retenir

- File = FIFO : on ajoute à l'arrière, on retire à l'avant.
- Avec un tableau, on utilise le modulo pour réutiliser les cases (tableau circulaire).
- Avec une liste, on garde un pointeur sur la tête **et** sur la queue.
- Pile et file font tout en O(1) ; seul l'ordre de sortie change.

## Pour aller plus loin (en anglais)

- [FIFO (First In First Out) approach in programming](https://www.geeksforgeeks.org/dsa/fifo-first-in-first-out-approach-in-programming/), GeeksforGeeks
- [Queue data structure](https://www.geeksforgeeks.org/dsa/queue-data-structure/), GeeksforGeeks
- [Queue in C](https://www.geeksforgeeks.org/c/queue-in-c/), GeeksforGeeks
- [FIFO vs LIFO approach in programming](https://www.geeksforgeeks.org/dsa/fifo-vs-lifo-approach-in-programming/), GeeksforGeeks
- [LIFO vs FIFO: mastering stacks and queues in C](https://medium.com/@edwinsanjosoji/lifo-vs-fifo-mastering-stacks-and-queues-in-c-4cfc58b8b17a), Medium
- [Understanding queues: mastering the FIFO principle in JavaScript](https://dev.to/gr8soln/understanding-queues-data-structure-mastering-fifo-principle-in-javascript-8di), DEV : la même idée dans un autre langage.

---
title: "Piles (LIFO)"
date: 2025-10-20
author: CHOUBIK Houssam
tags: [dsa, cs2c, pile, lifo]
---

# Piles : LIFO

## L'idée

Pense à une pile d'assiettes. On pose une assiette **sur le dessus**, et on reprend toujours **celle du dessus**. La dernière posée est la première reprise.

C'est le principe **LIFO** : *Last In, First Out*, dernier entré, premier sorti.

```
 empiler 1, 2, 3            dépiler
                              3  <-- sort en premier
   +---+                    +---+
   | 3 |  <-- sommet        | 2 |  <-- nouveau sommet
   +---+                    +---+
   | 2 |                    | 1 |
   +---+                    +---+
   | 1 |
   +---+
```

On ne touche **jamais** au milieu ni au fond : tout se passe au sommet.

## Où on en croise dans la vraie vie

- **Ctrl+Z** dans un éditeur : on annule d'abord la dernière action faite.
- **Le bouton Retour** du navigateur : on revient à la dernière page visitée.
- **Les appels de fonctions** : quand `main` appelle `f`, qui appelle `g`, le programme doit finir `g` avant de revenir dans `f`, puis dans `main`. Le C range ces appels dans la **pile d'appels** (*call stack*). Une récursion sans fin la remplit : c'est le fameux *stack overflow*.
- **Vérifier les parenthèses** d'une expression, ou **évaluer une expression postfixée** (voir plus bas).

## Les opérations

| Opération | Rôle | Coût |
|---|---|---|
| `empiler(x)` (*push*) | Pose x au sommet | O(1) |
| `depiler()` (*pop*) | Retire et renvoie le sommet | O(1) |
| `sommet()` (*peek*, *top*) | Renvoie le sommet sans le retirer | O(1) |
| `est_vide()` | La pile est-elle vide ? | O(1) |

Deux erreurs à prévoir :

- **dépiler une pile vide** (*underflow*) ;
- **empiler sur une pile pleine** (*overflow*), seulement avec un tableau de taille fixe.

## Version 1 : avec un tableau

On garde un tableau et l'indice du sommet. Pile vide : `sommet = -1`.

```
 indice :   0    1    2    3    4
          +----+----+----+----+----+
 t :      |  1 |  2 |  3 |    |    |
          +----+----+----+----+----+
                      ^
                   sommet = 2
```

```c
#include <stdio.h>

#define MAX 100

typedef struct {
    int t[MAX];
    int sommet;      /* indice du dernier élément, -1 si vide */
} Pile;

void init(Pile *p)             { p->sommet = -1; }
int est_vide(const Pile *p)    { return p->sommet == -1; }
int est_pleine(const Pile *p)  { return p->sommet == MAX - 1; }

int empiler(Pile *p, int x) {
    if (est_pleine(p)) return 0;        /* overflow */
    p->t[++p->sommet] = x;              /* on avance le sommet, puis on écrit */
    return 1;
}

int depiler(Pile *p, int *x) {
    if (est_vide(p)) return 0;          /* underflow */
    *x = p->t[p->sommet--];             /* on lit, puis on recule le sommet */
    return 1;
}

int main(void) {
    Pile p;
    int x;
    init(&p);
    empiler(&p, 1);
    empiler(&p, 2);
    empiler(&p, 3);
    while (depiler(&p, &x))
        printf("%d ", x);               /* affiche 3 2 1 */
    printf("\n");
    return 0;
}
```

Les fonctions renvoient 1 si tout va bien et 0 en cas d'erreur, et la valeur dépilée passe par un pointeur. Comme ça, l'appelant voit tout de suite si la pile était vide.

## Version 2 : avec une liste chaînée

Plus de limite de taille. Le sommet est la **tête** de la liste : empiler, c'est insérer en tête ; dépiler, c'est retirer la tête. Les deux sont en O(1).

```
 sommet
   |
   v
 [ 3 ] --> [ 2 ] --> [ 1 ] --> NULL
```

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Noeud {
    int valeur;
    struct Noeud *next;
} Noeud;

typedef struct {
    Noeud *sommet;
} PileL;

int empiler_l(PileL *p, int x) {
    Noeud *n = malloc(sizeof(Noeud));
    if (n == NULL) return 0;
    n->valeur = x;
    n->next = p->sommet;        /* le nouveau nœud pointe sur l'ancien sommet */
    p->sommet = n;
    return 1;
}

int depiler_l(PileL *p, int *x) {
    if (p->sommet == NULL) return 0;
    Noeud *haut = p->sommet;
    *x = haut->valeur;
    p->sommet = haut->next;
    free(haut);
    return 1;
}
```

| | Tableau | Liste chaînée |
|---|---|---|
| Taille | fixée à l'avance | illimitée (tant qu'il y a de la mémoire) |
| Mémoire | rien en plus | un pointeur par élément |
| Vitesse | très rapide | un `malloc` à chaque empilement |

## Exemple 1 : les parenthèses sont-elles bien équilibrées ?

On lit l'expression de gauche à droite. À chaque ouvrante, on l'empile. À chaque fermante, le sommet doit être l'ouvrante qui va avec. À la fin, la pile doit être vide.

```
 "( [ ] )"
  (      pile : (
  [      pile : ( [
  ]      sommet [ correspond  -> pile : (
  )      sommet ( correspond  -> pile vide   => équilibrée
```

```c
int equilibree(const char *s) {
    char pile[100];
    int h = -1;
    for (; *s; s++) {
        if (*s == '(' || *s == '[' || *s == '{') {
            if (h == 99) return 0;          /* trop d'imbrications pour ce tableau */
            pile[++h] = *s;
        } else if (*s == ')' || *s == ']' || *s == '}') {
            if (h == -1) return 0;          /* fermante sans ouvrante */
            char o = pile[h--];
            if ((*s == ')' && o != '(') || (*s == ']' && o != '[') || (*s == '}' && o != '{'))
                return 0;
        }
    }
    return h == -1;                         /* il ne doit rien rester */
}
```

`equilibree("{[()]}")` vaut 1, `equilibree("([)]")` vaut 0.

## Exemple 2 : évaluer une expression postfixée

En notation postfixée, l'opérateur vient **après** ses deux nombres, donc plus besoin de parenthèses : `(3 + 4) * 2` s'écrit `3 4 + 2 *`.

```
 lu    action                      pile
 3     empiler                     3
 4     empiler                     3 4
 +     dépiler 4 et 3, 3+4=7       7
 2     empiler                     7 2
 *     dépiler 2 et 7, 7*2=14      14      => résultat 14
```

Le corrigé complet est dans l'examen de TP : [ex3 : pile et expression postfixée](../examens/exam-tp/ex3-pile-expression-postfixee.c).

## À retenir

- Pile = LIFO : on ajoute et on retire **au même bout**, le sommet.
- Toutes les opérations sont en O(1).
- Toujours tester la pile vide avant de dépiler.
- Le sommet d'une pile chaînée est la tête de la liste.

Suite : [Files (FIFO), et LIFO contre FIFO](04-files-fifo.md).

## Pour aller plus loin (en anglais)

- [LIFO vs FIFO: mastering stacks and queues in C](https://medium.com/@edwinsanjosoji/lifo-vs-fifo-mastering-stacks-and-queues-in-c-4cfc58b8b17a), Medium
- [FIFO vs LIFO approach in programming](https://www.geeksforgeeks.org/dsa/fifo-vs-lifo-approach-in-programming/), GeeksforGeeks

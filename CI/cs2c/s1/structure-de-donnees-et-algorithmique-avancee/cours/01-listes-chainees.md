---
title: "Listes chaînées"
date: 2025-09-26
author: CHOUBIK Houssam
tags: [dsa, cs2c]
---

# Listes chaînées

## Pourquoi pas un tableau ?

Un tableau a une taille fixe, et ses cases se suivent en mémoire. Insérer une valeur au début oblige à décaler toutes les autres.

Une **liste chaînée** règle ces deux problèmes. Chaque élément, appelé **nœud**, est créé avec `malloc` quand on en a besoin, n'importe où en mémoire. Les nœuds sont reliés par des pointeurs, comme les wagons d'un train par leurs attaches.

Chaque nœud contient :

- une **donnée** (un entier, un nom, une `struct`...) ;
- un pointeur **next** vers le nœud suivant.

On garde l'adresse du premier nœud dans un pointeur appelé **tête** (*head*). Le dernier nœud a `next = NULL` : c'est la fin de la liste.

```
 tete
  |
  v
+----+---+    +----+---+    +----+------+
| 10 | o-+--->| 20 | o-+--->| 30 | NULL |
+----+---+    +----+---+    +----+------+
```

Un nœud en C, c'est une `struct` qui contient un pointeur vers son propre type (une *structure autoréférente*) :

```c
typedef struct Noeud {
    int valeur;
    struct Noeud *next;
} Noeud;
```

## Les opérations

### Créer un nœud

```c
Noeud *creer(int v) {
    Noeud *n = malloc(sizeof(Noeud));
    if (n == NULL) return NULL;
    n->valeur = v;
    n->next = NULL;
    return n;
}
```

### Insérer en tête : O(1)

Le nouveau nœud pointe sur l'ancienne tête, puis il devient la tête.

```
avant :          tete --> [10] --> [20] --> NULL
nouveau nœud :   [5]
après :          tete --> [5] --> [10] --> [20] --> NULL
```

```c
Noeud *inserer_tete(Noeud *tete, int v) {
    Noeud *n = creer(v);
    if (n == NULL) return tete;
    n->next = tete;
    return n;           /* la nouvelle tête */
}
```

Utilisation : `tete = inserer_tete(tete, 5);`

### Insérer en queue : O(n)

Il faut parcourir la liste jusqu'au dernier nœud.

```c
Noeud *inserer_queue(Noeud *tete, int v) {
    Noeud *n = creer(v);
    if (n == NULL) return tete;
    if (tete == NULL) return n;     /* liste vide : le nœud devient la tête */
    Noeud *p = tete;
    while (p->next != NULL)
        p = p->next;
    p->next = n;
    return tete;
}
```

Si l'on garde aussi un pointeur sur le dernier nœud (la **queue**, *tail*), cette insertion passe en O(1). C'est exactement ce que fait une file, voir [Files (FIFO)](04-files-fifo.md).

### Parcourir et afficher : O(n)

```c
void afficher(Noeud *tete) {
    for (Noeud *p = tete; p != NULL; p = p->next)
        printf("%d -> ", p->valeur);
    printf("NULL\n");
}
```

### Supprimer une valeur : O(n)

On cherche le nœud, on le « court-circuite », puis on le libère.

```
supprimer 20 :
tete --> [10] --> [20] --> [30] --> NULL
           |                ^
           +----------------+        10 pointe maintenant sur 30, puis free(20)
```

```c
Noeud *supprimer(Noeud *tete, int v) {
    if (tete == NULL) return NULL;
    if (tete->valeur == v) {          /* cas particulier : c'est la tête */
        Noeud *suite = tete->next;
        free(tete);
        return suite;
    }
    Noeud *p = tete;
    while (p->next != NULL && p->next->valeur != v)
        p = p->next;
    if (p->next != NULL) {            /* trouvé : p est juste avant */
        Noeud *cible = p->next;
        p->next = cible->next;
        free(cible);
    }
    return tete;
}
```

### Tout libérer

```c
void liberer(Noeud *tete) {
    while (tete != NULL) {
        Noeud *suite = tete->next;   /* on garde la suite avant le free */
        free(tete);
        tete = suite;
    }
}
```

Erreur classique : écrire `free(p); p = p->next;`. Une fois `p` libéré, on n'a plus le droit de lire `p->next`.

## Les autres types de listes

### Liste doublement chaînée

Chaque nœud connaît aussi le précédent (`prev`). On peut parcourir dans les deux sens et supprimer un nœud sans chercher celui d'avant, au prix d'un pointeur de plus par nœud.

```
         +------+----+------+     +------+----+------+     +------+----+------+
NULL <---| prev | 10 | next |<--->| prev | 20 | next |<--->| prev | 30 | next |---> NULL
         +------+----+------+     +------+----+------+     +------+----+------+
```

```c
typedef struct NoeudD {
    int valeur;
    struct NoeudD *prev;
    struct NoeudD *next;
} NoeudD;
```

Exemple concret : l'historique d'un navigateur (page précédente, page suivante).

### Liste circulaire

Le dernier nœud pointe sur le premier au lieu de `NULL`. Pratique pour tourner en boucle, par exemple pour donner la main à chaque joueur à tour de rôle.

```
   +---------------------------------+
   v                                 |
 [10] --> [20] --> [30] -------------+
```

Attention : pour la parcourir, on s'arrête quand on **revient au départ**, pas sur `NULL`, sinon la boucle ne s'arrête jamais.

## Tableau ou liste ?

| Opération | Tableau | Liste simplement chaînée |
|---|---|---|
| Lire le i-ème élément | O(1) | O(n) |
| Insérer en tête | O(n) (tout décaler) | O(1) |
| Insérer en queue | O(1) s'il reste de la place | O(n), ou O(1) avec un pointeur de queue |
| Supprimer une valeur | O(n) | O(n) |
| Taille | fixe | grandit à la demande |
| Mémoire en plus | aucune | un pointeur par nœud |

En résumé : le tableau est imbattable pour l'accès direct, la liste pour les insertions et suppressions fréquentes en début de liste.

Les exercices sont dans [Listes chaînées : exercices](02-listes-chainees-exercices.md) et dans [exercices/](../exercices/).

/*
 * Examen TP DSA, exercice 1 : listes chaînées
 *
 * On considère la structure de liste chaînée suivante :
 *
 *   typedef struct cel {
 *       float val;
 *       struct cel *suiv;
 *   } cellule;
 *
 * 1. Implémenter void rotation(cellule **L, int n) qui déplace les n premiers
 *    éléments d'une liste simplement chaînée à la fin de cette liste
 *    (sans créer de nouvelles cellules).
 * 2. Implémenter void substr(cellule **L, cellule *M) qui supprime tous les
 *    éléments de la liste L qui se trouvent dans la liste M.
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct cel {
    float val;
    struct cel *suiv;
} cellule;

/* 1. Rotation */
void rotation(cellule **L, int n) {
    if (*L == NULL || n <= 0) return;

    cellule *fin = *L;
    int longueur = 1;
    while (fin->suiv != NULL) {
        fin = fin->suiv;
        longueur++;
    }
    if (n >= longueur) return;

    /* temp = n-ième cellule, elle devient la dernière */
    cellule *temp = *L;
    for (int i = 1; i < n; i++)
        temp = temp->suiv;

    fin->suiv = *L;
    *L = temp->suiv;
    temp->suiv = NULL;
}

/* 2. Supprimer de L les valeurs présentes dans M */
int verifier(cellule *M, float val) {
    while (M) {
        if (M->val == val) return 1;
        M = M->suiv;
    }
    return 0;
}

void substr(cellule **L, cellule *M) {
    cellule *curr = *L;
    cellule *prec = NULL;
    while (curr) {
        if (verifier(M, curr->val)) {
            cellule *suppr = curr;
            if (prec == NULL)
                *L = curr->suiv;
            else
                prec->suiv = curr->suiv;
            curr = curr->suiv;
            free(suppr);
        } else {
            prec = curr;
            curr = curr->suiv;
        }
    }
}

/* Outils pour tester */
void ajouter_fin(cellule **L, float val) {
    cellule *c = malloc(sizeof(cellule));
    c->val = val;
    c->suiv = NULL;
    if (*L == NULL) {
        *L = c;
        return;
    }
    cellule *p = *L;
    while (p->suiv) p = p->suiv;
    p->suiv = c;
}

void afficher(cellule *L) {
    while (L) {
        printf("%g ", L->val);
        L = L->suiv;
    }
    printf("\n");
}

void liberer(cellule *L) {
    while (L) {
        cellule *s = L->suiv;
        free(L);
        L = s;
    }
}

int main(void) {
    cellule *L = NULL, *M = NULL;
    for (int i = 1; i <= 6; i++) ajouter_fin(&L, i);

    rotation(&L, 2);
    afficher(L); /* 3 4 5 6 1 2 */

    ajouter_fin(&M, 4);
    ajouter_fin(&M, 1);
    substr(&L, M);
    afficher(L); /* 3 5 6 2 */

    liberer(L);
    liberer(M);
    return 0;
}

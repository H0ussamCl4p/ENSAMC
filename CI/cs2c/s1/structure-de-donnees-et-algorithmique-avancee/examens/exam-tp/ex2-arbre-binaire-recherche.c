/*
 * Examen TP DSA, exercice 2 : arbre binaire de recherche
 *
 *   typedef struct ABR {
 *       int val;
 *       struct ABR *FD; // fils droit
 *       struct ABR *FG; // fils gauche
 *   } arbre;
 *
 * Écrire les fonctions qui :
 * 1. retournent la taille d'un arbre ;
 * 2. retournent la valeur maximale d'un arbre ;
 * 3. calculent la somme des valeurs des nœuds ;
 * 4. calculent la hauteur de la branche la plus courte ;
 * 5. retournent le nombre de feuilles.
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct ABR {
    int val;
    struct ABR *FD;
    struct ABR *FG;
} arbre;

/* 1. Taille */
int taille(arbre *root) {
    if (root == NULL) return 0;
    return 1 + taille(root->FD) + taille(root->FG);
}

/* 2. Maximum : dans un ABR c'est le nœud le plus à droite.
 * L'arbre ne doit pas être vide. */
int max(arbre *root) {
    while (root->FD != NULL)
        root = root->FD;
    return root->val;
}

/* 3. Somme */
int somme(arbre *root) {
    if (root == NULL) return 0;
    return root->val + somme(root->FD) + somme(root->FG);
}

/* 4. Hauteur de la branche la plus courte (jusqu'à une feuille) */
int min_hauteur(arbre *root) {
    if (root == NULL) return 0;
    if (root->FD == NULL) return 1 + min_hauteur(root->FG);
    if (root->FG == NULL) return 1 + min_hauteur(root->FD);
    int d = min_hauteur(root->FD);
    int g = min_hauteur(root->FG);
    return 1 + (d < g ? d : g);
}

/* 5. Nombre de feuilles */
int nb_feuilles(arbre *root) {
    if (root == NULL) return 0;
    if (root->FD == NULL && root->FG == NULL) return 1;
    return nb_feuilles(root->FD) + nb_feuilles(root->FG);
}

/* Outils pour tester */
arbre *inserer(arbre *root, int val) {
    if (root == NULL) {
        arbre *n = malloc(sizeof(arbre));
        n->val = val;
        n->FD = n->FG = NULL;
        return n;
    }
    if (val < root->val)
        root->FG = inserer(root->FG, val);
    else
        root->FD = inserer(root->FD, val);
    return root;
}

void liberer(arbre *root) {
    if (root == NULL) return;
    liberer(root->FG);
    liberer(root->FD);
    free(root);
}

int main(void) {
    int valeurs[] = {8, 3, 10, 1, 6, 14, 4, 7, 13};
    arbre *root = NULL;
    for (int i = 0; i < 9; i++)
        root = inserer(root, valeurs[i]);

    printf("taille      : %d\n", taille(root));      /* 9 */
    printf("max         : %d\n", max(root));         /* 14 */
    printf("somme       : %d\n", somme(root));       /* 66 */
    printf("min hauteur : %d\n", min_hauteur(root)); /* 3 */
    printf("feuilles    : %d\n", nb_feuilles(root)); /* 4 */

    liberer(root);
    return 0;
}

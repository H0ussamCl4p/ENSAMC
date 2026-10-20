#include <stdio.h>
#include <stdlib.h>

#define max 50

int main() {
    int A[max], n, i, VAL, POS = -1;
    printf("Veuillez saisir la taille du tableau (entre 1 et 50) :\n");
    scanf("%d", &n);
    while (n <= 0 || n > max) {
        printf("Erreur : la taille doit etre comprise entre 1 et 50 !\n");
        scanf("%d", &n);
    }
    printf("Veuillez saisir les elements du tableau :\n");
    for (i = 0; i < n; i++) {
        printf("Element %d : ", i + 1);
        scanf("%d", &A[i]);
    }
    printf("Entrez la valeur a rechercher : ");
    scanf("%d", &VAL);
    for (i = 0; i < n; i++) {
        if (A[i] == VAL) {
            POS = i;
            break;
        }
    }
    if (POS == -1) {
        printf("La valeur %d n'a pas ete trouvee dans le tableau.\n", VAL);
    } else {
        printf("La valeur %d a ete trouvee à la position %d (indice %d).\n", VAL, POS + 1, POS);
    }

    return 0;
}

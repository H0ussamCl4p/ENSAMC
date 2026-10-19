#include <stdio.h>
#define max 100

int main() {
    int A[max];
    int n, X;
    int *P1, *P2;
    printf("Veuillez saisir la taille du tableau : ");
    scanf("%d", &n);
    printf("Entrez les elements du tableau :\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", A + i);
    }
    printf("Entrez l'entier a supprimer (X) : ");
    scanf("%d", &X);
    P1 = A;
    P2 = A;
    for (int i = 0; i < n; i++, P1++) {
        if (*P1 != X) {
            *P2 = *P1;
            P2++;
        }
    }
    int nouvelle_taille = P2 - A;
    printf("Tableau apres la suppression de %d :\n", X);
    for (int i = 0; i < nouvelle_taille; i++) {
        printf("%d ", *(A + i));
    }
    printf("\n");
    return 0;
}

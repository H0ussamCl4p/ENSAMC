#include <stdio.h>
#define max 200
int main() {
    int n, m, i, T1[max],T2[max];
    int *p1 = T1;
    int *p2 = T2;
    do {
        printf("Entrez la taille de T1 : ");
        scanf("%d", &n);
        printf("Entrez la taille de T2 : ");
        scanf("%d", &m);
        if (n + m > max) {
            printf("Erreur : la taille totale depasse la limite autorisee (%d).\n", max);
        }
    } while (n + m > max);
    printf("Entrez les elements du tableau T1 :\n");
    for (i=0; i<n; i++) {
        scanf("%d", p1 + i);
    }
    printf("Entrez les elements du tableau T2 :\n");
    for (i=0; i<m; i++) {
        scanf("%d", p2 + i);
    }
    for (i = 0; i < m; i++) {
        *(p1+n+i) = *(p2+i);
    }
    printf("Tableau T1 apres ajout de T2 :\n");
    for (i = 0; i<n+m; i++) {
        printf("%d ", *(p1 + i));
    }
    printf("\n");
    return 0;
}

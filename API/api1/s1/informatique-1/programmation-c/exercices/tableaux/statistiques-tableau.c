/*
 * Saisir un tableau, afficher sa moyenne, chercher une valeur et afficher les éléments pairs.
 */

#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int main() {
    int i, s = 0, compt = 0, x, n;
    int T[MAX];

    printf("Saisir la taille du tableau : ");
    scanf("%d", &n);

    // Saisie des éléments
    for(i = 0; i < n; i++) {
        printf("Élément %d : ", i + 1);
        scanf("%d", &T[i]);
        s += T[i];
    }

    // Affichage des éléments
    printf("Les éléments du tableau sont :\n");
    for(i = 0; i < n; i++) {
        printf("T[%d] = %d\n", i, T[i]);
    }

    // Calcul de la moyenne
    float moy = (float)s / n;
    printf("La moyenne est : %.2f\n", moy);

    // Recherche d'une valeur
    printf("Entrer la valeur à chercher : ");
    scanf("%d", &x);

    compt = 0;
    for(i = 0; i < n; i++) {
        if(T[i] == x) {
            printf("Valeur trouvée à la position %d\n", i + 1);
            compt++;
        }
    }

    if(compt == 0) {
        printf("Valeur non trouvée.\n");
    } else {
        printf("Nombre d'occurrences : %d\n", compt);
    }

    // Affichage des éléments pairs
    printf("Les éléments pairs sont :\n");
    for(i = 0; i < n; i++) {
        if(T[i] % 2 == 0) {
            printf("%d\n", T[i]);
        }
    }

    return 0;
}

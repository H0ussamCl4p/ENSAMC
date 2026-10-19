/*
 * Afficher les n premiers nombres premiers.
 */

#include <stdio.h>
#include <stdlib.h>

int premier(int n) {
    int i;
    if (n < 2) return 0;
    for (i=2;i*i<= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}
void afficher(int n){
    int  i = 2, compteur = 0;
    while (compteur < n) {
        if (premier(i)) {
            printf("%d ", i);
            compteur++;
        }
        i++;
    }
}

int main() {
    int n;
    printf("Veuillez saisir le nombre de nbr premiers:\n");
    scanf("%d",&n);
    afficher(n);
    return 0;
}

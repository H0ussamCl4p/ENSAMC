#include <stdio.h>
#include <math.h>

int main() {
    int n;
    printf("Entrez un entier n : ");
    scanf("%d", &n);
    if (n < 0) {
        printf("Un carre parfait ne peut pas être négatif.\n");
    }
    int racine = sqrt(n);
    if (racine * racine == n) {
        printf("%d est un carré parfait.\n", n);
    } else {
        printf("%d n'est pas un carré parfait.\n", n);
    }
    return 0;
}

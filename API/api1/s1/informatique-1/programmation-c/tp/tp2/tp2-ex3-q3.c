#include <stdio.h>

int main() {
    int n, m;
    float s,p ;
    printf("Entrez la valeur de n : ");
    scanf("%d", &n);
    printf("Entrez la valeur de m : ");
    scanf("%d", &m);
    p = 1.0;
    s = 0.0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            s = s + (float)(j + i) / (i * j);
        }
        p = p * s;
    }
    printf("Le produit est : %f\n", p);
    return 0;
}

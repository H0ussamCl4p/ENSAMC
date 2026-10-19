#include <stdio.h>

int main() {
    int n, p, fp, fn, fnp, i, comb;

    printf("Veuillez saisir la valeur de n et p :\n");
    do {
        scanf("%d %d", &n, &p);
        if (n < p) {
            printf("Il faut que n >= p. Veuillez ressaisir n et p :\n");
        }
    } while (n < p);

    fn = 1;
    fp = 1;
    fnp = 1;
    for (i = 1; i <= n; i++) {
        fn = fn * i;
    }
    for (i = 1; i <= p; i++) {
        fp = fp*i;
    }
    for (i = 1; i <= (n - p); i++) {
        fnp = fnp*i;
    }
    comb = fn / (fp * fnp);
    printf("La combinaison est C = %d \n",comb);
    return 0;
}

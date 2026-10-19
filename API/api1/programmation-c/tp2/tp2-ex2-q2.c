#include <stdio.h>

int main()
{
    int n, i, u, u0, u1;
    printf("Veuillez saisir la valeur de n:\n");
    scanf("%d", &n);
    u0 = 0;
    u1 = 1;
    if (n == 0) {
        u = u0;
    } else if (n == 1) {
        u = u1;
    } else {
        for (i = 1; i <= n; i++) {
            u = 6 * u1 - 9 * u0;
            u0 = u1;
            u1 = u;
        }
    }
    printf("La valeur de la suite u = 6 * u1 - 9 * u0 pour n = %d est %d\n", n, u);
    return 0;
}

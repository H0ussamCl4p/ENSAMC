#include <stdio.h>

int main() {
    int n, i, u;
    printf("Veuillez saisir la valeur de n:\n");
    scanf("%d", &n);
    u = 4;
    if (n % 2 == 0) {
        for (i = 1; i <= n; i++) {
            u = u / 2;
        }
    } else {
        for (i = 1; i <= n; i++) {
            u = (u + 1) / 2;
        }
    }
    printf("La valeur de u pour n = %d est %d\n", n, u);
    return 0;
}

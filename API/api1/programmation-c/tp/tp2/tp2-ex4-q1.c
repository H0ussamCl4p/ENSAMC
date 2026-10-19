#include <stdio.h>

int main() {
    int n;
    printf("Veuillez saisir un entier n : ");
    scanf("%d", &n);
    printf("Les diviseurs de %d sont : ", n);
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}

#include <stdio.h>

int main() {
    int n, premier = 1;
    printf("Veuillez saisir un entier n : ");
    scanf("%d", &n);
    if (n <= 1) {
        printf("%d n'est pas un nombre premier.\n", n);
    }
    premier = 1;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            premier = 0;
            break;
        }
    }
    if (premier) {
        printf("%d est un nombre premier.\n", n);
    } else {
        printf("%d n'est pas un nombre premier.\n", n);
    }

    return 0;
}

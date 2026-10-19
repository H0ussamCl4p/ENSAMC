#include <stdio.h>

int main() {
    int i,j,p ;
    printf("Table de multiplication (1 a 9):\n");
    for (i = 1; i<=9; i++) {
        for (j = 1; j<=9; j++) {
            p = i*j ;
            printf("%2d ", p);
        }
        printf("\n");
    }
    return 0;
}

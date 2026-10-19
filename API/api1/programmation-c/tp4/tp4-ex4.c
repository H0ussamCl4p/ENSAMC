#include <stdio.h>
#include <stdlib.h>
#define taille_max 100

int main()
{
    int A[] = {12, 23, 34, 45, 56, 67, 78, 89, 90};
    int *P;
    P = A;
    int a = *P+2;
    int b = *(P+2);
    int c = &P+1;
    int d = &A[4]-3;
    int e = A+3;
    int f = &A[7]-P;
    int g = P+(*P-10);
    int h = (P+*(P+8)-A[7]);
    printf("%d",h);
    return 0;
}



#include <stdio.h>

int main()
{
    int n,inv,r,i ;
    printf("Veuillez saisir un entier :\n");
    scanf("%d",&n);
    while (n!=0) {
        r = n%10 ;
        n = n/10 ;
        inv = inv*10+r ;
    }
    printf("L'inverse de l'entier saisit est %d", inv);
    return 0;
}

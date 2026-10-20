#include <stdio.h>

int main()
{
    int n,i,u ;
    printf("Veuillez saisir la valeur de n:\n");
    scanf("%d",&n);
    u = 1;
    for (i=1;i<=n;i++) {
        u = 6*u+4;
    }
    printf("La valeur de la suite Un=6Un-1+4 est %d",u);
    return 0;
}

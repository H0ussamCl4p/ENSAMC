#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,comp,num ;
    printf("Veuillez saisir un entier :\n");
    scanf("%d",&num);
    n=num ;
    comp = 0;
    while (n!=0) {
        n = n/10 ;
        comp = comp + 1;
    }
    printf("Le nombre de chiffre de l'entier %d que vous avez introduit est : %d",num,comp);
    return 0;
}

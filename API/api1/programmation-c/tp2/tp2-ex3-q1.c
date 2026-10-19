#include <stdio.h>

int main()
{
    int n,i,s ;
    printf("Veuillez saisir un entier :\n");
    scanf("%d",&n);
    s=0;
    for (i=1;i<=n;i++) {
        s = s + i*i;
    }
    printf("La serie vaut : %d",s);
    return 0;
}

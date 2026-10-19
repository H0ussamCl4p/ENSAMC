#include <stdio.h>

int main()
{
    int a,b,c,s,i;
    printf("Veuillez saisir deux entiers :\n");
    scanf("%d %d",&a,&b);
    if (a>b) {
        c = a ;
        a = b ;
        b = c ;
    }
    s = 0;
    for (i = a;i<=b;i++) {
        s = s + i;
    }
    printf("La somme entre les entiers %d et %d est S = %d",a,b,s);
    return 0;
}

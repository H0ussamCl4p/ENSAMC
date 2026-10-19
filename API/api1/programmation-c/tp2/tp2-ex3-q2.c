#include <stdio.h>

int main()
{
    int n,m,i,j ;
    float s ;
    printf("Veuillez saisir un entier n:\n");
    scanf("%d",&n);
    printf("Veuillez saisir un entier m:\n");
    scanf("%d",&m);
    s = 0.0;
    for(i=1;i<=n;i++) {
        for (j=0;j<=m;j++) {
            s = s + 1.0/(i+j);
        }
    }
    printf("La valeur de la serie est : %f",s);
    return 0;
}

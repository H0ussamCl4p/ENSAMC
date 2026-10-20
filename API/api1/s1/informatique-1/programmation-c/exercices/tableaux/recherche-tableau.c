/*
 * Chercher une valeur dans un tableau (retourne 1 si trouvée, 0 sinon).
 */

#include <stdio.h>
#include <stdlib.h>
#define taille_max 100
int recherche(int T[],int n,int x)
{
    int i;
    for(i=0;i<n;i++){
        if(x==T[i]){
            return 1;
        }
    }
    return 0;
}


int main()
{
    int i,n,x,T[taille_max];
    printf("Taille du tableau : ");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&T[i]);
    }
    printf("Valeur a chercher : ");
    scanf("%d",&x);
    printf("%d\n",recherche(T,n,x));
    return 0;
}

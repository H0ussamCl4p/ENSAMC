/* Réalisé par  Choubik Houssam */

/* TP4 Exercice 1 */


#include <stdio.h>
#include <stdlib.h>
#define max 50

int main()
{
    int T[max],n,i,somme ;
    printf("Veuillez saisir la taille du tableau :\n");
    scanf("%d",&n);
    while (n>50 || n<0) {
        printf("La taille du tableau doit etre comprise entre 50 et 0 ! \n");
        scanf("%d",&n);
    }
    printf("Veuillez saisir les elements du tableau :\n");
    somme = 0;
    for(i=0;i<n;i++) {
        printf("Element %d \n",i+1);
        scanf("%d",&T[i]);
        somme = somme + T[i];
    }
    printf("Voici les elements du tableau :\n");
    for(i=0;i<n;i++) {
        printf("%d",T[i]);
        printf(" ");
    }
    printf("\n");
    printf("La somme des elements du tableau est %d :\n",somme);

    return 0;
}

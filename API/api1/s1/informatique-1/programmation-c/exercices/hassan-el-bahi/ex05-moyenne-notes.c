/*
 * Exercice de la série de Hassan El Bahi, n°5
 * Calculer la moyenne de n notes.
 */

#include <stdio.h>

int main(){
    float tab [100];
    int i,n;
    printf("Veuillez saisir le nombre de notes : ");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        printf("La note %d : ",i+1);
        scanf("%f",&tab[i]);
    }
    float somme=0;
    for(i=0;i<n;i++){
        somme+=tab[i];
    }
    float moyenne=somme/n;
    printf("La moyenne est : %f\n",moyenne);
    return 0;
}

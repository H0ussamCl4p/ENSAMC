/*
 * Exercice de la série de Hassan El Bahi, n°2
 * Lire la largeur et la longueur d'un rectangle, afficher son périmètre et son aire.
 */

#include <stdio.h>

float perimetre(float lar, float lon)
{
    return 2*(lar+lon);
}

float aire(float lar, float lon){
    return lar*lon;
}

int main(){
    float l,L;
    printf("Veuillez saisir la largeur et longuer du rectangle : \n");
    printf("largeur : ");
    scanf("%f",&l);     
    printf("longuer : ");
    scanf("%f",&L);
    printf("Le perimetre du rectangle est : %f\n",perimetre(l,L));  
    printf("L'aire du rectangle est : %f\n",aire(l,L));
    return 0;
}

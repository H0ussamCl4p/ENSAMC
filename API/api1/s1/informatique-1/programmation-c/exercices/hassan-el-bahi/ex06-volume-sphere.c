/*
 * Exercice de la série de Hassan El Bahi, n°6
 * Lire le rayon d'une sphère et afficher son volume.
 */

#include <stdio.h>

float volume(float r){
    return (4*3.14*r*r*r)/3;
}

int main(){
    float r;
    printf("veuillez entrez le rayon de la sphere : ");
    scanf("%f",&r);
    printf("le volume de la sphère de rayon %f est : %f\n",r,volume(r));
    return 0;
}

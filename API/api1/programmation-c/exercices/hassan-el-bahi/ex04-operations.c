/*
 * Exercice de la série de Hassan El Bahi, n°4
 * Somme, produit, division et soustraction de deux nombres.
 */

#include <stdio.h>


float somme(float x,float y){
    return x+y;
}

float sous(float x,float y){
    return x-y;
}

float div(float x,float y){
    return x/y;
}

float produit(float x,float y){
    return x*y;
}

int main(){
    float x,y;
    printf("Veuillez saisir x et y : \n");
    printf("x : ");
    scanf("%f",&x);
    printf("y : ");
    scanf("%f",&y);
    printf("La somme de x et y est : %f\n",somme(x,y));
    printf("Le produit de x et y est : %f\n",produit(x,y));
    printf("La division de x et y est : %f\n",div(x,y));
    printf("La soustraction de x et y est : %f\n",sous(x,y));
    return 0;
}

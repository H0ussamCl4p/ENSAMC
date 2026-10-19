/*
 * Définir une structure point (x, y), lire deux points et afficher la distance entre eux.
 * Compiler avec -lm : gcc point-distance.c -o point -lm
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct points {
    float x;
    float y;
};

int main(){
    struct points p1,p2;
    float d;
    printf("Veuillez saisir les coordonnees du premier point (x1,y1) : ");
    printf("x1 = ");
    scanf("%f", &p1.x);
    printf("y1 = ");
    scanf("%f", &p1.y);
    printf("Veuillez saisir les coordonnees du deuxieme point (x2,y2) : ");
    printf("x2 = ");
    scanf("%f", &p2.x);
    printf("y2 = ");
    scanf("%f", &p2.y);
    d = sqrt((p2.x - p1.x)*(p2.x - p1.x) + (p2.y - p1.y)*(p2.y - p1.y));    
    printf("La distance entre les deux points est : %f\n", d);
    return 0;

}

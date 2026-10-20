/*
 * Exercice de la série de Hassan El Bahi, n°79
 * Créer, initialiser et utiliser un pointeur.
 */

#include <stdio.h>

int main(){
    int a=5;
    int *p=&a;
    printf("L'adresse de a est : %p\n",(void *)&a);
    printf("La valeur de p (adresse de a) : %p\n",(void *)p);
    printf("La valeur de a est : %d\n",a);
    printf("La valeur pointée par p : %d\n",*p);
    *p=10;
    printf("La nouvelle valeur de a est : %d\n",a);
    return 0;
}

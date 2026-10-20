/*
 * Exercice de la série de Hassan El Bahi, n°1
 * Demander l'année de naissance et l'année courante, puis afficher l'âge.
 */

#include <stdio.h>

int main(){
    int annee_naissance, age, annee_courante;
    printf("Veuillez saisir votre annee de naissance : ");
    scanf("%d",&annee_naissance);
    printf("Veuillez saisir l'annee courante : ");
    scanf("%d",&annee_courante);    
    age = annee_courante - annee_naissance;
    printf("Vous avez %d ans.\n", age);
    return 0;
}

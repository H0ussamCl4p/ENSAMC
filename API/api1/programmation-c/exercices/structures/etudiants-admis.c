/*
 * Structure étudiant (nom, prénom, note) : lire une liste d'étudiants
 * et afficher ceux qui ont une note supérieure ou égale à 10.
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define max 100

struct Etudiants{
    char nom[20];
    char prenom[20];
    float note;
};

int main(){
    struct Etudiants tab[max];
    int i , n;
    printf("Veuillez saisir le nombre d'etudiants :");
    scanf("%d",&n);
    for(i=0; i<n; i++){
        printf("Veuillez saisir le nom de l'etudiant %d : ", i+1);
        scanf("%s", tab[i].nom);
        printf("Veuillez saisir le prenom de l'etudiant %d : ", i+1);
        scanf("%s", tab[i].prenom);
        printf("Veuillez saisir la note de l'etudiant %d : ", i+1);
        scanf("%f", &tab[i].note);
    }
    printf("Les étudiants ayant une note superieure ou egale a 10 sont :\n");
    for(i=0; i<n; i++){
        if(tab[i].note >= 10){
            printf("%s %s\n", tab[i].nom, tab[i].prenom);
        }
    }
    return 0;
}

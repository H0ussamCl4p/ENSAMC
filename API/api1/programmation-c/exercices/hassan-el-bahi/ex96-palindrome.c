/*
 * Exercice de la série de Hassan El Bahi, n°96
 * Vérifier si un mot est un palindrome.
 */

#include <stdio.h>
#include <string.h>


int main(){
    int n, i, len;
    char mot[100];
    char mot_inverse[100];
    printf("Veuillez saisir un mot : ");
    fgets(mot, sizeof(mot), stdin);
    mot[strcspn(mot, "\n")] = '\0';
    len = strlen(mot);
    for(i=0;i<len;i++)
        mot_inverse[i]=mot[len-1-i];
    mot_inverse[len]='\0';
    n=strcmp(mot,mot_inverse);
    if(n==0)
        printf("Le mot %s est un palindrome\n",mot);
    else
        printf("Le mot %s n'est pas un palindrome\n",mot);
    return 0;
}

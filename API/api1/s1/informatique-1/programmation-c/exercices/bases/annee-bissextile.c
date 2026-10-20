/*
 * Dire si une année est bissextile.
 */

#include <stdio.h>

void bis(int n){
    if (n%4==0){
        if (n%100==0){
            if (n%400==0){
                printf("L'annee est bissextile");
            }
            else {
                printf("L'annee n'est pas bissextile");
            }
        }
        else {
                printf("L'annee est bissextile");
        }

    }
    else {
        printf("L'annee n'est pas bissextile");
    }
}

int main()
{
    int n;
    printf("Veuillez saisir une annee : ");
    scanf("%d",&n);
    bis(n);
    return 0;
}

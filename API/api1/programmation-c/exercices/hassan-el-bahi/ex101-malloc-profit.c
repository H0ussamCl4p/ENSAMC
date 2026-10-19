/*
 * Exercice de la série de Hassan El Bahi, n°101
 * Avec l'allocation dynamique : lire le prix de revient et le prix de vente,
 * puis dire s'il y a un profit ou une perte.
 */

#include <stdio.h>
#include <stdlib.h>

int main(){
    float *p_achat = malloc(sizeof(float));
    float *p_vente = malloc(sizeof(float));
    float *p_profit = malloc(sizeof(float));

    printf("veuillez saisir le prix d'achat : ");
    scanf("%f",p_achat);

    printf("veuillez saisir le prix de vente : ");
    scanf("%f",p_vente);

    *p_profit=*p_vente-*p_achat;
    if(*p_profit>0)
        printf("vous avez un profit de : %f\n",*p_profit);
    else if(*p_profit<0)
        printf("vous avez une perte de : %f\n",-*p_profit);
    else
        printf("vous n'avez ni profit ni perte\n");
        
    free(p_achat);
    free(p_vente);
    free(p_profit);

    return 0;
}

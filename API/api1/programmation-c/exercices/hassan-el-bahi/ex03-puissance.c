/*
 * Exercice de la série de Hassan El Bahi, n°3
 * Lire x et y et calculer x puissance y.
 */

#include <stdio.h>


int puissance(int x , int y){
    int i,p;
    p=1;
    for(i=1;i<=y;i++){
        p*=x;
    }
    return p;
}

int main(){
    int x,y;
    printf("Veuillez saisir x et    y : \n");
    printf("x : ");             
    scanf("%d",&x);
    printf("y : ");
    scanf("%d",&y);
    printf("x^y = %d\n",puissance(x,y));
    return 0;
}

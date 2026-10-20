/*
 * Échanger deux entiers sans variable auxiliaire (a = a + b ; b = a - b ; a = a - b).
 */

#include <stdio.h>
#include <stdlib.h>

/* a et b sont des copies : l'échange n'est visible que dans la fonction.
   Pour modifier les variables du main, il faut passer des pointeurs (int *a, int *b). */
void permut(int a ,int b)
{
   /** int c;
    c = a;
    a = b;
    b = c; **/

    a = a+b;
    b = a-b;
    a = a-b;

    printf("La valeur de a est %d \n La valeur de b est %d",a,b);
}

int main()
{
    int a,b;
    printf("Veuillez saisir la valeur de a :\n");
    scanf("%d",&a);
    printf("Veuillez saisir la valeur de b :\n");
    scanf("%d",&b);
    permut(a,b);
    return 0;
}

/*
 * Chiffre de César : décaler chaque lettre du message de k positions.
 */

#include <stdio.h>
#include <ctype.h>

#define MAX 1024

int main(void)
{
    int k;
    char message[MAX];


    printf("Veuillez saisir la cle de chiffrement : ");
    scanf("%d", &k);

    getchar();     

    printf("Veuillez saisir le message : ");
    scanf(" %[^\n]", message);       

    for (char *p = message; *p; ++p) {
        if (isupper((unsigned char)*p))
            *p = 'A' + (*p - 'A' + k) % 26;
        else if (islower((unsigned char)*p))
            *p = 'a' + (*p - 'a' + k) % 26;
    }


    printf("Message chiffre : %s\n", message);
    return 0;
}

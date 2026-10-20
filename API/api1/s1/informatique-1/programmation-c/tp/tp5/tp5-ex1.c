#include <stdio.h>
#include <string.h>

int main() {
    char TXT[201];
    int longueur = 0, nbe = 0;
    printf("Entrez une phrase (max 200 caracteres) :\n");
    fgets(TXT, 201, stdin);

    while (TXT[longueur] != '\0' && TXT[longueur] != '\n') {
        if (TXT[longueur] == 'e' || TXT[longueur] == 'E') nbe++;
        longueur++;
    }
    printf("a) Longueur de la chaine : %d\n", longueur);
    printf("b) Nombre de lettres 'e' : %d\n", nbe);
    printf("c) Phrase inversee : ");
    for (int i = longueur - 1; i >= 0; i--) {
        printf("%c", TXT[i]);
    }
    printf("\n");
    return 0;
}

#include <stdio.h>

int main() {
    char *jours[] = {"", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"};
    int n;
    printf("Entrez un nombre entre 1 et 7 : ");
    scanf("%d", &n);
    if (n >= 1 && n <= 7) {
        printf("Jour correspondant : %s\n", jours[n]);
    } else {
        printf("Nombre invalide.\n");
    }
    return 0;
}

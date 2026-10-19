/*
 * Écrire une ligne dans un fichier texte puis la relire.
 */

#include <stdio.h>

int main() {
    FILE *f = fopen("test.txt", "w");
    if (f == NULL) {
        printf("Erreur d'ouverture.\n");
        return 1;
    }

    fprintf(f, "Bonjour ENSAM\n");
    fclose(f);

    // Lecture
    char ligne[100];
    f = fopen("test.txt", "r");
    if (f == NULL) {
        printf("Erreur d'ouverture.\n");
        return 1;
    }

    fgets(ligne, sizeof(ligne), f);
    printf("Contenu lu : %s", ligne);
    fclose(f);

    return 0;
}

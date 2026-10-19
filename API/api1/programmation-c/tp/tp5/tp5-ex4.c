#include <stdio.h>
#define MAX 100

struct Enregistrement {
    int matricule;
    char nom[100];
    char prenom[100];
};
int main(void) {
    int n;
    struct Enregistrement e;
    struct Enregistrement T[MAX];
    FILE *file;
    file = fopen("EnsamApi2.txt", "w");
    if (file == NULL) {
        printf("Erreur : impossible d’ouvrir le fichier.\n");
        return 1;
    }
    do {
        printf("Entrez le nombre d'enregistrements (1 a %d) : ", MAX);
        scanf("%d", &n);
    } while (n < 1 || n > MAX);
    for (int i = 0; i < n; i++) {
        printf("Enregistrement %d :\n", i + 1);
        printf("- Matricule : ");
        scanf("%d", &T[i].matricule);
        printf("- Nom : ");
        scanf("%s", T[i].nom);
        printf("- Prenom : ");
        scanf("%s", T[i].prenom);
    }
    for (int i = 0; i < n; i++) {
        fprintf(file, "%d %s %s\n", T[i].matricule, T[i].nom, T[i].prenom);
    }
    fclose(file);
    file = fopen("EnsamApi2.txt", "r");
    if (file == NULL) {
        printf("Erreur : impossible d’ouvrir le fichier.\n");
        return 1;
    }
    printf("\nContenu du fichier :\n");
    while (fscanf(file, "%d %s %s", &e.matricule, e.nom, e.prenom) != EOF) {
        printf("%d\t%s\t%s\n", e.matricule, e.nom, e.prenom);
    }
    fclose(file);
    return 0;
}

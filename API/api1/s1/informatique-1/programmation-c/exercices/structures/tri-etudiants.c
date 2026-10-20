/*
 * Lire des étudiants (nom, note) et les trier par note croissante (tri à bulles).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define max1 100
#define max2 50

typedef struct {
    char name[max2];
    float grade;
} Student;

void input(Student Etudiants[], int *n) {
    printf("Veuillez saisir le nombre d'etudiants : ");
    scanf("%d", n);
    getchar();

    for (int i = 0; i < *n; i++) {
        printf("\nEtudiant %d\n", i + 1);
        printf("Nom: ");
        fgets(Etudiants[i].name, max2, stdin);
        Etudiants[i].name[strcspn(Etudiants[i].name, "\n")] = 0;
        printf("Note: ");
        scanf("%f", &Etudiants[i].grade);
        getchar();
    }
}

void tri_note(Student Etudiants[], int n) {
    Student temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (Etudiants[j].grade > Etudiants[j + 1].grade) {
                temp = Etudiants[j];
                Etudiants[j] = Etudiants[j + 1];
                Etudiants[j + 1] = temp;
            }
        }
    }
}

void affichage(Student Etudiants[], int n) {
    printf("\nLes etudiants trie par ordre croissant :\n");
    for (int i = 0; i < n; i++) {
        printf("%s - %.2f\n", Etudiants[i].name, Etudiants[i].grade);
    }
}

int main() {
    Student Etudiants[max1];
    int n;
    input(Etudiants, &n);
    tri_note(Etudiants, n);
    affichage(Etudiants, n);

    return 0;
}

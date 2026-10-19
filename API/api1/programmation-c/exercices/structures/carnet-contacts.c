/*
 * Carnet de contacts (nom, prénom, téléphone) avec allocation dynamique et recherche par nom.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAILLE_NOM 30
#define TAILLE_TEL 15

/* ---------- Structures ---------- */
typedef struct {
    char nom[TAILLE_NOM];
    char prenom[TAILLE_NOM];
    char tel[TAILLE_TEL];
} Contact;

/* ---------- Fonctions ---------- */
void saisir(Contact *c) {
    printf("Nom        : ");  scanf("%29s", c->nom);
    printf("Prénom     : ");  scanf("%29s", c->prenom);
    printf("Téléphone  : ");  scanf("%14s", c->tel);
}

void afficher_contact(const Contact *c) {
    printf("Nom : %-29s | Prénom : %-29s | Tél : %-14s\n",
           c->nom, c->prenom, c->tel);
}

void afficher_liste(const Contact *tab, int n) {
    puts("\n----- Carnet de contacts -----");
    for (int i = 0; i < n; ++i) {
        printf("%2d. ", i + 1);
        afficher_contact(&tab[i]);
    }
}

void rechercher_par_nom(const Contact *tab, int n, const char *nom_recherche) {
    int trouve = 0;
    puts("\nRésultat de la recherche :");
    for (int i = 0; i < n; ++i) {
        if (strcmp(tab[i].nom, nom_recherche) == 0) {
            afficher_contact(&tab[i]);
            trouve = 1;
        }
    }
    if (!trouve) {
        printf("Aucun contact trouvé avec le nom « %s ».\n", nom_recherche);
    }
}

/* ---------- Programme principal ---------- */
int main(void) {
    int n;
    printf("Combien de contacts voulez-vous saisir ? ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        puts("Nombre non valide.");
        return 1;
    }

    Contact *contacts = malloc(n * sizeof *contacts);
    if (!contacts) {
        puts("Erreur d'allocation mémoire.");
        return 1;
    }

    for (int i = 0; i < n; ++i) {
        printf("\n--- Saisie du contact %d/%d ---\n", i + 1, n);
        saisir(&contacts[i]);
    }

    afficher_liste(contacts, n);

    char nom_recherche[TAILLE_NOM];
    printf("\nEntrez un nom à rechercher : ");
    scanf("%29s", nom_recherche);
    rechercher_par_nom(contacts, n, nom_recherche);

    free(contacts);
    return 0;
}

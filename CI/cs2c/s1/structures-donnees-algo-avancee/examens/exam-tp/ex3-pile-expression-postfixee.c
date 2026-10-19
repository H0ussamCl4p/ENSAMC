/*
 * Examen TP DSA, exercice 3 : pile et expression postfixée
 *
 * Une expression postfixée (notation polonaise inversée) place les opérateurs
 * après leurs opérandes, donc pas besoin de parenthèses. On l'évalue de gauche
 * à droite avec une pile :
 *   1. si on lit un nombre, on l'empile ;
 *   2. si on lit un opérateur, on dépile les deux dernières valeurs, on
 *      applique l'opération et on empile le résultat ;
 *   3. à la fin, la pile contient un seul élément : le résultat.
 *
 * Écrire une fonction qui évalue une expression postfixée donnée sous forme de
 * chaîne, où les tokens (nombres et opérateurs + - * /) sont séparés par des
 * espaces.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define TAILLE_MAX 100

typedef struct {
    float t[TAILLE_MAX];
    int sommet;
} lifo;

void init(lifo *p) { p->sommet = -1; }

void push(lifo *p, float x) {
    if (p->sommet < TAILLE_MAX - 1)
        p->t[++p->sommet] = x;
}

float pop(lifo *p) {
    return p->t[p->sommet--];
}

/* strtok modifie la chaîne : c doit être modifiable (pas une chaîne littérale) */
float eval(char *c) {
    lifo l;
    init(&l);
    char *token = strtok(c, " ");
    while (token != NULL) {
        if (isdigit(token[0]) || (token[0] == '-' && isdigit(token[1]))) {
            push(&l, atof(token)); /* atof gère 12, 3.5, -4 */
        } else {
            float b = pop(&l);
            float a = pop(&l);
            switch (token[0]) {
                case '+': push(&l, a + b); break;
                case '-': push(&l, a - b); break;
                case '*': push(&l, a * b); break;
                case '/': push(&l, a / b); break;
            }
        }
        token = strtok(NULL, " ");
    }
    return pop(&l);
}

int main(void) {
    char e1[] = "3 4 + 2 *";        /* (3 + 4) * 2 = 14 */
    char e2[] = "5 1 2 + 4 * + 3 -"; /* 5 + (1 + 2) * 4 - 3 = 14 */
    char e3[] = "12 -4 /";          /* 12 / -4 = -3 */

    printf("%g\n", eval(e1));
    printf("%g\n", eval(e2));
    printf("%g\n", eval(e3));
    return 0;
}

/*
 * Exercice : opérations sur une liste chaînée
 * Construire une liste aléatoire, insérer au début et à la fin, afficher à l'envers
 * (récursif), supprimer en tête, en fin, par valeur, puis libérer la liste.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct cell {
    int val;
    char s[2];
    struct cell* next;
} cell;

cell* build_n_random(int n) {
    if (n <= 0) return NULL;
    cell* head = NULL, *current = NULL;
    for (int i = 0; i < n; i++) {
        cell* new_cell = malloc(sizeof(cell));
        new_cell->val = rand() % 26;
        new_cell->s[0] = 'A' + new_cell->val;
        new_cell->s[1] = '\0';
        new_cell->next = NULL;
        if (!head) head = new_cell;
        else current->next = new_cell;
        current = new_cell;
    }
    return head;
}

void print_list(const cell* head) {
    while (head) {
        printf("[%d, %s] -> ", head->val, head->s);
        head = head->next;
    }
    printf("NULL\n");
}


void push_front(cell** phead, int v, char c) {
    cell* new_cell = malloc(sizeof(cell));
    new_cell->val = v;
    new_cell->s[0] = c;
    new_cell->s[1] = '\0';
    new_cell->next = *phead;
    *phead = new_cell;
}

void push_back(cell** phead, int v, char c) {
    cell* new_cell = malloc(sizeof(cell));
    new_cell->val = v;
    new_cell->s[0] = c;
    new_cell->s[1] = '\0';
    new_cell->next = NULL;
    if (*phead == NULL) {
        *phead = new_cell;
        return;
    }
    cell* cur = *phead;
    while (cur->next != NULL) cur = cur->next;
    cur->next = new_cell;
}

void print_reverse_rec(const cell* head) {
    if (head == NULL) return;
    print_reverse_rec(head->next);
    printf("[%d, %s] -> ", head->val, head->s);
}

void pop_front(cell** phead) {
    if (*phead == NULL) return;
    cell* tmp = *phead;
    *phead = (*phead)->next;
    free(tmp);
}

void pop_back(cell** phead) {
    if (*phead == NULL) return;
    if ((*phead)->next == NULL) {
        free(*phead);
        *phead = NULL;
        return;
    }
    cell* cur = *phead;
    while (cur->next->next != NULL) cur = cur->next;
    free(cur->next);
    cur->next = NULL;
}

void remove_first_by_val(cell** phead, int v) {
    if (*phead == NULL) return;
    cell* cur = *phead, *prev = NULL;
    while (cur && cur->val != v) {
        prev = cur;
        cur = cur->next;
    }
    if (cur == NULL) return;
    if (prev == NULL) *phead = cur->next;
    else prev->next = cur->next;
    free(cur);
}

void free_list(cell** phead) {
    cell* cur = *phead;
    while (cur) {
        cell* tmp = cur;
        cur = cur->next;
        free(tmp);
    }
    *phead = NULL;
}

int main() {
    srand(time(NULL));

    cell* list = build_n_random(5);
    printf("Liste initiale :\n");
    print_list(list);

    printf("\nInsertion au debut:\n");
    push_front(&list, 0, 'A');
    print_list(list);

    printf("\nInsertion en fin:\n");
    push_back(&list, 25, 'Z');
    print_list(list);

    printf("\nreverse:\n");
    print_reverse_rec(list);
    printf("NULL\n");

    printf("\nSuppression du premier elt :\n");
    pop_front(&list);
    print_list(list);

    printf("\nSuppression du dernier elt :\n");
    pop_back(&list);
    print_list(list);

    printf("\nSuppression du premier elt de val=10 :\n");
    remove_first_by_val(&list, 10);
    print_list(list);

    printf("\nSuppression de la liste :\n");
    free_list(&list);
    print_list(list);

    return 0;
}

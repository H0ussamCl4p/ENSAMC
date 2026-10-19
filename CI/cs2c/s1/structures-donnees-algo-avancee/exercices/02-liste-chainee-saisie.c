/*
 * Exercice : liste chaînée
 * Créer une liste de n nœuds (entier + chaîne) saisis par l'utilisateur,
 * l'afficher puis libérer la mémoire.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int n;
    char ch[10];
    struct Node* next;
} Node;


Node* Init_node(int val, const char* exp) {
    Node* node = (Node*)malloc(sizeof(Node));

    if (node == NULL) {
        printf("Allocation failed!\n");
        exit(1);
    }

    node->n = val;
    strcpy(node->ch, exp);
    node->next = NULL;

    return node;
}


Node* write_list(int count) {
    Node* head = NULL;
    Node* temp = NULL;

    for (int i = 0; i < count; i++) {
        int value;
        char word[10];

        printf("Enter value for node %d: ", i + 1);
        scanf("%d", &value);

        printf("Enter string for node %d: ", i + 1);
        scanf("%9s", word);

        Node* newNode = Init_node(value, word);

        if (head == NULL) {
            head = newNode;
            temp = newNode;
        } else {
            temp->next = newNode;
            temp = newNode;
        }
    }

    return head;
}


void print_list(Node* head) {
    Node* temp = head;
    printf("\n--- Linked List ---\n");
    while (temp != NULL) {
        printf("Value: %d, String: %s\n", temp->n, temp->ch);
        temp = temp->next;
    }
}

void free_list(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        Node* next = temp->next;
        free(temp);
        temp = next;
    }
}

int main() {
    int count;
    printf("How many nodes do you want? ");
    scanf("%d", &count);

    Node* head = write_list(count);
    print_list(head);
    free_list(head);

    return 0;
}

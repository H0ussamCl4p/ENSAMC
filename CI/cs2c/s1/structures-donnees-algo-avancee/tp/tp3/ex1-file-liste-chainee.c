/*
 * TP3 ex1 : file (queue) implémentée avec une liste chaînée
 * init, enqueue, dequeue, front, size, clear. Le main teste chaque fonction.
 *
 * Auteur : CHOUBIK Houssam (CS2C 1)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct QNode {
    char id[32];
    struct QNode* next;
} QNode;

typedef struct {
    QNode* head;
    QNode* tail;
    int count;
} QueueList;
void queue_init(QueueList* q) {
    q->head = NULL;
    q->tail = NULL;
    q->count = 0;
}
int queue_is_empty(const QueueList* q) {
    return (q->count == 0);
}
int enqueue(QueueList* q, const char* id) {
    QNode* node = (QNode*)malloc(sizeof(QNode));
    if (!node) return 0;

    strncpy(node->id, id, sizeof(node->id) - 1);
    node->id[sizeof(node->id) - 1] = '\0';
    node->next = NULL;

    if (queue_is_empty(q)) {
        q->head = q->tail = node;
    } else {
        q->tail->next = node;
        q->tail = node;
    }

    q->count++;
    return 1;
}
int dequeue(QueueList* q, char* out_id) {
    if (queue_is_empty(q))
        return 0;

    QNode* temp = q->head;
    if (out_id != NULL)
        strcpy(out_id, temp->id);

    q->head = temp->next;
    if (q->head == NULL)
        q->tail = NULL;

    free(temp);
    q->count--;
    return 1;
}
int queue_front(const QueueList* q, char* out_id) {
    if (queue_is_empty(q))
        return 0;

    if (out_id != NULL)
        strcpy(out_id, q->head->id);

    return 1;
}
int queue_size(const QueueList* q) {
    return q->count;
}
void queue_clear(QueueList* q) {
    char tmp[32];
    while (dequeue(q, tmp));
    q->head = q->tail = NULL;
    q->count = 0;
}

int main(void) {
    QueueList q;
    char id[32];
    queue_init(&q);
    if (queue_is_empty(&q) && queue_size(&q) == 0)
        printf("1) OK init\n");
    else
        printf("1) ERREUR init\n");
    enqueue(&q, "A");
    enqueue(&q, "B");
    enqueue(&q, "C");
    if (queue_size(&q) == 3) printf("2) OK enqueue A,B,C\n");
    queue_front(&q, id);
    if (strcmp(id, "A") == 0) printf("OK front == A\n");
    dequeue(&q, id);
    if (strcmp(id, "A") == 0) printf("3) OK dequeue -> %s\n", id);
    queue_front(&q, id);
    if (strcmp(id, "B") == 0 && queue_size(&q) == 2)
        printf("OK front == B ; size == 2\n");
    queue_clear(&q);
    if (queue_is_empty(&q))
        printf("4) OK clear to empty\n");
    return 0;
}

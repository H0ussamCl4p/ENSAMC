#include <stdio.h>

typedef struct Node{

	int data;
	struct Node* next;
}Node;

Node* newNode(int data) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

Node* reverseSegment(Node* start, Node* end) {
    Node* prev = NULL;
    Node* curr = start;
    Node* stop = end->next;

    while (curr != stop) {
        Node* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

Node* restoreOriginal(Node* head) {
    Node dummy;
    dummy.next = head;
    Node* prev = &dummy;
    Node* curr = head;

    while (curr) {
        if (curr->data % 2 == 0) { 
            Node* start = curr;
            while (curr->next && curr->next->data % 2 == 0) {
                curr = curr->next;
            }
            Node* end = curr;
            Node* next = end->next;

            
            Node* newHead = reverseSegment(start, end);

            
            prev->next = newHead;
            start->next = next;

            
            prev = start;
            curr = next;
        } else {
            prev = curr;
            curr = curr->next;
        }
    }
    return dummy.next;
}

void printList(Node* head) {
    for (Node* temp = head; temp; temp = temp->next) {
        printf("%d ", temp->data);
    }
    printf("\n");
}

int main() {
    int n;
    scanf("%d", &n);

    Node* head = NULL;
    Node* tail = NULL;

    for (int i = 0; i < n; i++) {
        int val;
        scanf("%d", &val);
        Node* node = newNode(val);
        if (!head) head = tail = node;
        else {
            tail->next = node;
            tail = node;
        }
    }

    head = restoreOriginal(head);
    printList(head);

    return 0;
}

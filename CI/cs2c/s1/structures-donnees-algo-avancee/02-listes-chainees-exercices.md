---
title: Linked List - exercices
date: 2025-09-26
author: CHOUBIK Houssam
draft: false
tags:
  - DSA
  - CS2C
  - ENSAMC
---

When you want to create a node dynamically, you use `malloc`:

```C
struct node *n1 = (struct node *)malloc(sizeof(struct node));
```

This allocates memory for one node and returns a pointer to it.

---
## Exercice 1 : 


```C
#include <stdio.h>
#include <stdlib.h>


 struct Node{

    int n;
    char ch[10];

    struct Node* next;
 };



int main()
{
    struct Node *n1= (struct Node *)malloc(sizeof(struct Node));
    struct Node *n2= (struct Node *)malloc(sizeof(struct Node));
    struct Node *n3= (struct Node *)malloc(sizeof(struct Node));


    n1-> n=10;
    strcpy(n1->ch,"A");

    n2-> n=20;
    strcpy(n2->ch,"B");

    n3-> n=30;
    strcpy(n3->ch,"C");


    n1->next=n2;
    n2->next=n3;
    n3->next=NULL;

    struct Node *count=n1;

    while(count!=NULL){
        printf("(%d , \"%s\")\n",count->n,count->ch);
        count=count->next;
    }

    free(n1);
    free(n2);
    free(n3);

    return 0;

}
```


NB !

```C
    (*n1).n=10;
    strcpy((*n1).ch,"A");

    n1-> n=10;
    strcpy(n2->ch,"A");
```

The two declarations are the same thing !!!!!

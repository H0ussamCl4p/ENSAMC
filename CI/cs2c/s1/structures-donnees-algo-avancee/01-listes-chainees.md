---
title: Linked List
date: 2025-09-26
author: CHOUBIK Houssam
draft: false
tags:
  - DSA
  - CS2C
  - ENSAMC
---

	Declaration of a matrix using dynamic allocation ; we should use a pointer of a pointer.
---
	A linked list : is a linear data structure where each element (called a node) is connected to the next one using pointers. Unlike array, elements of linked list are stored in random memory locations.

---
## What is a Linked List?

	A linked list is a sequence of nodes in which each node is made up of two parts:
	- ****Data****: The value stored in the node.
	- ****Pointer****: A reference to the next node in the sequence. __(There can be multiple pointers for different kind of linked list.)__
---
## Representation of Linked List in C

In C, linked lists are represented as the pointer to the first node in the list. For that reason, the first node is generally called ****head**** of the linked list. Each node of the linked list is represented by a structure that contains a data field and a pointer of the same type as itself. Such structure is called [self-referential structures](https://www.geeksforgeeks.org/dsa/self-referential-structures/).

## Types of Linked List in C

### Singly Linked List

A linked list or [****singly linked list****](https://www.geeksforgeeks.org/c/c-program-to-implement-singly-linked-list/) is a linear data structure that is made up of a group of nodes in which each node has two parts: the data, and the pointer to the next node. The last node's (also known as tail) pointers point to NULL to indicate the end of the linked list.

![singly-linked-list-in-c](https://media.geeksforgeeks.org/wp-content/uploads/20240826132228/singly-linked-list-in-c.webp)

Singly Linked List

#### Representation of Singly Linked List

A linked list is represented as a pointer to the first node where each node contains:

- ****Data:**** Here the actual information is stored.
- ****Next:**** [****Pointer****](https://www.geeksforgeeks.org/c/c-pointers/) that links to the next node.

```C
// Structure to represent the 
// singly linked list
struct Node {
  
  // Data field - can be of 
  // any type and count
  int data;
  
  // Pointer to the next node
  struct Node* next;
}
```

#### Basic Operations on Singly Linked List

|Operation|Operation Type|Description|Time Complexity|Space Complexity|
|---|---|---|---|---|
|Insertion|At Beginning|Insert a new node at the start of a linked list.|O (1)|O (1)|
|At the End|Insert a new node at the end of the linked list.|O (N)|O (1)|
|At Specific Position|Insert a new node at a specific position in a linked list.|O (N)|O (1)|
|Deletion|From Beginning|Delete a node from the start of a linked list|O (1)|O (1)|
|From the End|Delete a node at the end of a linked list.|O (N)|O (1)|
|A Specific Node|Delete a node from a specific position of a linked list.|O (N)|O (1)|
|Traversal|   |Traverse the linked list from start to end.|O (N)|O (1)|
#### Doubly Linked List

A [****doubly linked list****](https://www.geeksforgeeks.org/c/doubly-linked-list-in-c/) is a bit more complex than singly linked list. In it, each node contains three parts: the data, a pointer to the next node, and one extra pointer which points to the previous node. This allows for traversal in both directions, making it more versatile than a singly linked list.

![doubly-linked-list-in-c](https://media.geeksforgeeks.org/wp-content/uploads/20240826130046/doubly-linked-list-in-c.webp)

Doubly Linked List

#### Representation of Doubly Linked List

A doubly linked list is represented as a pointer to the first node (head), where each node contains:

- ****Data****: The actual information stored in the node.
- ****Next****: A pointer that links to the next node in the sequence.
- ****Previous****: A pointer that links to the previous node in the sequence.

```C
// Structure to represent the doubly linked list
struct Node {
  
  // Data field - can be of any type and count
  int data;
  
  // Pointer to the next node
  struct Node* next;
  
  // Pointer to the previous node
  struct Node* prev;
}
```

#### Basic Operations on Doubly Linked List

|Operation|Operation Type|Description|Time Complexity|Space Complexity|
|---|---|---|---|---|
|Insertion|At Beginning|Insert a new node at the start of a linked list.|O (1)|O (1)|
|At the End|Insert a new node at the end of the linked list.|O (N)|O (1)|
|At Specific Position|Insert a new node at a specific position in a linked list.|O (N)|O (1)|
|Deletion|From Beginning|Delete a node from the start of a linked list|O (1)|O (1)|
|From the End|Delete a node at the end of a linked list.|O (N)|O (1)|
|A Specific Node|Delete a node from a specific position of a linked list.|O (N)|O (1)|
|Traversal|   |Traverse the linked list from start to end or vice versa.|O (N)|O (1)|

### Circular Linked List

A [****circular linked list****](https://www.geeksforgeeks.org/c/c-program-to-implement-circular-linked-list/) is a variation of a singly linked list where the last node points back to the first node, forming a circle. This means there is no NULL at the end, and the list can be traversed in a circular manner.

![Circular-linked-list-in-c](https://media.geeksforgeeks.org/wp-content/uploads/20240826132256/Circular-linked-list-in-c.webp)

Circular Linked List

The structure of the circular linked list node is same as that of singly linked list.

#### Representation of Circular Linked List

A circular linked list is represented as a pointer to the first node, where each node contains:

- ****Data****: The actual information stored in the node.
- ****Next****: A pointer that links to the next node, with the last node pointing back to the first node.

```C
// Structure to represent the circular linked list
struct Node {
  
  // Data field - can be of any type and count
  int data;
  
  // Pointer to the next node
  struct Node* next;
}
```

> **Note:** A circular linked list can also be represented by a pointer to the last node.

### Basic Operations on Circular Linked List

|Operation|Operation Type|Description|Time Complexity|Space Complexity|
|---|---|---|---|---|
|Insertion|At Beginning|Insert a new node at the start of a linked list.|O (N)|O (1)|
|At the End|Insert a new node at the end of the linked list.|O (N)|O (1)|
|At Specific Position|Insert a new node at a specific position in a linked list.|O (N)|O (1)|
|Deletion|From Beginning|Delete a node from the start of a linked list|O (N)|O (1)|
|From the End|Delete a node at the end of a linked list.|O (N)|O (1)|
|A Specific Node|Delete a node from a specific position of a linked list.|O (N)|O (1)|
|Traversal|   |Traverse the linked list from start to end or vice versa.|O (N)|O (1)|


---

When you want to create a node dynamically, you use `malloc`:

`struct node *n1 = (struct node *)malloc(sizeof(struct node));`

This allocates memory for one node and returns a pointer to it.
# Structures de données et algorithmique avancée (CS2C, S1)

Tout est en C. Pour compiler un fichier : `gcc fichier.c -o prog`.

## Cours
- [00 : les bases du C](cours/00-dsa-en-c.md) : struct, pointeurs, malloc et free, fichiers, notation O
- [01 : listes chaînées](cours/01-listes-chainees.md) : insertion, suppression, listes doubles et circulaires
- [02 : listes chaînées, exercices](cours/02-listes-chainees-exercices.md)
- [03 : piles (LIFO)](cours/03-piles-lifo.md) : tableau et liste chaînée, parenthèses, expression postfixée
- [04 : files (FIFO)](cours/04-files-fifo.md) : tableau circulaire, liste chaînée, et LIFO contre FIFO

## Exercices
- [01 : structures](exercices/01-struct-etudiants.c) : tableau de struct étudiants
- [02 : liste chaînée](exercices/02-liste-chainee-saisie.c) : créer une liste depuis la saisie
- [03 : opérations sur une liste](exercices/03-liste-chainee-operations.c) : insertion, suppression, affichage à l'envers

## TP
- [TP3 ex1 : file avec liste chaînée](tp/tp3/ex1-file-liste-chainee.c)

## Examen TP (corrigé)
Chaque fichier contient l'énoncé en commentaire et un `main` de test.
- [ex1 : listes chaînées](examens/exam-tp/ex1-listes-chainees.c) : rotation, suppression des éléments d'une autre liste
- [ex2 : arbre binaire de recherche](examens/exam-tp/ex2-arbre-binaire-recherche.c) : taille, max, somme, hauteur minimale, feuilles
- [ex3 : pile](examens/exam-tp/ex3-pile-expression-postfixee.c) : évaluation d'une expression postfixée

## Pour aller plus loin : piles et files
En français :
- [Les piles et les files](https://sdz.tdct.org/sdz/les-piles-et-les-files-4.html) : tutoriel en C de l'ancien Site du Zéro (archive ; le navigateur peut signaler un certificat expiré).
- [Les piles et les files en langage C](https://www.studocu.com/row/document/universite-de-sousse/commande-des-machines/les-piles-et-les-files-en-langage-c/17168376) : cours sur Studocu (inscription parfois demandée).

En anglais :
- [Queue in C](https://www.geeksforgeeks.org/c/queue-in-c/) et [Queue data structure](https://www.geeksforgeeks.org/dsa/queue-data-structure/), GeeksforGeeks
- [FIFO approach](https://www.geeksforgeeks.org/dsa/fifo-first-in-first-out-approach-in-programming/) et [FIFO vs LIFO](https://www.geeksforgeeks.org/dsa/fifo-vs-lifo-approach-in-programming/), GeeksforGeeks
- [LIFO vs FIFO: mastering stacks and queues in C](https://medium.com/@edwinsanjosoji/lifo-vs-fifo-mastering-stacks-and-queues-in-c-4cfc58b8b17a), Medium
- [Understanding queues in JavaScript](https://dev.to/gr8soln/understanding-queues-data-structure-mastering-fifo-principle-in-javascript-8di), DEV

## Problem solving
Dans [problem-solving/](problem-solving/) : input-output, LeetCode (array, trees), reverse linked list. Les solutions LeetCode ne contiennent que la fonction, comme sur le site.

# Contribuer

## Où mettre un fichier

`<cycle>/<filière>/<semestre>/<module>/<type>/`

- cycle : `API`, `CI`, `Master`
- filière : `api1`, `api2`, `tronc-commun-1a`, `cs2c`, `iagi`...
- semestre : `s1`, `s2`... (on peut s'en passer si le module dure toute l'année)
- type : `cours`, `td`, `tp`, `projet`, `examens`, `assets` pour les images

Si un module est commun à plusieurs filières, il va dans `tronc-commun-1a`.

## Noms de fichiers

Minuscules, pas d'accents, pas d'espaces, des tirets entre les mots. Exemples : `td2-boucles-tableaux.md`, `tp1-ex3.c`, `tp2-ex2-q1.py`, `enonce-tp4.pdf`. Un préfixe `00-`, `01-` sert à garder l'ordre de lecture.

## Fichiers Markdown

Mettre un en-tête en haut du fichier, il servira pour le site plus tard :

```yaml
---
title: TD2 Boucles et tableaux
date: 2025-10-01
author: Prénom NOM
tags: [algorithmique, api1]
---
```

Pour les images, utiliser la syntaxe Markdown classique avec un chemin vers `assets/`, pas la syntaxe `![[...]]` d'Obsidian.

# Contribuer

## Où mettre un fichier

`<cycle>/<filière>/<semestre>/<module>/<type>/`

- cycle : `API`, `CI`, `Master`
- filière : `api1`, `api2`, `tronc-commun-1a`, `cs2c`, `iagi`... (créer le dossier quand il y a du contenu)
- semestre : `s1`, `s2`... (on peut s'en passer si le module dure toute l'année)
- type : `cours`, `td/tdN`, `tp/tpN`, `projet`, `assets` pour les images

Si un module est commun à plusieurs filières, il va dans `tronc-commun-1a`.

## Noms de fichiers

Minuscules, pas d'accents, pas d'espaces, des tirets entre les mots. Exemples : `td/td2/correction.md`, `td/td2/enonce.pdf`, `tp/tp1/tp1-ex3.c`, `tp/tp2/tp2-ex2-q1.py`. Un préfixe `00-`, `01-` sert à garder l'ordre de lecture.

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

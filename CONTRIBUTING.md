# Contribuer

## Où mettre un fichier

`<cycle>/<niveau ou filière>/<semestre>/<module>/<sous-module>/<type>/`

- cycle : `API`, `CI`, `Master`
- niveau ou filière : `api1`, `api2`, `cs2c`, `iagi`, `gsi`..., ou `tronc-commun` pour un module suivi par toutes les filières
- semestre : `s1`, `s2`... comme dans le programme officiel (en API : S1 et S2 en API1, S3 et S4 en API2)
- module : le nom officiel du module sur [ensam-casa.ma](https://www.ensam-casa.ma/), en minuscules sans accents, par exemple `systeme-d-exploitation-linux` ; mettre le nom exact dans le `title:` du `README.md` du module
- sous-module : quand un module en regroupe plusieurs, par exemple `informatique-1/algorithmique`
- type : `cours`, `td/tdN`, `tp/tpN`, `projet`, `assets` pour les images

Un module commun à toutes les filières va dans `tronc-commun`. Un module partagé par quelques filières reste dans le dossier d'une filière, et les pages des autres filières le mettent en lien.

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

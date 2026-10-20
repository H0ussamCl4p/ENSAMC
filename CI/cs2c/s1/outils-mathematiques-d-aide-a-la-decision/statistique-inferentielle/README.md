---
title: "Statistique inférentielle"
---

# Statistique inférentielle avec R (sous-module, S1)

- [Fiche statistiques avec R](fiche-r.md) : toutes les commandes utiles, de l'import des données à la régression
- [Examen blanc](examen-blanc.md) : statistique descriptive, données groupées et exercice R, avec corrigé

| Script | Contenu |
|---|---|
| [01-bases-r.R](01-bases-r.R) | Variables, vecteurs, indexation |
| [02-variable-discrete.R](02-variable-discrete.R) | Nombre d'enfants par famille : taille, type, valeurs distinctes |
| [03-gapminder-test-t.R](03-gapminder-test-t.R) | Données gapminder : résumé, dplyr, test t (Afrique du Sud vs Irlande), graphique ggplot2 |

Lancer un script :

```bash
Rscript 01-bases-r.R
```

Le script 03 a besoin de `install.packages(c("gapminder", "dplyr", "ggplot2"))` (une seule fois).

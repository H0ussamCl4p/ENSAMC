# Examen blanc : statistiques et R

Partie écrite sur 20 points, puis un exercice R sur 8 points. Le corrigé est à la fin.

## Exercice 1 : questions de cours (4 pts)

1. (2 pts) Expliquer la différence entre un **diagramme différentiel** et un **diagramme intégral** pour une variable quantitative.
2. (2 pts) Expliquer la différence entre la **variance théorique** et la **variance corrigée**. Donner les deux formules et dire pourquoi on utilise la variance corrigée.

## Exercice 2 : statistique descriptive univariée (8 pts)

On étudie X, la durée de fonctionnement (en heures) de 10 machines :

```
120  130  125  140  135  150  145  160  170  155
```

1. (1 pt) Donner la population, sa taille, le caractère étudié et sa nature.
2. (3 pts) Donner la formule de la moyenne, puis calculer la moyenne et la médiane.
3. (3 pts) Donner la formule de la variance théorique, puis calculer la variance corrigée et l'écart-type.
4. (1 pt) Comparer moyenne et médiane, et conclure sur l'asymétrie.

## Exercice 3 : données groupées (8 pts)

Temps de traitement (en secondes) d'une machine industrielle :

| Intervalle (s) | Effectif |
|---|---|
| [10 ; 20[ | 6 |
| [20 ; 30[ | 14 |
| [30 ; 40[ | 20 |
| [40 ; 50[ | 10 |
| **Total** | **50** |

1. (3 pts) Calculer les milieux de classes, donner la formule de la moyenne estimée et la calculer.
2. (3 pts) Calculer les effectifs cumulés, trouver la classe médiane et calculer la médiane estimée avec `Me = L + h × (N/2 − F) / f`.
3. (2 pts) Interpréter la moyenne et la médiane.

## Exercice R (8 pts, 30 à 40 min)

Un fichier texte contient la variable X, temps de réponse (en secondes), mesurée sur 20 individus. Son nom est stocké dans la variable `fichier`. Le fichier a une ligne d'en-tête, utilise `;` comme séparateur et `,` comme séparateur décimal.

1. (1 pt) Écrire la commande R qui importe les données dans un objet `data`.
2. (1 pt) Donner la population, sa taille, le caractère étudié et sa nature.
3. (3 pts) Donner les commandes R pour : la moyenne, la médiane, la variance corrigée, l'écart-type, les quartiles (une commande par ligne).
4. (2 pts) Donner les commandes R pour tracer un histogramme de X et une boîte à moustaches horizontale de X.
5. (1 pt) Donner les commandes R pour le coefficient d'asymétrie et le coefficient d'aplatissement, en précisant la bibliothèque.

---

## Corrigé

### Exercice 1

1. Le **diagramme différentiel** représente les effectifs (ou fréquences) de chaque valeur ou classe : diagramme en bâtons, histogramme. Le **diagramme intégral** représente les effectifs (ou fréquences) **cumulés** : courbe cumulative, en escalier pour une variable discrète.
2. Variance théorique : `V = (1/n) × Σ (xi − x̄)²`. Variance corrigée : `s² = (1/(n−1)) × Σ (xi − x̄)²`. Sur un échantillon, la variance théorique sous-estime en moyenne la variance de la population, parce que les écarts sont pris par rapport à x̄, calculée sur les mêmes données. Diviser par n − 1 donne un estimateur sans biais.

### Exercice 2

1. Population : les 10 machines. Taille n = 10. Caractère : la durée de fonctionnement, quantitatif continu.
2. `x̄ = (1/n) × Σ xi = 1430 / 10 = 143 h`.
   Valeurs triées : 120, 125, 130, 135, **140, 145**, 150, 155, 160, 170. n est pair, donc la médiane est la moyenne des 5e et 6e valeurs : `Me = (140 + 145) / 2 = 142,5 h`.
3. Écarts à la moyenne : −23, −13, −18, −3, −8, 7, 2, 17, 27, 12. Somme des carrés : 2310.
   Variance théorique : 2310 / 10 = 231. Variance corrigée : 2310 / 9 ≈ 256,67. Écart-type corrigé : √256,67 ≈ 16,02 h.
4. x̄ = 143 est à peine plus grand que Me = 142,5 : la distribution est presque symétrique, très légèrement étalée à droite.

### Exercice 3

1. Milieux : 15, 25, 35, 45. `x̄ ≈ Σ ni × ci / N = (6×15 + 14×25 + 20×35 + 10×45) / 50 = 1590 / 50 = 31,8 s`.
2. Effectifs cumulés : 6, 20, 40, 50. N/2 = 25, première classe où le cumul dépasse 25 : [30 ; 40[.
   L = 30, h = 10, F = 20, f = 20, donc `Me = 30 + 10 × (25 − 20) / 20 = 32,5 s`.
3. La moitié des traitements dure moins de 32,5 s, et la durée moyenne est 31,8 s. La moyenne est un peu plus petite que la médiane : la distribution est légèrement étalée à gauche, à cause de la classe [10 ; 20[.

### Exercice R

Question 2 : population, les 20 individus, taille n = 20. Caractère : le temps de réponse, quantitatif continu.

```r
# 1
data <- read.table(file = fichier, header = TRUE, sep = ";", dec = ",")

# 3
mean(data$X)
median(data$X)
var(data$X)
sd(data$X)
quantile(data$X)

# 4
hist(data$X)
boxplot(data$X, horizontal = TRUE)

# 5
library(moments)
skewness(data$X)
kurtosis(data$X)
```

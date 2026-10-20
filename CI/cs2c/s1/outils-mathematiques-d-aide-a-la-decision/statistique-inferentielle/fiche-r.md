# Fiche statistiques avec R

Dans les exemples, `data` est le tableau de données et `X` la variable étudiée.

## Importer les données

```r
# Fichier texte avec en-tête, séparateur ; et virgule décimale
data <- read.table(file = fichier, header = TRUE, sep = ";", dec = ",")

# CSV classique
data <- read.csv(fichier, header = TRUE)
```

## Accéder à une variable

```r
data$X
data[, "X"]
```

## Identifier le caractère

```r
length(data$X)   # taille n
str(data$X)      # type
summary(data$X)  # résumé : min, quartiles, moyenne, max
```

## Paramètres de position

```r
mean(data$X)       # moyenne
median(data$X)     # médiane
quantile(data$X)   # quartiles
```

## Paramètres de dispersion

```r
range(data$X)              # min et max
diff(range(data$X))        # étendue
var(data$X)                # variance corrigée (divise par n - 1)
sd(data$X)                 # écart-type corrigé
IQR(data$X)                # écart interquartile Q3 - Q1
sd(data$X) / mean(data$X)  # coefficient de variation
```

`var` et `sd` donnent toujours la version **corrigée**. Pour la variance théorique : `mean((data$X - mean(data$X))^2)`.

## Tableau statistique (variable discrète)

```r
eff     <- table(data$X)    # effectifs
freq    <- prop.table(eff)  # fréquences
effCum  <- cumsum(eff)      # effectifs cumulés
freqCum <- cumsum(freq)     # fréquences cumulées
```

## Graphiques

```r
hist(data$X)                         # histogramme (variable continue)
barplot(table(data$X))               # diagramme en bâtons (variable discrète)
boxplot(data$X)                      # boîte à moustaches
boxplot(data$X, horizontal = TRUE)   # boîte à moustaches horizontale
```

## Données groupées en classes

```r
milieux  <- (borne_inf + borne_sup) / 2
mean_est <- weighted.mean(milieux, effectif)   # moyenne estimée
```

Médiane estimée : on repère la classe médiane, celle où l'effectif cumulé dépasse N/2, puis

```
Me = L + h × (N/2 − F) / f
```

avec L la borne inférieure de la classe médiane, h son amplitude, f son effectif, et F l'effectif cumulé avant elle.

## Forme de la distribution

```r
library(moments)    # install.packages("moments") une seule fois
skewness(data$X)    # asymétrie : > 0 étalée à droite, < 0 étalée à gauche
kurtosis(data$X)    # aplatissement : 3 pour une loi normale
```

## Moyennes particulières

```r
sqrt(mean(data$X^2))   # moyenne quadratique
1 / mean(1 / data$X)   # moyenne harmonique
exp(mean(log(data$X))) # moyenne géométrique
```

## Statistiques par groupe

```r
aggregate(X ~ Groupe, data, mean)
aggregate(X ~ Groupe, data, sd)
by(data$X, data$Groupe, mean)
```

## Régression linéaire simple

```r
cor(data$X, data$Y)       # coefficient de corrélation
cov(data$X, data$Y)       # covariance
modele <- lm(Y ~ X, data) # droite Y = a + bX
summary(modele)
```

---
title: "Notes MATLAB"
date: 2025-02-28
author: CHOUBIK Houssam
tags: [matlab, api2]
---

# Notes MATLAB

## TP2 : vecteurs et matrices (28-02-2025)

### Matrices aléatoires

```
rand(n)
```
- matrice carrée d'ordre n de réels aléatoires entre 0 et 1

```
randi(m,n)
```
- matrice carrée d'ordre n d'entiers aléatoires entre 1 et m (i pour integer)

### Produit scalaire

```
>> x = [10 20 30 69 90];
>> a = x*x'
a =
       14261
>> b = sum(x.*x)
b =
       14261
```

Les deux écritures `x*x'` et `sum(x.*x)` sont équivalentes.

### repmat

`repmat(M, m, n)` répète la matrice M m fois en ligne et n fois en colonne. Utile pour générer des motifs ou étendre une matrice.

```
>> M = [1 2; 3 4];
>> repmat(M, 3, 5)     % matrice 6 x 10 : M répétée 3 fois vers le bas et 5 fois vers la droite
```

### toeplitz

`toeplitz(c, r)` crée une matrice de Toeplitz dont la première colonne est c et la première ligne est r.

```
>> n = 5;
>> M = toeplitz([1 3 zeros(1,n-2)], [1 2 zeros(1,n-2)])
M =
     1     2     0     0     0
     3     1     2     0     0
     0     3     1     2     0
     0     0     3     1     2
     0     0     0     3     1
```

Si le premier élément de c et celui de r sont différents, MATLAB affiche un avertissement et garde celui de la colonne :

```
>> toeplitz([1 2 3], [4 5 6])
Warning: First element of input column does not match first element of input row.
         Column wins diagonal conflict.
ans =
     1     5     6
     2     1     5
     3     2     1
```

### kron

```
>> A = [1 2; 3 4];
>> B = [5 6; 7 8];
>> kron(A,B)
ans =
     5     6    10    12
     7     8    14    16
    15    18    20    24
    21    24    28    32
```

`kron` multiplie chaque élément de A par la matrice B, on obtient une matrice par blocs :

```
kron(A,B) = [ 1*B  2*B
              3*B  4*B ]
```

## TP3 : représentation graphique (28-02-2025)

Le point-virgule `;` exécute une instruction sans afficher le résultat. Une expression non affectée (par exemple `a+b;`) est quand même rangée dans la variable `ans`, visible dans le Workspace.

```
>> a = 4, b = 2
>> a + b;
```

## TP8 : polynômes, fractions rationnelles (15-03-2025)

Un polynôme est représenté par le vecteur de ses coefficients, du plus haut degré au plus bas : `[2 5 4]` correspond à 2x² + 5x + 4.

### Dérivée : polyder

```
>> x = [2 5 4];
>> polyder(x)              % dérivée de x
ans =
     4     5
>> q = [5 2 3];
>> polyder(x, q)           % dérivée du produit x(t)*q(t)
ans =
    40    87    72    23
>> polyder(conv(x, q))     % même résultat : conv calcule le produit des polynômes
ans =
    40    87    72    23
```

`[y, z] = polyder(a, b)` renvoie y et z tels que y/z est la dérivée de la fraction a/b :

```
>> [y, z] = polyder(x, q)
y =
   -21   -28     7
z =
    25    20    34    12     9
```

### Intégrale : polyint et polyval

`polyint(p)` ou `polyint(p, constante)` donne une primitive. Pour une intégrale entre deux bornes, on évalue la primitive avec `polyval` puis on fait la différence :

```
>> w = [2 2];
>> P = polyint(w)
P =
     1     2     0
>> polyval(P, [1 3])
ans =
     3    15
>> diff(polyval(P, [1 3]))   % intégrale de 1 à 3 = 15 - 3
ans =
    12
```

`diff(v)` renvoie les différences entre éléments voisins : `diff([5 2 3 10])` donne `[-3 1 7]`.

### Décomposition en éléments simples : residue

```
>> n = 6;                 % numérateur
>> d = [1 6 11 6 0];      % dénominateur
>> [r, p, k] = residue(n, d)
r =
   -1.0000
    3.0000
   -3.0000
    1.0000
p =
   -3.0000
   -2.0000
   -1.0000
         0
k =
     []
```

Donc 6 / (x⁴ + 6x³ + 11x² + 6x) = -1/(x+3) + 3/(x+2) - 3/(x+1) + 1/x.

On revient à la fraction de départ avec `[n, d] = residue(r, p, k)`.

### Interpolation polynomiale : polyfit

```
>> x = randi(10, 1, 10);
>> y = randi(10, 1, 10);
>> p = polyfit(x, y, 4)    % polynôme de degré 4 le plus proche des points
>> rats(p)                 % affiche les coefficients sous forme de fractions
```

Avec un degré trop grand (ici 9 pour 10 points dont certains x sont répétés), MATLAB prévient que le polynôme est mal conditionné : il faut réduire le degré ou utiliser des x distincts.

### Coder et décoder un message

```
>> m = 'bonjour je suis houssam';
>> code = double(m) + 25;     % codes ASCII décalés de 25
>> char(code - 25)            % on retrouve le message
ans =
    'bonjour je suis houssam'
```

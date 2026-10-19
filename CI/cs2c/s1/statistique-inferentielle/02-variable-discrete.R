# Étude d'une variable discrète : nombre d'enfants par famille (100 familles)

nbenf <- c(1, 4, 4, 3, 1, 5, 2, 3, 2, 2, 2, 3, 2, 6, 4, 1, 3, 1, 6,
           2, 1, 4, 1, 1, 6, 4, 1, 5, 5, 1, 3, 3, 7, 2, 4, 3, 2, 3, 3, 5, 2, 3, 6,
           4, 4, 3, 2, 2, 1, 5, 3, 6, 2, 0, 5, 1, 7, 4, 3, 5, 4, 3, 6, 5, 2, 7, 7,
           3, 3, 1, 2, 0, 2, 3, 5, 3, 3, 7, 6, 7, 2, 3, 1, 3, 3, 3, 5, 3, 2, 5, 6,
           4, 1, 0, 2, 6, 5, 1, 0, 1)

nbenf
length(nbenf)   # taille de l'échantillon
mode(nbenf)     # type des données
unique(nbenf)   # valeurs distinctes

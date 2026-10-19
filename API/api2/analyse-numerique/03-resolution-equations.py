# Code pour l'analyse numérique , résolutions de équations

from math import sqrt, exp

# Demander à l'utilisateur de saisir les valeurs de a et b
a = float(input("Veuillez saisir la valeur de a : "))
b = float(input("Veuillez saisir la valeur de b : "))
x0 = float(input("Veuillez saisir la valeur de x0 : "))

# Tolérance
eps = 1e-13  

# Fonction
def f(x):
    return x**2 - 7

# La fonction dérivée
def df(x):
    return 2 * x

# Méthode du point fixe
def g(x):
    return 0.75 * x + 1.75 / x

# Vérification de l'existence d'une racine dans l'intervalle
if f(a) * f(b) > 0:
    print("L'intervalle [a, b] ne contient pas de racine (f(a) et f(b) ont le même signe).")
else:
    # Méthode de dichotomie
    def dichotomie(a, b, f, epsilon):
        while b - a > epsilon:
            c = (a + b) / 2
            if abs(f(c)) < epsilon:
                return c
            elif f(c) * f(a) < 0:
                b = c
            else:
                a = c
        return (a + b) / 2

    # Méthode de Newton
    def Newton(x0, f, df, epsilon):
        x = x0
        y = x - f(x) / df(x)
        while abs(y - x) > epsilon:
            x = y
            y = x - f(x) / df(x)
        return y

    # Méthode du point fixe
    def PointFixe(x0, g, epsilon):
        x = x0
        y = g(x)
        while abs(y - x) > epsilon:
            x = y
            y = g(x)
        return y

    # Affichage des résultats
    print("La solution par :")
    print("Dichotomie      :", dichotomie(a, b, f, eps))
    print("Newton          :", Newton(x0, f, df, eps))
    print("Point Fixe      :", PointFixe(x0, g, eps))
    print("Racine de 7     :", sqrt(7))

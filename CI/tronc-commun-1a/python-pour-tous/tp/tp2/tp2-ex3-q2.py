def fact(a):
    if a == 0:
        return 1
    else:
        s = int(a * fact(a - 1))
        return s

n=int(input("Donner un entier:"))
print(fact(n))
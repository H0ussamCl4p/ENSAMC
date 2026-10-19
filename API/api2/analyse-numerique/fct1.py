def f(x):
    return x**2-7

def df(x):
    return 2*x 

a=2
b=3

x0=3
x1=x0-f(x0)/df(x0)
print(x1)
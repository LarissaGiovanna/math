from sympy import symbols, expand, sympify

x_interpolado = 1

def interpolacao(x, y, x_interpolado):
    n = len(x)
    result = 0
    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo *= (x_interpolado - x[j]) / (x[i] - x[j])
        result += termo
    return result

def polinomio(x, y):
    X = symbols('X')
    n = len(x)
    Polinomioh = 0
    for i in range(n):
        termo = sympify(y[i])
        for j in range(n):
            if i != j:
                termo *= (X - x[j]) / (x[i] - x[j])
        Polinomioh += termo
    return expand(Polinomioh)
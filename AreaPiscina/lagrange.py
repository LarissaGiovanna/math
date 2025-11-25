from integral import comprimentosX, largurasY
from sympy import symbols, expand

x_interpolado = 1
def interpolacao(x, y, x_interpolado):
    n = len(x)
    result = 0
    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo *= (x_interpolado - x[j]) / (x[i] - x[j])
        resultado += termo
    return result
    
def polinomio(x, y):
    X = symbols('X')
    n = len(x)
    Polinomioh = 0
    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo *= (X - x[j]) / (x[i] - x[j])
        Polinomioh += termo
    return expand(Polinomioh)

print(f"Y interpolado para X={x_interpolado}: {interpolacao(comprimentosX, largurasY, x_interpolado)}")

print("Polinômio de Lagrange:")
print(polinomio(comprimentosX, largurasY))
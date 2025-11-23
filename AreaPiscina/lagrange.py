# Função de interpolação de Lagrange
def lagrange_interpolacao(x, y, x_interpolado):
    n = len(x)
    resultado = 0
    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo *= (x_interpolado - x[j]) / (x[i] - x[j])
        resultado += termo
    return resultado

# Polinômio simbólico de Lagrange (necessário SymPy instalado)
from sympy import symbols, expand
def lagrange_polinomio(x, y):
    X = symbols('X')
    n = len(x)
    polinomio = 0
    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo *= (X - x[j]) / (x[i] - x[j])
        polinomio += termo
    return expand(polinomio)

x_interpolado = 1
print(f"Y interpolado para X={x_interpolado}: {lagrange_interpolacao(comprimentosX, largurasY, x_interpolado)}")

print("Polinômio de Lagrange:")
print(lagrange_polinomio(comprimentosX, largurasY))

from sympy import symbols, expand, sympify

x_interpolado = 1
def interpolacao(x, y):
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

    #verificao caso exista x repetidos
    if len(set(x)) != len(x):
        raise ValueError("Existem valores repetidos em X. Interpolação de Lagrange não permite isso.")


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

# print(f"Y interpolado para X={x_interpolado}: {interpolacao(comprimentosX, largurasY)}")

# print("Polinômio de Lagrange:")
# print(polinomio(comprimentosX, largurasY))
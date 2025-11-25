<<<<<<< HEAD
from sympy import symbols, expand, sympify

x_interpolado = 1
def interpolacao(x, y):
=======
def interpolacao(x, y, x_interpolado):
>>>>>>> b735c63 (Refactor Lagrange interpolation functions)
    n = len(x)
    result = 0
    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo *= (x_interpolado - x[j]) / (x[i] - x[j])
<<<<<<< HEAD
        result += termo
    return result
    
def polinomio(x, y):

    #verificao caso exista x repetidos
    if len(set(x)) != len(x):
        raise ValueError("Existem valores repetidos em X. Interpolação de Lagrange não permite isso.")


=======
        resultado += termo
    return resultado
    
from sympy import symbols, expand
def polinomio(x, y):
>>>>>>> b735c63 (Refactor Lagrange interpolation functions)
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

<<<<<<< HEAD
# print("Polinômio de Lagrange:")
# print(polinomio(comprimentosX, largurasY))
=======
print("Polinômio de Lagrange:")
print(lagrange_polinomio(comprimentosX, largurasY))

>>>>>>> b735c63 (Refactor Lagrange interpolation functions)

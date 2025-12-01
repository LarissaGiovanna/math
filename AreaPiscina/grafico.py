from matplotlib import pyplot as mpl
import numpy as np
from sympy import symbols, lambdify

def organizar_grafico(funcaoAcima, funcaoAbaixo, comprimentosX_acima, comprimentosX_abaixo):
        X = symbols('X')

        # expr_acima/expr_abaixo são as Expressões SymPy retornadas por lagrange.polinomio(...)
        f_acima = lambdify(X, funcaoAcima, "numpy")
        f_abaixo = lambdify(X, funcaoAbaixo, "numpy")

        x_min = min(min(comprimentosX_acima), min(comprimentosX_abaixo))
        x_max = max(max(comprimentosX_acima), max(comprimentosX_abaixo))

        x_medio = np.linspace(x_min, x_max, 500)

        y_suave_acima = f_acima(x_medio)
        y_suave_abaixo = f_abaixo(x_medio)

        return x_medio, y_suave_acima, y_suave_abaixo

def mostrar_integral(x, y_acima, y_abaixo):
    mpl.figure()  # abre nova janela

    #destacar eixo x
    ax = mpl.gca()
    ax.axhline(0, color="black", linewidth=2)

    mpl.plot(x, y_acima, label="Curva acima", color="orange")
    mpl.plot(x, y_abaixo, label="Curva abaixo", color="blue")

    mpl.fill_between(x, y_acima, y_abaixo, color="orange", alpha=0.3)

    mpl.legend()
    mpl.grid()
    mpl.title("Área pela Integral")
    mpl.xlabel("x")
    mpl.ylabel("y")
    mpl.show(block = False)

def mostrar_trapezios(x_acima, y_acima, x_abaixo, y_abaixo):
    mpl.figure()

    # Parte de cima
    for i in range(len(x_acima) - 1):
        xs = [x_acima[i], x_acima[i+1], x_acima[i+1], x_acima[i]]
        ys = [0, 0, y_acima[i+1], y_acima[i]]
        mpl.fill(xs, ys, color="green", alpha=0.3)

    mpl.plot(x_acima, y_acima, marker="o", color="green", label="Acima")


    # Parte de baixo
    # ----- Ordenação -----
    x_abaixo_sorted, y_abaixo_sorted = zip(*sorted(zip(x_abaixo, y_abaixo)))

    for i in range(len(x_abaixo_sorted) - 1):
        xs = [x_abaixo_sorted[i], x_abaixo_sorted[i+1], 
              x_abaixo_sorted[i+1], x_abaixo_sorted[i]]
        ys = [0, 0, y_abaixo_sorted[i+1], y_abaixo_sorted[i]]
        mpl.fill(xs, ys, color="red", alpha=0.3)

    # ----- Curva -----
    mpl.plot(x_abaixo_sorted, y_abaixo_sorted, marker="o", color="red", label="Abaixo")


    # Eixo X mais destacado
    mpl.axhline(0, color="black", linewidth=2)

    mpl.legend()
    mpl.grid()
    mpl.xlabel("x")
    mpl.ylabel("y")
    mpl.title("Área pelo Método do Trapézio")
    mpl.show(block=False)

def pausar():
    input("Digite ENTER para encerrar...")
from matplotlib import pyplot as mpl
import numpy as np

def mostrar_integral(x, y_acima, y_abaixo):
    mpl.figure()  # abre nova janela
    mpl.plot(x, y_acima, label="Curva acima", color="orange")
    mpl.plot(x, y_abaixo, label="Curva abaixo", color="blue")

    mpl.fill_between(x, y_acima, y_abaixo, color="orange", alpha=0.3)

    mpl.legend()
    mpl.grid()
    mpl.title("Área pela Integral")
    mpl.xlabel("x")
    mpl.ylabel("y")
    mpl.show(block = False)


def mostrar_trapezios(x_nos, y_acima_nos, y_abaixo_nos):
    mpl.figure()  # abre nova janela

    # plota apenas os pontos
    mpl.plot(x_nos, y_acima_nos, marker="o", color="green", label="Acima")
    mpl.plot(x_nos, y_abaixo_nos, marker="o", color="red", label="Abaixo")

    # desenhar os trapézios
    for i in range(len(x_nos) - 1):
        xs = [x_nos[i], x_nos[i+1], x_nos[i+1], x_nos[i]]
        ys = [y_acima_nos[i], y_acima_nos[i+1], y_abaixo_nos[i+1], y_abaixo_nos[i]]

        mpl.fill(xs, ys, color="green", alpha=0.3)

    mpl.legend()
    mpl.grid()
    mpl.title("Área pelo Método dos Trapézios")
    mpl.xlabel("x")
    mpl.ylabel("y")
    mpl.show(block = False)


def pausar():
    input()
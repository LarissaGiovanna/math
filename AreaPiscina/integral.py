import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
import os
os.system("cls")

def organizar_pontos(compimentosX, largurasY):
    pontos = list(zip(compimentosX, largurasY))
    return pontos

def calcular_area_integral_por_pontos(pontos):
    # Ordena os pontos pelo valor de x
    pontos = sorted(pontos, key=lambda p: p[0])

    area = 0
    for i in range(len(pontos) - 1):
        x1, y1 = pontos[i]
        x2, y2 = pontos[i+1]

        largura = x2 - x1
        altura_media = (y1 + y2) / 2

        area += largura * altura_media

    return area

def calcular_area_integral_por_funcao(funcao, limite_inferior, limite_superior):
    X = sy.symbols('X')
    area = sy.integrate(funcao, (X, limite_inferior, limite_superior))
    print("Tipo da função:", type(funcao))
    print("Função simbólica:", funcao)
    print("Limite inferior =", limite_inferior)
    print("Limite superior =", limite_superior)
    print("Resultado da integral =", area, " | Tipo =", type(area))

    if area.has(sy.nan, sy.zoo, sy.oo):
        raise ValueError("A função contém valores indefinidos (nan, zoo ou infinito). Verifique os pontos de entrada.")

    area = area.evalf()

    return float(area) #type: ignore

# Entrada dos pontos

# pontos = []

# print("Digite os pontos no formato: x y")
# print("Para terminar, digite 'fim'.\n")

# while True:
#     entrada = input("Ponto (x y): ")

#     if entrada.lower() == "fim":
#         break

#     try:
#         x, y = map(float, entrada.split())
#         pontos.append((x, y))
#     except:
#         print("Formato inválido! Digite no formato: x y (ex: 2 3.5)")
#         continue

# # Verifica se tem pontos suficientes

# if len(pontos) < 2:
#     print("\nERRO: É necessário pelo menos 2 pontos para formar área.")
#     exit()

# # Cálculo da área

# area = calcular_area_por_integral(pontos)

# print("\n-----------------------------------")
# print("Pontos usados:")
# for p in pontos:
#     print(p)

# print("\nÁrea aproximada =", area)
# print("-----------------------------------\n")


# Plotar os pontos e a curva

# pontos = sorted(pontos, key=lambda p: p[0])
# xs = [p[0] for p in pontos]
# ys = [p[1] for p in pontos]

# plt.figure(figsize=(8,5))
# plt.plot(xs, ys, marker='o')
# plt.title("Curva formada pelos pontos inseridos")
# plt.xlabel("x")
# plt.ylabel("y")

# # mostrar rótulos (x, y)

# for x, y in pontos:
#     plt.text(x, y, f"({x}, {y})", fontsize=9, ha="right", va="bottom")

# plt.grid(True)
# plt.show()

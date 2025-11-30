import sympy as sy
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

    if area.has(sy.nan, sy.zoo, sy.oo):
        raise ValueError("A função contém valores indefinidos (nan, zoo ou infinito). Verifique os pontos de entrada.")

    area = area.evalf()

    return float(area) #type: ignore

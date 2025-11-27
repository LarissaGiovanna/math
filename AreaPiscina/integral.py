import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")

def calcular_area_por_integral(pontos):
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

# Entrada dos pontos

pontos = []

print("Digite os pontos no formato: x y")
print("Para terminar, digite 'fim'.\n")

while True:
    entrada = input("Ponto (x y): ")

    if entrada.lower() == "fim":
        break

    try:
        x, y = map(float, entrada.split())
        pontos.append((x, y))
    except:
        print("Formato inválido! Digite no formato: x y (ex: 2 3.5)")
        continue

# Verifica se tem pontos suficientes

if len(pontos) < 2:
    print("\nERRO: É necessário pelo menos 2 pontos para formar área.")
    exit()

# Cálculo da área

area = calcular_area_por_integral(pontos)

print("\n-----------------------------------")
print("Pontos usados:")
for p in pontos:
    print(p)

print("\nÁrea aproximada =", area)
print("-----------------------------------\n")


# Plotar os pontos e a curva

pontos = sorted(pontos, key=lambda p: p[0])
xs = [p[0] for p in pontos]
ys = [p[1] for p in pontos]

plt.figure(figsize=(8,5))
plt.plot(xs, ys, marker='o')
plt.title("Curva formada pelos pontos inseridos")
plt.xlabel("x")
plt.ylabel("y")

# mostrar rótulos (x, y)

for x, y in pontos:
    plt.text(x, y, f"({x}, {y})", fontsize=9, ha="right", va="bottom")

plt.grid(True)
plt.show()

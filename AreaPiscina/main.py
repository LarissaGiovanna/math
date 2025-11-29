import os
os.system("cls")

#Entrada dos dados (obviamente)

print("Quantos pares ordenados (x, y) teremos?")
print("[X = comprimento da piscina | Y = largura da piscina]")

numeroDePontos = int(input())

comprimentosX= []
largurasY= []

for i in range (numeroDePontos):

    comprimento = float(input(f"X{i+1} (comprimento): "))
    largura = float(input(f"Y{i+1} (largura): "))

    comprimentosX.append(comprimento)
    largurasY.append(largura)

print("Valores coletados:")
print(comprimentosX)
print(largurasY)

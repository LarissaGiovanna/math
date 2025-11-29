import os
import lagrange as lagrange
import integral
os.system("cls")
#import trapezio

#Entrada dos dados (obviamente)

print("Quantos pares ordenados (x, y) teremos?")
print("[X = comprimento da piscina | Y = largura da piscina]")

numeroDePontosAcima = int(input("Quantidade de pontos ACIMA do eixo X"))
numeroDePontosAbaixo = int(input("Quantidade de pontos ABAIXO do eixo X"))

comprimentosX_acima= []
largurasY_acima= []
comprimentosX_abaixo= []
largurasY_abaixo= []

print("Digite os pontos que estão ACIMA do eixo X")
for i in range (numeroDePontosAcima):

    comprimento = float(input(f"X{i+1} (comprimento): "))
    largura = float(input(f"Y{i+1} (largura): "))

    comprimentosX_acima.append(comprimento)
    largurasY_acima.append(largura)


print("Digite os pontos que estão ABAIXO do eixo X")
for i in range (numeroDePontosAbaixo):

    comprimento = float(input(f"X{i+1} (comprimento): "))
    largura = float(input(f"Y{i+1} (largura): "))

    comprimentosX_abaixo.append(comprimento)
    largurasY_abaixo.append(largura)

print("Valores coletados ACIMA:")
print(comprimentosX_acima)
print(largurasY_acima)

print("Valores coletados ABAIXO:")
print(comprimentosX_abaixo)
print(largurasY_abaixo)

# =================== Calcular area =======================
print("De que forma que deseja calcular a área?\ni - Integral\nt - Método do Trapézio\n a - Ambas as opções")
opcao = input("Sua opção: ").lower().strip()

if opcao == "i":
    print("---- Integral ----")
    forma = input("p - Calcular com base nos pontos\nf - Calcular com base na função (Lagrange)\nOpção: ").strip()
    if forma == "p":
        pontosAcima = integral.organizar_pontos(comprimentosX_acima, largurasY_acima)
        pontosAbaixo = integral.organizar_pontos(comprimentosX_abaixo, largurasY_abaixo)

        areaAcima = integral.calcular_area_integral_por_pontos(pontosAcima)
        areaAbaixo = integral.calcular_area_integral_por_pontos(pontosAbaixo)

        areaTotal = areaAcima + abs(areaAbaixo)
        print("Área calculada pela integral (base pontos): ", areaTotal)

    elif forma == "f":
        # ============ polinomio com lagrange ==============
        # linha acima do eixo X
        funcaoAcima = lagrange.polinomio(comprimentosX_acima, largurasY_acima)
        print(funcaoAcima)

        #linha abaixo do eixo X
        funcaoAbaixo = lagrange.polinomio(comprimentosX_abaixo, largurasY_abaixo)
        print(funcaoAbaixo)
        
        areaAcima = integral.calcular_area_integral_por_funcao(funcaoAcima, limite_inferior=min(comprimentosX_acima), limite_superior=max(comprimentosX_acima))

        areaAbaixo = integral.calcular_area_integral_por_funcao(funcaoAbaixo, limite_inferior=min(comprimentosX_abaixo), limite_superior=max(comprimentosX_abaixo))

        areaTotal = areaAcima + abs(areaAbaixo)

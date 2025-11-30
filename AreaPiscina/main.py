import os
import lagrange as lagrange
import integral
import trapezio
import grafico
os.system("cls")

# ========== Entrada dos dados ==========
print("Quantos pares ordenados (x, y) teremos?")
print("[X = comprimento da piscina | Y = largura da piscina]")

numeroDePontosAcima = int(input("Quantidade de pontos ACIMA do eixo X: "))
numeroDePontosAbaixo = int(input("Quantidade de pontos ABAIXO do eixo X: "))

comprimentosX_acima= []
largurasY_acima= []
comprimentosX_abaixo= []
largurasY_abaixo= []

print("Digite os pontos que estão ACIMA do eixo X")
for i in range (numeroDePontosAcima):

    comprimento = float(input(f"x{i+1} (comprimento): "))
    largura = float(input(f"y{i+1} (largura): "))

    comprimentosX_acima.append(comprimento)
    largurasY_acima.append(largura)


print("Digite os pontos que estão ABAIXO do eixo X")
for i in range (numeroDePontosAbaixo):

    comprimento = float(input(f"x{i+1} (comprimento): "))
    largura = float(input(f"y{i+1} (largura): "))

    comprimentosX_abaixo.append(comprimento)
    largurasY_abaixo.append(largura)

print("Valores coletados ACIMA:")
print(comprimentosX_acima)
print(largurasY_acima)

print("Valores coletados ABAIXO:")
print(comprimentosX_abaixo)
print(largurasY_abaixo)

# =================== Calcular area =======================
print("De que forma que deseja calcular a área?\n i - Integral\n t - Método do Trapézio\n a - Ambas as opções")
opcao = input("Sua opção: ").lower().strip()

if opcao == "i":
    print("\n---- Integral ----")
    forma = input("p - Calcular com base nos pontos\nf - Calcular com base na função (Lagrange)\nOpção: ").strip()
    if forma == "p":
        pontosAcima = integral.organizar_pontos(comprimentosX_acima, largurasY_acima)
        pontosAbaixo = integral.organizar_pontos(comprimentosX_abaixo, largurasY_abaixo)

        areaAcima = integral.calcular_area_integral_por_pontos(pontosAcima)
        areaAbaixo = integral.calcular_area_integral_por_pontos(pontosAbaixo)

        areaTotal = areaAcima + abs(areaAbaixo)
        print(f"Área calculada pela integral (base pontos): {areaTotal:.5f}")

    elif forma == "f":
        # ============ polinomio com lagrange ==============
        # linha acima do eixo X
        funcaoAcima = lagrange.polinomio(comprimentosX_acima, largurasY_acima)
        print("Polinômio acima:",funcaoAcima)

        #linha abaixo do eixo X
        funcaoAbaixo = lagrange.polinomio(comprimentosX_abaixo, largurasY_abaixo)
        print("Polinômio abaixo:",funcaoAbaixo)
        
        areaAcima = integral.calcular_area_integral_por_funcao(funcaoAcima, limite_inferior=min(comprimentosX_acima), limite_superior=max(comprimentosX_acima))

        areaAbaixo = integral.calcular_area_integral_por_funcao(funcaoAbaixo, limite_inferior=min(comprimentosX_abaixo), limite_superior=max(comprimentosX_abaixo))

        areaTotal = areaAcima + abs(areaAbaixo)
        print(f"Área calculada pela integral (base função): {areaTotal:.5f}")
    
            # ---- grafico ----
        x_medio, y_suave_acima, y_suave_abaixo = grafico.organizar_grafico(funcaoAcima, funcaoAbaixo, comprimentosX_acima, comprimentosX_abaixo)

        grafico.mostrar_integral(x_medio, y_suave_acima, y_suave_abaixo)

        grafico.pausar()

# ------- trapezio ---------
elif opcao == "t":
    print("---- Trapézio ----")
    if numeroDePontosAcima <= 2 and numeroDePontosAbaixo <= 2:
        areaAcima = trapezio.trapezio_simples(comprimentosX_acima, largurasY_acima)
        areaAbaixo = trapezio.trapezio_simples(comprimentosX_abaixo, largurasY_abaixo)

        areaTotal = areaAcima + abs(areaAbaixo)
        print(f"Área calculada pelo método do trapézio: {areaTotal:.5f}")
    else:
        areaAcima = trapezio.trapezio_composto(comprimentosX_acima, numeroDePontosAcima,largurasY_acima)
        areaAbaixo = trapezio.trapezio_composto(comprimentosX_abaixo, numeroDePontosAbaixo,largurasY_abaixo)

        areaTotal = areaAcima + abs(areaAbaixo)
        print(f"Área calculada pelo método do trapézio: {areaTotal:.5f}")

    # ----- grafico -----
    grafico.mostrar_trapezios(comprimentosX_acima, largurasY_acima,
                          largurasY_abaixo)
    grafico.pausar()

# ---- ambos ----
elif opcao == "a":
        funcaoAcima = lagrange.polinomio(comprimentosX_acima, largurasY_acima)
        print("Polinômio acima:",funcaoAcima)

        #linha abaixo do eixo X
        funcaoAbaixo = lagrange.polinomio(comprimentosX_abaixo, largurasY_abaixo)
        print("Polinômio abaixo:",funcaoAbaixo)
        
        areaAcima = integral.calcular_area_integral_por_funcao(funcaoAcima, limite_inferior=min(comprimentosX_acima), limite_superior=max(comprimentosX_acima))

        areaAbaixo = integral.calcular_area_integral_por_funcao(funcaoAbaixo, limite_inferior=min(comprimentosX_abaixo), limite_superior=max(comprimentosX_abaixo))

        areaIntegralTotal = areaAcima + abs(areaAbaixo)
        print(f"Área calculada pela integral (base função): {areaIntegralTotal:.5f}")

        
        if numeroDePontosAcima <= 2 and numeroDePontosAbaixo <= 2:
            areaAcima = trapezio.trapezio_simples(comprimentosX_acima, largurasY_acima)
            areaAbaixo = trapezio.trapezio_simples(comprimentosX_abaixo, largurasY_abaixo)

            areaTrapezioTotal = areaAcima + abs(areaAbaixo)
            print(f"Área calculada pelo método do trapézio: {areaTrapezioTotal:.5f}")
        else:
            areaAcima = trapezio.trapezio_composto(comprimentosX_acima, numeroDePontosAcima,largurasY_acima)
            areaAbaixo = trapezio.trapezio_composto(comprimentosX_abaixo, numeroDePontosAbaixo,largurasY_abaixo)

            areaTrapezioTotal = areaAcima + abs(areaAbaixo)
            print(f"Área calculada pelo método do trapézio: {areaTrapezioTotal:.5f}")

        # ----- comparação -----
        diferenca = abs(areaIntegralTotal - areaTrapezioTotal)
        print(f"Houve uma diferença de {diferenca:.5f}m² entre a área calculada por Integral e pelo Método do Trapézio.")

        # ---- grafico ----

        x_medio, y_suave_acima, y_suave_abaixo = grafico.organizar_grafico(funcaoAcima, funcaoAbaixo, comprimentosX_acima, comprimentosX_abaixo)

        grafico.mostrar_integral(x_medio, y_suave_acima, y_suave_abaixo)

        grafico.mostrar_trapezios(comprimentosX_acima, largurasY_acima, largurasY_abaixo)

        grafico.pausar()
    
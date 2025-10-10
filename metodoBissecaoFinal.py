#testes
    #x**3 + sin(x) [-1, 1]
    #x**2 + 2 [0, 1]
    #x**2 - cos(x) [0.5, 1]
    #(x/2)**2 + sin(x) [-2, -1]
    #3*x**4 - x + 3 [5, 1]
    #sin(x) + cos(x) - (3/x) [-2, -3]

import os
os.system("cls")
from matplotlib import pyplot as mpl
import numpy
import sympy

print("===== Método da Bisseção =====")

#transformação string na função
x = sympy.symbols('x')
funcao = input("Digite uma função f(x): ")
funcao_digitada = sympy.sympify(funcao)
f = sympy.lambdify(x, funcao_digitada, "numpy") #função

intervalo = [] #pessoa digita um intervalo(array)
intervalo.append(float(input("Digite o valor de 'a' (início do intervalo): ")))
intervalo.append(float(input("Digite o valor de 'b' (fim do intervalo): ")))

a = intervalo[0]
b = intervalo[1]

parada = float(input("Digite o critério de parada: "))

tentativasX =[]
tentativasY = []
print("\n===== Infos =====")
print(f"- Intervalo: {intervalo}")
print(f"- Critério de parada: {parada}")
print(f"- Função: {funcao}")

#calcular a média dos pontos
def mediaPontos(a, b):
    media = (a+b)/2
    return media

#comparar os pontos e saber qual deve ser substituido
def comparacaoPontos(a, b, xMedio):
    if f(a) > 0 and f(b) < 0 and f(xMedio) > 0 or f(a) < 0 and f(b) > 0 and f(xMedio) < 0:
        a = xMedio
        print("O ponto 'a' foi substituido\n")
        resultado = ["a", a]
        tentativasX.append(a)
        tentativasY.append(f(a))
        return resultado
    
    elif f (a) < 0 and f(b) > 0 and f(xMedio) > 0 or f(a) > 0 and f(b) < 0 and f(xMedio) < 0:
        b = xMedio
        print("O ponto 'b' foi substituido\n")
        resultado = ["b", b]
        tentativasX.append(b)
        tentativasY.append(f(b))
        return resultado
    
    else:
        resultado = "Não foi possivel achar uma raíz real nesse intervalo"
        return resultado

#calcular o módulo
def modulo(x):
    moduloX = x 
    if moduloX < 0: 
        moduloX = moduloX * (-1) # se x der negativo, multiplica por -1 e o valor fica positivo
    return moduloX 

i = 1
#looping
while (True):
    print(f"===== {i}ª Interação =====")
    print(f"a = {a}")
    print(f"b = {b}")

    #calcular a média dos intervalos
    xMedio = mediaPontos(a, b)
    print(f"xMédio = {xMedio}")
    
    print(f"f(a) = {f(a)}")
    print(f"f(b) = {f(b)}")
    print(f"f(xMedio) = {f(xMedio)}")

    #imagem da media
    ImagemXMedio = f(xMedio)

    #calcular modulo da imagem
    moduloImagem = modulo(ImagemXMedio)

    #verificação do critério de parada
    if moduloImagem > parada:
        print(f"|f(xMedio)| não atingiu o critério de parada (<= {parada})")
        comparacao = comparacaoPontos(a, b, xMedio)
        if comparacao[0] == "a": 
            a = comparacao[1] #substituição do novo a
            i = i + 1
        elif comparacao[0] == "b":
            b = comparacao[1] #novo b
            i = i + 1
        else:
            print(f"{comparacao}")
            xMedio = None
            i = i + 1
            break
    else:
        print(f"f(xMedio) = {f(xMedio)}")
        print(f"|f(xMedio)| atingiu o critério de parada (<= {parada})")
        print(f"Quantidade de interações: {i}")
        print(f"Raíz encontrada: {xMedio}")
        break #se atingir o criterio de parada, encerrra

#grafico
opcao = input("Quer o gráfico? (s/n) ")
if opcao == 's':
    x = numpy.linspace(intervalo[0], intervalo[1], 1000) #definição do eixo x
    y = f(x) #funcao que determina o y
    fig, axe = mpl.subplots(figsize=(7, 4)) #tamanho da figura
    axe.plot([intervalo[0],intervalo[1]], [0,0], color="gray") #linha que passa pelo eixo x

    #formatação/estilo do grafico
    for i in range(len(tentativasX)):
        axe.plot([tentativasX[i], tentativasX[i]], [0, tentativasY[i]], color="gray", linestyle="--") #linha tracejada vertical do x pro y
        axe.plot(tentativasX[i], tentativasY[i], marker="o", color="gray") #bolinha pra marcar o ponto

        #formatação do texto
        if tentativasX[i] > 0:
            axe.text(tentativasX[i], -0.05, f"{i+1}ºx = {tentativasX[i]}", fontsize="7")
        else:
            axe.text(tentativasX[i], 0.01, f"{i+1}ºx = {tentativasX[i]}", fontsize="7")

    #se tiver xMedio/for encontrado uma raiz
    if type(xMedio) is float or type(xMedio) is int:
        axe.plot([xMedio, xMedio], [0, f(xMedio)]) #linha verical da raiz encontrada
        axe.plot(xMedio, f(xMedio), marker="o", color="blue") #bolinha

        #formatação de texto
        if xMedio > 0:
            axe.text(xMedio, -0.05, f"{len(tentativasX)+1}ºx = {xMedio}", fontsize="7", color="blue")
        else:
            axe.text(xMedio, 0.01, f"{len(tentativasX)+1}ºx = {xMedio}", fontsize="7", color="blue")

    axe.plot(x, y) #criar o grafico
    mpl.show() #mostrar o grafico
else:
    print("ok")
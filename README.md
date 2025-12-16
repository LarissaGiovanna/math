# Método da bisseção

Esse repositório contém um programa em Python que encontra uma raíz aproximada de uma função utilizando o Método da Bisseção.

O Método consiste em analisar dois intervalos, achar a média entre eles, comparar e tentar se aproximar o mais perto possível da raíz exata.

## Como executar:
1. Baixe o arquivo metodoBissecao.py no seu computador.
2. Abra o arquivo com sua IDE de preferência. 
3. Instale as bibliotecas necessárias através do terminal executando esse código:
```bash
  pip install mathplotlib | pip install sympy
```
4. Agora rode o código e insira as instruções que o programa pedir.

OBS.: Caso queira alguns exemplos de entradas de funções, veja o arquivo [metodoBissecao-exemplos.txt](https://github.com/LarissaGiovanna/math/blob/main/metodoBisseção-exemplos.txt).

## Elementos envolvidos:
- Condicionais (`if`, `elif` e `else`)
- Estruturas de repetições (`while`);
- Listas `[]`;
- Funções (`def`):
- Importação de bibliotecas externas:
    - [Mathplotlib](https://matplotlib.org)
    - [Sympy](https://www.sympy.org/en/index.html)
    - [Numpy](https://numpy.org)

## Como funciona o cálculo:
O programa pede para o usuário inserir uma função, um intervalo A e um intervalo B e um critério de parada (ex.: 0.01). 

Após isso, o programa calcula a média entre os dois pontos e calcula a imagem do ponto A, do ponto B e do ponto médio. Depois, ele compara se as imagens deram positivas ou negativas e verifica se é possivel encontrar uma raíz nesse intervalo. 

Caso seja possivel, ele vai substituir os pontos e vai fazendo novamente esses cálculos em looping até que a imagem do ponto médio seja menor ou igual ao critério de parada estabelecido pelo usuário.

## Como foi o processo de desenvolvimento:
Esse projeto foi uma atividade avaliativa em grupo que foi passada pelo nosso professor da cadeira de Matemática para Computação do 1º período.

No nosso grupo haviam 3 pessoas e separamos as partes do código e atribuímos a cada participante. Vimos que poderíamos colocar algumas funcionalidades a mais como uma representação gráfica e dar um diferencial. Quando todos terminaram suas partes, juntamos nosso código em um só.
OBS.: Não chegamos a utilizar o Git e o GitHub nesse processo.

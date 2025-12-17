# 📐 Math - Projetos de Cálculo

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Math-Numerical%20Calculus-green.svg" alt="Numerical Calculus">
</p>

## 📚 Sobre o Repositório

Este repositório reúne implementações práticas de **métodos numéricos e conceitos de Cálculo** desenvolvidos durante a disciplina **Matemática para Computação (Cálculo 1)** do 1º período. 

O objetivo principal é **aplicar teoria matemática na prática**, transformando conceitos abstratos em soluções computacionais para problemas reais, utilizando Python e suas poderosas bibliotecas científicas.

## 📋 Sumário

- [Projetos](#-projetos)
  - [1. Método da Bisseção](#1-método-da-bisseção)
  - [2. AreaPiscina - Cálculo de Área de Piscinas Irregulares](#2-areapiscina---cálculo-de-área-de-piscinas-irregulares)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Começar](#-como-começar)
- [Equipe](#-equipe)
- [Contribuições](#-contribuições)

## 🎯 Projetos

### 1. Método da Bisseção

**📁 Localização:** `/MetodoBissecao`

#### Sobre
Programa em Python que encontra uma **raiz aproximada de uma função** utilizando o **Método da Bisseção**. 

O Método consiste em analisar dois intervalos, calcular a média entre eles, comparar os resultados e tentar se aproximar o mais perto possível da raiz exata através de iterações sucessivas.

#### Como Funciona o Cálculo

1. O usuário insere: 
   - Uma função matemática
   - Um intervalo inicial A
   - Um intervalo inicial B
   - Um critério de parada (tolerância, ex.: 0.01)

2. O programa calcula:
   - A média entre os dois pontos (ponto médio)
   - A imagem (valor da função) nos pontos A, B e no ponto médio
   - Compara se as imagens são positivas ou negativas

3. Processo iterativo:
   - Substitui os intervalos baseado nas comparações
   - Repete o cálculo em loop
   - Para quando a imagem do ponto médio é menor ou igual ao critério de parada

#### Como Executar

1. Baixe o arquivo `metodoBissecao.py` no seu computador
2. Abra o arquivo com sua IDE de preferência
3. Instale as bibliotecas necessárias: 
```bash
pip install matplotlib sympy numpy
```
4. Execute o código e insira as instruções solicitadas

**💡 Dica:** Para exemplos de funções, consulte o arquivo [metodoBissecao-exemplos.txt](https://github.com/LarissaGiovanna/math/blob/main/metodoBisseção-exemplos.txt).

#### Elementos Implementados

- Condicionais (`if`, `elif` e `else`)
- Estruturas de repetição (`while`)
- Listas `[]`
- Funções (`def`)
- Bibliotecas externas: 
  - [Matplotlib](https://matplotlib.org) - Visualização gráfica
  - [SymPy](https://www.sympy.org/en/index.html) - Matemática simbólica
  - [NumPy](https://numpy.org) - Computação numérica

#### Processo de Desenvolvimento

Este projeto foi uma **atividade avaliativa em grupo** da cadeira de Matemática para Computação do 1º período. O grupo tinha 3 pessoas e cada uma ficou responsável por partes específicas do código.  Foram adicionadas funcionalidades extras, como representação gráfica e melhorias na interface. 

*OBS.: Este foi um projeto inicial, desenvolvido antes da adoção do Git/GitHub.*

---

### 2. AreaPiscina - Cálculo de Área de Piscinas Irregulares

**📁 Localização:** `/AreaPiscina`

#### Sobre

Aplicação em Python que calcula a **área de piscinas com formatos irregulares** utilizando métodos numéricos avançados.  O programa permite inserir pontos que definem o contorno da piscina e calcula a área através de diferentes métodos matemáticos, comparando resultados e gerando visualizações gráficas. 

Desenvolvido em grupo como aplicação prática dos conhecimentos de Cálculo 1.

#### Metodologia

1. **Captura da Imagem**: Utilização de uma imagem aérea de uma piscina real
2. **Posicionamento no Plano Cartesiano**: A imagem é posicionada em um sistema de coordenadas
3. **Marcação de Pontos**: Identificação de pontos das extremidades (acima e abaixo do eixo X)
4. **Entrada de Dados**: Os pontos são inseridos no programa
5. **Geração da Função**: Cálculo da função interpoladora usando Lagrange
6. **Cálculo da Área**: Integral definida para obter a área
7. **Comparação**:  Cálculo paralelo usando o Método do Trapézio

#### Métodos Implementados

##### 🔹 Interpolação de Lagrange
- Gera um **polinômio interpolador** que passa por todos os pontos fornecidos
- Transforma medições pontuais em uma função matemática contínua
- Arquivo:  `lagrange.py`

##### 🔹 Cálculo por Integral
- **Por pontos**: Regra do trapézio básica entre pontos consecutivos
- **Por função**: Integra o polinômio de Lagrange (integral definida)
- Fornece resultado preciso baseado na função contínua
- Arquivo: `integral.py`

##### 🔹 Método do Trapézio
- **Trapézio Simples**: Para 2 pontos
- **Trapézio Composto**: Para múltiplos pontos
- Calcula área diretamente dos pontos, sem interpolação
- Permite comparação de precisão
- Arquivo: `trapezio.py`

##### 🔹 Visualização Gráfica
- Gráfico da área calculada por integral (com preenchimento)
- Gráfico dos trapézios formados
- Facilita comparação visual entre métodos
- Arquivo: `grafico. py`

#### Estrutura do Projeto

```
AreaPiscina/
│
├── main.py           # Arquivo principal (interface e fluxo do programa)
├── lagrange.py       # Interpolação polinomial de Lagrange
├── integral.py       # Cálculo de área por integral
├── trapezio.py       # Método do Trapézio (simples e composto)
├── grafico.py        # Visualizações com Matplotlib
└── Exemplos/         # Pasta com exemplos de uso
```

#### Como Executar

1. Clone o repositório: 
```bash
git clone https://github.com/LarissaGiovanna/math.git
cd math/AreaPiscina
```

2. Instale as dependências:
```bash
pip install sympy numpy matplotlib
```

3. Execute o programa:
```bash
python main.py
```

4. Siga as instruções no terminal: 
   - Informe a quantidade de pontos acima e abaixo do eixo X
   - Digite as coordenadas (x, y) de cada ponto
   - Escolha o método de cálculo: 
     - `i` - Integral
     - `t` - Método do Trapézio
     - `a` - Ambos (com comparação)

#### Exemplo de Uso

```
Quantos pares ordenados (x, y) teremos?
[X = comprimento da piscina | Y = largura da piscina]
Quantidade de pontos ACIMA do eixo X:  3
Quantidade de pontos ABAIXO do eixo X:  3

Digite os pontos que estão ACIMA do eixo X
x1 (comprimento): 0
y1 (largura): 2
x2 (comprimento): 2
y2 (largura): 4
x3 (comprimento): 4
y3 (largura): 2

Digite os pontos que estão ABAIXO do eixo X
x1 (comprimento): 0
y1 (largura): -1
x2 (comprimento): 2
y2 (largura): -2
x3 (comprimento): 4
y3 (largura): -1

De que forma que deseja calcular a área?
 i - Integral
 t - Método do Trapézio
 a - Ambas as opções
Sua opção: a
```

#### Funcionalidades

✅ Cálculo de área por diferentes métodos numéricos  
✅ Suporte para formas irregulares (pontos acima e abaixo do eixo X)  
✅ Geração automática de polinômios interpoladores  
✅ Comparação entre métodos (Integral vs.  Trapézio)  
✅ Visualização gráfica interativa  
✅ Interface de linha de comando intuitiva  
✅ Análise de diferença de precisão entre métodos  

#### Conceitos Matemáticos

**Interpolação de Lagrange:**
```
P(x) = Σ[i=0 até n] yi · Li(x)
```

**Integral Definida:**
```
A = ∫[a até b] P(x) dx
```

**Método do Trapézio Composto:**
```
A ≈ (h/2) · [f(x0) + 2·Σf(xi) + f(xn)]
```

#### Saída do Programa

1. **Polinômios interpoladores** (quando usa Lagrange)
2. **Área calculada** por cada método escolhido
3. **Diferença entre métodos** (quando escolhe opção "a")
4. **Gráficos interativos** mostrando: 
   - Curvas interpoladas
   - Áreas preenchidas
   - Trapézios formados
5. **Comparação visual e numérica**

#### Aprendizados

Este projeto foi **muito importante e interessante**, pois permitiu: 

- ✨ **Aplicar teoria matemática na prática**
- 💻 **Integrar programação e resolução de problemas reais**
- 📊 **Visualizar graficamente conceitos abstratos de Cálculo**
- 🤝 **Trabalhar em equipe** no desenvolvimento de software
- 🔍 **Comparar diferentes métodos numéricos** e entender suas vantagens

---

## 🔧 Tecnologias Utilizadas

<table>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="50" height="50" /><br>
      <b>Python 3.x</b>
    </td>
    <td align="center">
      <img src="https://www.sympy.org/static/images/logo.png" width="50" height="50" /><br>
      <b>SymPy</b><br>
      Matemática Simbólica
    </td>
    <td align="center">
      <img src="https://numpy.org/images/logo.svg" width="50" height="50" /><br>
      <b>NumPy</b><br>
      Computação Numérica
    </td>
    <td align="center">
      <img src="https://matplotlib.org/_static/logo_dark.svg" width="50" height="50" /><br>
      <b>Matplotlib</b><br>
      Visualização de Dados
    </td>
  </tr>
</table>


## 🚀 Como Começar

### Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)

### Instalação das Dependências

```bash
pip install sympy numpy matplotlib
```

### Executando os Projetos

**Método da Bisseção:**
```bash
cd MetodoBissecao
python metodoBissecao.py
```

**AreaPiscina:**
```bash
cd AreaPiscina
python main.py
```

---

## 👥 Equipe

### Projeto AreaPiscina
- **Larissa Giovanna** - [@LarissaGiovanna](https://github.com/LarissaGiovanna)
- **Julia Tenório Calado** - [@juliatenoriocalado](https://github.com/juliatenoriocalado)
- **Gabriel Rios** - [@RiosGabri](https://github.com/RiosGabri)
- **Luis Felipe Higino** - [@LuisHigino](https://github.com/LuisHigino)

### Projeto Método da Bisseção
- **Larissa Giovanna** - [@LarissaGiovanna](https://github.com/LarissaGiovanna)
- **Julia Tenório Calado** - [@juliatenoriocalado](https://github.com/juliatenoriocalado)
- **Gabriel Rios** - [@RiosGabri](https://github.com/RiosGabri)

*Projetos desenvolvidos como parte da disciplina Matemática para Computação (Cálculo 1)*

---

## 🤝 Contribuições

Contribuições são bem-vindas!  Sinta-se à vontade para: 

- 🐛 Reportar bugs
- 💡 Sugerir novas funcionalidades
- 📝 Melhorar a documentação
- 🔧 Otimizar algoritmos existentes

Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request


## 🔗 Links Úteis

- [Documentação Python](https://docs.python.org/3/)
- [Documentação SymPy](https://docs.sympy.org/)
- [Documentação NumPy](https://numpy.org/doc/)
- [Documentação Matplotlib](https://matplotlib.org/stable/contents.html)


## 📊 Estatísticas do Repositório

![GitHub repo size](https://img.shields.io/github/repo-size/LarissaGiovanna/math)
![GitHub stars](https://img.shields.io/github/stars/LarissaGiovanna/math?style=social)
![GitHub forks](https://img.shields.io/github/forks/LarissaGiovanna/math?style=social)

<p align="center">
  ⭐ Se este projeto foi útil ou se apenas achou interessante para você, considere dar uma estrela no repositório! <br>
</p>
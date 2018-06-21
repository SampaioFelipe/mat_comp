import numpy as np
import math

'''
1.Tabela inicial:  inserir variáveis de folga
2.Solução é ótima? Há coeficiente negativo em Z?
3.Escolher var que entra: menor coef em Z
4.Escolher var que sai: menor razão não negativa
5.Computar nova linha pivô
6.Recomputar linhas em relação à nova linha pivô, voltar para 3

Forma canonica
max Z = Cx
	s.r Ax <= b
'''
# Coeficientes da função objetivo separados por espaço
funcao_objetivo = input("Coeficientes da função objetivo: ").split()

n_variaveis = len(funcao_objetivo)
n_restricoes = int(input('Quantidade restricoes: '))

linhas = n_restricoes + 1  # var de folga + Z
colunas = n_variaveis + linhas + 1  # var + var de folga + Z + constante

# Criacao da tabela com zeros
Tabela = np.zeros((linhas, colunas))
Tabela[0][0] = 1  # coluna do Z

# primeira linha da tabela
for i in range(1, n_variaveis + 1):
    Tabela[0][i] = (-1) * int(funcao_objetivo[i-1])

# Preenchimento do dicionário inicial
i = 1
while(i <= n_restricoes):
    restricao = input('Digite os coeficientes + constante da restrição ' + str(i) + ': ').split()

    # Se houver mais variáveis do que a funcao objetivo
    if len(restricao) != n_variaveis + 1:
        print("Número de variáveis incompatível. Tente novamente.")
    else:
        # Preenche os coeficientes da restrição
        for j in range(1, n_variaveis + 1):
            Tabela[i][j] = int(restricao[j-1])
        
        Tabela[i][n_variaveis + i] = 1  # variavel de folga
        Tabela[i][-1] = int(restricao[-1]) # valor da constante

        i = i + 1

print("\nDicionário Inicial\n")
print(Tabela)

def busca_negativo():
    for j in range(1, n_variaveis + 1):
        if(Tabela[0][j] < 0):
            return 1
    return 0

def var_entra():
    for j in range(1, n_variaveis + 1):
        if(Tabela[0][j] < Tabela[0][j - 1]):
            if(Tabela[0][j] != 0):
                return Tabela[0][j], j
    return Tabela[0][j -1], j-1

def var_sai(coluna):
    razao_aux = math.inf
    for i in range(1,linhas):
       if (Tabela[i][coluna] != 0): # evitar divisao por zero
            razao = Tabela[i][colunas - 1]/Tabela[i][coluna]
            if(razao < razao_aux):
                razao_aux = razao
                linha_pivo = i
    return linha_pivo

# Calcular nova linha pivo
def nova_pivo(linha, nmr):  #linha pivo / nmr pivo
    for j in range(0,colunas):
        Tabela[linha][j] = Tabela[linha][j] / nmr

# Calcular novas linhas
def nova_linha(linha, coef, linhapivo):
    for j in range(0, colunas):
        Tabela[linha][j] = Tabela[linha][j] - (Tabela[linhapivo][j] * coef)

def simplex():
    var_in, coluna_pivo = var_entra()
    print("Variavel que entra: ", var_in)
    linha_pivo = (var_sai(coluna_pivo))
    print("Linha pivo", linha_pivo)
    pivo = Tabela[linha_pivo][coluna_pivo]
    print("Pivo", pivo, "\n")
    nova_pivo(linha_pivo, pivo)
    for i in range(0, linhas):
        if i != linha_pivo:
            coef = Tabela[i][coluna_pivo]
            nova_linha(i, coef, linha_pivo)

i = 1
while(busca_negativo()):
    print("==========================================")
    print("Iteração " + str(i) + "\n")
    simplex()
    print(Tabela)
    print("\n==========================================")
    i = i + 1

resultado = {'Z': Tabela[0][-1]}

for i in range(1, linhas):
    resultado['X{}'.format(i)] = Tabela[i][-1]

print(resultado)
    
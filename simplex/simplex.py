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

import numpy as np


# Definir variaveis auxiliares
variaveis = int(input('Digite a quantidade de variaveis: '))
restricoes = int(input('Digite a quantidade de restricoes: '))

linhas = restricoes + 1  # var de folga + Z
colunas = variaveis + linhas + 1  # var + var de folga + Z + constante

# Criacao da tabela com zeros
Tabela = np.zeros((linhas, colunas))
Tabela[0][0] = 1  # coluna do Z

# primeira linha da tabela
for j in range(1, variaveis + 1):
    Tabela[0][j] = (-1) * (int(input('Digite os coeficientes da funcao objetivo: \n')))
print("Funcao objetivo preenchida com sucesso\n")

# preencher coeficientes das restricoes
def preenche_restricoes(i):
    for j in range(1, variaveis + 1):
        Tabela[i][j] = int(input('Digite os coeficientes da restricao: \n'))

for i in range(1, linhas):
    Tabela[i][variaveis + i] = 1  # variaveis de folga e constante
    preenche_restricoes(i)
    Tabela[i][colunas - 1] = int(input('Digite a constante: '))
    print("Fim da restricao", i, '\n')
print("Dicionario inicial finalizado\n")

def busca_negativo():
    for j in range(1, variaveis + 1):
        if(Tabela[0][j] < 0):
            return 1
    return 0

def var_entra():
    for j in range(1, variaveis + 1):
        if(Tabela[0][j] < Tabela[0][j - 1]):
            if(Tabela[0][j] != 0):
                return Tabela[0][j], j
    return Tabela[0][j -1], j-1

def var_sai(coluna):
    razao_aux = 1000000
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
    print("Simplex iniciando\n")
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
    print("Simplex acabando\n")

while(busca_negativo()):
    simplex()

print(Tabela)
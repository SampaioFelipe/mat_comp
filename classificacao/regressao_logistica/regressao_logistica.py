import numpy as np
import matplotlib.pyplot as plt
import sys


def classifica(dado, w):
    v = 1/(1 + np.exp(-np.dot(dado, w)))
    return 0 if v < 0.5 else 1    

def regressao_logistica(dados, classes, alpha, limiar):
    w = np.zeros(len(dados[0]))
    epoca = 0
    erro = 1
    n = len(dados)

    while erro > limiar:
        print("Época ", epoca)
        erro = 0

        for i in range(n):
            d = classes[i]
            x = dados[i]
            y = classifica(x, w)

            if y != d:
                w = w + alpha * (d - y) * x
                erro = erro + 1
        
        erro = erro/n
        print(erro)
        epoca = epoca + 1

    return w

def teste(dados, w):
    classificacao = []

    for dado in dados:
        classificacao.append(classifica(dado, w))
    
    return classificacao

if __name__ == "__main__":
    dados_raw = np.genfromtxt(sys.argv[1], delimiter=',', dtype=float, encoding='utf-8')[:,:-1]
    classes_raw = np.genfromtxt(sys.argv[1], delimiter=',', dtype=None, usecols=-1, encoding='utf-8')

    # Adiciona coluna do bias (primeira coluna com 1's)
    dados = np.hstack((np.ones((len(dados_raw), 1)), dados_raw))

    c1 = classes_raw[0]
    classes = [(0 if x==c1 else 1) for x in classes_raw]

    pesos = regressao_logistica(dados, classes, 0.1, 0.2)
    classificacao = teste(dados, pesos)

    acertos = 0
    for i in range(len(classificacao)):
        if classificacao[i] == classes[i]:
            acertos = acertos + 1
    
    print("Acertos: {}/{}".format(acertos, len(classes)))
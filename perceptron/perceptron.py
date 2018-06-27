import numpy as np
import matplotlib.pyplot as plt
from random import randint

# Classifica um dado realizando a multiplicacao pelo vetor de pesos e aplicacao da funcao de ativacao
def classifica(dado, w):
    v = np.dot(dado, w)
    # Aplicação da funcao de ativacao degrau
    return -1 if v < 0 else 1

# Produz uma coleção de dados com [bias, x, y, classe]
def gera_dados(qtd):
    # Matrix de dados: qtd x 3 (bidimensional + bias + classe)
    dados = np.zeros((2 * qtd, 4))
    
    # Classe positiva [primeiro quadrante]
    for i in range(qtd):
        dados[i, 0] = 1 # bias
        x, y = np.random.randint(100, size=2) # valores de característica
        dados[i, 1] = x
        dados[i, 2] = y
        dados[i, 3] = 1 # classe positiva
    
    # Classe negativa [terceiro quadrante]
    for i in range(qtd, 2*qtd):
        dados[i, 0] = 1 # bias
        x, y = np.random.randint(-100, 0, size=2)
        dados[i, 1] = x
        dados[i, 2] = y
        dados[i, 3] = -1 # classe positiva
    
    return dados

def plot(dados_originais, classificacao, w):
    _, ax = plt.subplots(1, 1)

    for i, dado in enumerate(dados_originais):
        ax.scatter(dado[1], dado[2], c= 'blue' if dado[3]==1 else 'red')
        ax.scatter(dado[1], dado[2], c= 'white', marker='x' if classificacao[i]==1 else '+')
    
    x0, x1 = ax.get_xlim()

    y0 = -(x0*w[2] + w[0])/w[1]
    y1 = -(x1*w[2] + w[0])/w[1]

    plt.plot([x0, x1],[y0, y1], '-')
    plt.show()



def perceptron(dados, classes, alpha):
    w = np.zeros(3)
    epoca = 0
    erro = True # criterio de parada: para quando acertar todas as amostras

    while erro:
        print("Época ", epoca)
        erro = False
        
        for i in range(len(dados)):
            d = classes[i]
            x = dados[i]

            y = classifica(x, w)

            if y != classes[i]:
                w = w + alpha * (d - y) * x
                erro = True
        
        epoca = epoca + 1
    
    return w

def teste(dados, w):
    classificacao = []

    for dado in dados:
        classificacao.append(classifica(dado, w))
    
    return classificacao

dados = gera_dados(20)
pesos = perceptron(dados[:,:3], dados[:, 3], 0.5)
classificacao = teste(dados[:,:3], pesos)

plot(dados, classificacao, pesos)
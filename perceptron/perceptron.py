import numpy as np
import matplotlib.pyplot as plt
from random import randint


# Funcao de ativacao -1 ou 1
def func_ativ(a, b):
    mult = np.multiply(a, b)
    y = 0
    for i in mult:
        for j in i:
            y = j + y
    if (y < 0):
        return -1
    else:
        return 1


# Funcao para atualizar vetor de pesos
def update_weight(w, alpha, d, x):
    w = w + alpha * (d - (func_ativ(w, x))) * x
    return w


def perceptron(d, w, alpha, value):
    classe = func_ativ(value, w)
    w = update_weight(w, alpha, d, value)
    dict = {'Vetor de dados': value, 'Classe esperada': d, 'Classe obtida': classe, 'Novo vetor de pesos': w}
    print(dict)
    print('\n')
    return w


total = randint(5, 15)

x = np.array([[1]])

# Criar vetor de pesos aleatorio
w = np.array([[3, -4, 5]])
w.astype(int)

alpha = 0.5

for i in range(total):
    # Positivos
    pos_value = np.array([np.random.randint(100, size=2)])  # Criar dados aleatorios no primeiro quadrante
    plt.scatter(pos_value[0, 0], pos_value[0, 1], c='blue')  # Plotar de azul
    pos_value = np.concatenate((x, pos_value), axis=1)  # Inserir x0
    d = 1
    w = perceptron(d, w, alpha, pos_value)

for i in range(total):
    # Negativos
    neg_value = np.array([np.random.randint(-100, 0, size=2)])  # Criar dados aleatorios no terceiro quadrante
    plt.scatter(neg_value[0, 0], neg_value[0, 1], c='red')  # Plotar de vermelho
    neg_value = np.concatenate((x, neg_value), axis=1)  # Inserir x0
    d = -1
    w = perceptron(d, w, alpha, neg_value)

#plt.plot([x1, x2], [y1, y2], color='black', linestyle='-', linewidth=2)
plt.show()

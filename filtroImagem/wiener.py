import numpy as np
import copy

def filtro(img, sigma_n=0.01, tam_janela=3):
    novo = copy.deepcopy(img)
    centro = tam_janela//2

    for i in range(centro, img.shape[0]-centro):
        linhas = list(range(i-centro, i+centro + 1))
        for j in range(centro, img.shape[1]-centro):
            colunas = list(range(j-centro, j+centro + 1))
            janela = []
            for l in linhas:
                for c in colunas:
                    janela.append(img[l][c])

            u_f = np.mean(janela)
            sigma_f = np.var(janela)
            sigma_s = max(0, sigma_f-sigma_n)
            novo[i][j] = u_f + (sigma_s/(sigma_s+sigma_n))*(img[i][j] - u_f)
            
    return novo
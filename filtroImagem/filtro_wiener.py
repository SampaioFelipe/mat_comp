import matplotlib
import matplotlib.pyplot as plt
import skimage
from skimage import io

import numpy as np

# img = io.imread('imagens/barbara_sal_e_pimenta.png', plugin='matplotlib')
img = io.imread('imagens/camera_gaussian.png', plugin='matplotlib')

def filtro_wiener(img, sigma_n=0.01, tam_janela=3):
    novo = []
    centro = tam_janela//2

    for i in range(centro, img.shape[0]-centro):
        nova_linha = []
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
            s = u_f + (sigma_s/(sigma_s+sigma_n))*(img[i][j] - u_f)

            nova_linha.append(s)

        novo.append(nova_linha)

    return novo

novo = filtro_wiener(img)

plt.figure(1)
plt.subplot(121)
io.imshow(img)

plt.subplot(122)
io.imshow(skimage.img_as_float(novo))
plt.show()
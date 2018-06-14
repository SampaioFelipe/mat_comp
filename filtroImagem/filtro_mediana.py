import matplotlib
import matplotlib.pyplot as plt
import skimage
from skimage import io

img = io.imread('imagens/man_sal_e_pimenta.png', plugin='matplotlib')
# img = io.imread('imagens/barbara_gaussian.png', plugin='matplotlib')

def filtro_mediana(img, janela=3):
    novo = []
    centro = janela//2
    qtd_janela = janela*janela
    pos_mediana = qtd_janela//2


    for i in range(centro, img.shape[0]-centro):
        nova_linha = []
        linhas = list(range(i-centro, i+centro + 1))

        for j in range(centro, img.shape[1]-centro):
            colunas = list(range(j-centro, j+centro + 1))

            valores = []
            for l in linhas:
                for c in colunas:
                    valores.append(img[l][c])
            valores.sort()
            nova_linha.append(valores[pos_mediana])

        novo.append(nova_linha)

    return novo

novo = filtro_mediana(img)

plt.figure(1)
plt.subplot(121)
io.imshow(img)

plt.subplot(122)
io.imshow(skimage.img_as_float(novo))
plt.show()
import copy

def filtro(img, janela=3):
    novo = copy.deepcopy(img)

    centro = janela//2
    qtd_janela = janela*janela
    pos_mediana = qtd_janela//2

    for i in range(centro, img.shape[0]-centro):
        linhas = list(range(i-centro, i+centro + 1))
        for j in range(centro, img.shape[1]-centro):
            colunas = list(range(j-centro, j+centro + 1))
            valores = []
            for l in linhas:
                for c in colunas:
                    valores.append(img[l][c])
            valores.sort()

            novo[i][j] = valores[pos_mediana]

    return novo
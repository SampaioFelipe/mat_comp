import matplotlib
import matplotlib.pyplot as plt
import skimage
import math
from skimage import io
from skimage import measure

import wiener
import mediana

def PSNR(original, filtrada):    
    MSE = 0
    for i in range(original.shape[0]):
        for j in range(original.shape[1]):
            MSE = MSE + (original[i][j] - filtrada[i][j])**2
    
    MSE = MSE / (original.shape[0] * original.shape[1])
    
    PSNR = 20 * math.log(1/math.sqrt(MSE), 10) # 1 pois o pixel tem valor entre [0, 1]

    return PSNR

def save_image(original, ruidosa, filtrada, destino):
    plt.figure(1, figsize=(8, 4))

    fig1 = plt.subplot(121)
    fig1.axis('off')
    fig1.set_title("PSNR={0:.2f} dB".format(PSNR(original, ruidosa)))
    io.imshow(ruidosa)

    fig2 = plt.subplot(122)
    fig2.axis('off')
    fig2.set_title("PSNR={0:.2f} dB".format(PSNR(original, filtrada)))
    io.imshow(skimage.img_as_float(filtrada))
    plt.savefig('{}.png'.format(destino), dpi=250)
    plt.close()

imagens = ['barbara', 'boat', 'camera', 'lena', 'man']

for i, imagem in enumerate(imagens):
    print('Filtrando imagem: {} ({}/{})'.format(imagem, i+1, len(imagens)))
    img_original = io.imread('imagens/{}.png'.format(imagem), plugin='matplotlib')
    img_gaussian = io.imread('imagens/{}_gaussian.png'.format(imagem), plugin='matplotlib')
    img_sal_pimenta = io.imread('imagens/{}_sal_e_pimenta.png'.format(imagem), plugin='matplotlib')

    # Aplicando filtro da mediana
    img_mediana = mediana.filtro(img_original)
    save_image(img_original, img_sal_pimenta, img_mediana, "resultados/{}_mediana".format(imagem))    

    # Aplicando o filtra de wiener
    img_wiener = wiener.filtro(img_gaussian)
    save_image(img_original, img_gaussian, img_wiener, "resultados/{}_wiener".format(imagem))    


    

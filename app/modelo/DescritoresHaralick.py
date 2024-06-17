import numpy as np
from skimage.feature import graycomatrix, graycoprops


def calcula_descritores_haralick(image_array):
    """
    Calcula os descritores de Haralick.
    :param image_array: Array da imagem.
    :return: Descritores de Haralick.
    """
    # Define os parâmetros para a GLCM
    distancia = [1]  # Distância entre os pixels
    angulos = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]  # Ângulos

    # Calcula a GLCM
    glcm = graycomatrix(image_array, distancia, angulos, 256, symmetric=True, normed=True)

    # Calcula os descritores de Haralick
    propriedades = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
    return [(propriedade, graycoprops(glcm, propriedade).mean()) for propriedade in propriedades]

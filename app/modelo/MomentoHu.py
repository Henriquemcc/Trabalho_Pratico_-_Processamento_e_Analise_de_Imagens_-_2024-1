import cv2
import numpy as np


def calculate_hu_moments(image_array):
    """
    Calcula os momentos de Hu de uma imagem.
    :param image_array: Array da imagem.
    :return: Momentos invariantes de Hu.
    """
    # Calcular os momentos
    moments = cv2.moments(image_array)

    # Calcular os momentos invariantes de Hu
    hu_moments = cv2.HuMoments(moments)

    # Log-transforma os momentos de Hu para melhor interpretação
    for i in range(0, 7):
        hu_moments[i] = -np.sign(hu_moments[i]) * np.log10(abs(hu_moments[i]))

    return hu_moments

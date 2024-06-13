import os

import joblib
import numpy

from .imagem import Imagem
from .imagem_hsv import ImagemHSV
from .imagem_rgb import ImagemRGB
from .imagem_tons_cinza import ImagemTonsCinza


class SVM:
    """
    Implementa um classificador Svm (Support Vector Machine).
    """

    def __init__(self):
        """
        Construtor da classe.
        """
        self.modelo = joblib.load("./inteligencia/svm.pkl")

    def __pre_processar(self, imagem: Imagem):
        """
        Realiza o pré-processamento da imagem.
        :param imagem: Imagem a ser pré-processada.
        :return: Imagem pré-processada.
        """

        # Convertendo para tons de cinza
        if isinstance(imagem, ImagemRGB) or isinstance(imagem, ImagemHSV):
            imagem = ImagemTonsCinza.from_image(imagem)

        # Redimensionando a imagem
        return imagem.matriz.ravel()

    def predict(self, imagem: Imagem):
        """
        Realiza a predição da imagem.
        :param imagem: Imagem a ser classificada.
        :return: Classe da imagem.
        """
        imagem = self.__pre_processar(imagem)
        return self.modelo.predict(numpy.array([imagem]))[0]

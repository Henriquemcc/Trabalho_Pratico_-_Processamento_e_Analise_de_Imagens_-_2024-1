import numpy
from tensorflow.python.keras.models import load_model
import PIL

from .classificador import Classificador
from .imagem import Imagem
from .imagem_hsv import ImagemHSV
from .imagem_rgb import ImagemRGB
from .imagem_tons_cinza import ImagemTonsCinza


class Svm(Classificador):
    """
    Implementa um classificador Svm (Support Vector Machine).
    """

    def pre_processar(self, imagem: Imagem):
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

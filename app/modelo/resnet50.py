import numpy
from tensorflow.keras.applications.resnet50 import preprocess_input

from .classificador import Classificador
from .imagem_hsv import ImagemHSV
from .imagem_rgb import ImagemRGB
from .imagem_tons_cinza import ImagemTonsCinza


class Resnet50(Classificador):
    """
    Implementa um classificador ResNet50.
    """

    def pre_processar(self, imagem: ImagemRGB):
        """
        Realiza o pré-processamento da imagem.
        :param imagem: Imagem a ser pré-processada.
        :return: Imagem pré-processada.
        """
        if isinstance(imagem, ImagemTonsCinza):
            raise "Imagem em tons de cinza não é suportada."

        if isinstance(imagem, ImagemHSV):
            raise "Imagem em HSV não é suportada."

        # Redimensionando a imagem
        return preprocess_input(numpy.array(imagem.to_image().resize((224, 224))))

import numpy
from tensorflow.keras.applications.resnet50 import preprocess_input
from .imagem_hsv import ImagemHSV
from .imagem_rgb import ImagemRGB
from .imagem_tons_cinza import ImagemTonsCinza
from tensorflow.keras.models import load_model


class Resnet50:
    """
    Implementa um classificador ResNet50.
    """

    def __init__(self):
        """
        Construtor da classe.
        """
        self.modelo = load_model("./app/inteligencia/resnet50.h5")

    def __pre_processar(self, imagem: ImagemRGB):
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

    def predict(self, imagem: ImagemRGB):
        """
        Realiza a predição da imagem.
        :param imagem: Imagem a ser classificada.
        :return: Classe da imagem.
        """
        imagem = self.__pre_processar(imagem)
        return self.modelo.predict(numpy.array([imagem]))[0]

import numpy
from tensorflow.keras.applications.resnet50 import preprocess_input
from .imagem_hsv import ImagemHSV
from .imagem_rgb import ImagemRGB
from .imagem_tons_cinza import ImagemTonsCinza
from tensorflow.keras.models import load_model
import os


class Resnet50:
    """
    Implementa um classificador ResNet50.
    """

    def __init__(self):
        """
        Construtor da classe.
        """
        caminho_modelo = "inteligencia/resnet50.h5"
        if os.path.exists(caminho_modelo):
            self.modelo = load_model(caminho_modelo)
        else:
            os.makedirs(os.path.dirname(caminho_modelo), exist_ok=True)
            print("Modelo não encontrado. Adicione o modelo em {}".format(caminho_modelo))

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

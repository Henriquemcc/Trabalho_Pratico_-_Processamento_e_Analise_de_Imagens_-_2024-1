import numpy
from tensorflow.python.keras.models import load_model
import PIL

from modelo.classificador import Classificador


class Svm(Classificador):
    """
    Implementa um classificador Svm (Support Vector Machine).
    """

    def __init__(self, model_path):
        """
        Constrói um modelo Svm.
        :param model_path: Caminho do arquivo com o modelo a ser carregado.
        """
        super().__init__()
        self.modelo = load_model(model_path)

    def pre_processar(self, image_path):
        """
        Realiza o pré-processamento da imagem.
        :param image_path: Caminho da imagem a ser pré-processada.
        :return: Imagem pré-processada.
        """
        return numpy.array(PIL.Image.open(image_path).convert('L')).ravel()

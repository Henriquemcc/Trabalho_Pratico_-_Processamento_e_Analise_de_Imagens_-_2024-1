import PIL
import numpy
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input

from modelo.classificador import Classificador


class Resnet50(Classificador):
    """
    Implementa um classificador ResNet50.
    """

    def __init__(self, model_path):
        """
        Constrói um modelo ResNet50.
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
        return preprocess_input(numpy.array(PIL.Image.open(image_path).convert('RGB').resize((224, 224))))
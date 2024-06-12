from tensorflow.keras.models import load_model

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
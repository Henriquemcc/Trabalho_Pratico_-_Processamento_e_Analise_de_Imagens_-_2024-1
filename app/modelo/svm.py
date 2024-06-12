from tensorflow.python.keras.models import load_model

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


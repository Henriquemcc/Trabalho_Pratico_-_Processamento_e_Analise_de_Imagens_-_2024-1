from modelo.imagem import Imagem
from modelo.imagem_rgb import ImagemRGB


class Classificador:
    """
    Super classe de Resnet50 e Svm.
    """

    def __init__(self, modelo):
        """
        Constrói uma nova instância da classe Classificador.
        :param modelo: Modelo a ser utilizado.
        """
        self.modelo = modelo

    def pre_processar(self, imagem: Imagem):
        """
        Realiza o pré-processamento da imagem a ser utilizada para treinar o ser predita pelo modelo.
        :param imagem: ImagemRGB a ser pré-processada.
        :return: Imagem pré-processada.
        """
        pass

    def perdict(self, *args, **kwargs):
        """
        Realiza uma predição utilizando o modelo.
        :param args: Argumentos a serem passados à classe 'predict' do modelo.
        :return: Valor da predição.
        """
        return self.modelo.predict(*args, **kwargs)

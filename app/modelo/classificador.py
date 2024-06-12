class Classificador:
    """
    Super classe de Resnet50 e Svm.
    """

    def __init__(self):
        """
        Constrói uma nova instância da classe Classificador.
        """
        self.modelo = None

    def pre_processar(self, image_path):
        """
        Realiza o pré-processamento da imagem a ser utilizada para treinar o ser predita pelo modelo.
        :param image_path: Caminho da imagem a ser pré-processada.
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

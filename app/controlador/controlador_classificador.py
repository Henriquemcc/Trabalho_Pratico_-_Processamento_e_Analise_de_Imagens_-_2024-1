import numpy

from modelo.classifier_types import ClassifierTypes
from modelo.resnet50 import Resnet50
from modelo.svm import SVM


class ControladorClassificador:
    """
    Controlador responsável pelo modelo.
    """

    def __init__(self):
        """
        Constrói uma nova instância de ControladorModelo
        :param parent_controller: Controlador pai.
        """

        # Tipo de classificacao
        self.__tipo_classificacao = ClassifierTypes.MULTICLASS

        # Modelo a ser utilizado
        self.modelo_svm = SVM()
        self.modelo_resnet = Resnet50()

        # Labels
        self.labels = ['ASC-H','ASC-US','HSIL','LSIL','Negative for intraepithelial lesion','SCC']

    def __classificar(self, imagem, out_label, modelo):
        """
        Realiza a classificação da imagem.
        :return:
        """
        resultado = modelo.predict(imagem)
        resultado = numpy.argmax(resultado)
        out_label.config(text=self.labels[resultado])

    def classificar_svm(self, imagem, out_label):
        """
        Realiza a classificação da imagem utilizando o SVM.
        :return:
        """
        return self.__classificar(imagem, out_label, self.modelo_svm)

    def classificar_resnet(self, imagem, out_label):
        """
        Realiza a classificação da imagem utilizando o ResNet50.
        :return:
        """
        return self.__classificar(imagem, out_label, self.modelo_resnet)

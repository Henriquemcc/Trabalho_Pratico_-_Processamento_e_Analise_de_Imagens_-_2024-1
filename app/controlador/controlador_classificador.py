import time

import numpy

from modelo.classifier_types import ClassifierTypes
from modelo.resnet50 import Resnet50
from modelo.svm import SVM


class ControladorClassificador:
    """
    Controlador responsável pelo modelo de classificação.
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
        self.labels = ['ASC-H', 'ASC-US', 'HSIL', 'LSIL', 'Negative for intraepithelial lesion', 'SCC']
        self.binary_labels = ['Com câncer', 'Sem câncer']
        self.negative_result = 4

    def __classificar(self, imagem, out_label, modelo, label_tempo, classifier_type=ClassifierTypes.MULTICLASS):
        """
        Realiza a classificação da imagem.
        :return:
        """
        labels = self.labels
        tempo_inicio = time.time_ns()
        resultado = modelo.predict(imagem)
        tempo_fim = time.time_ns()
        resultado = numpy.argmax(resultado)
        if classifier_type == ClassifierTypes.BINARY:
            resultado = 1 if resultado == self.negative_result else 0
            labels = self.binary_labels
        out_label.config(text=labels[resultado])
        tempo_gasto = tempo_fim - tempo_inicio
        label_tempo.config(text="Tempo gasto: {}ns".format(tempo_gasto))

    def classificar_svm(self, imagem, out_label, label_tempo, classifier_type=ClassifierTypes.MULTICLASS):
        """
        Realiza a classificação da imagem utilizando o SVM.
        :return:
        """
        return self.__classificar(imagem, out_label, self.modelo_svm, label_tempo, classifier_type)

    def classificar_resnet(self, imagem, out_label, label_tempo, classifier_type=ClassifierTypes.MULTICLASS):
        """
        Realiza a classificação da imagem utilizando o ResNet50.
        :return:
        """
        return self.__classificar(imagem, out_label, self.modelo_resnet, label_tempo, classifier_type)

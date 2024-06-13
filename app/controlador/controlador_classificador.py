import enum
from tkinter import filedialog

import numpy
from tensorflow.keras.models import load_model

from modelo.imagem_rgb import ImagemRGB
from modelo.resnet50 import Resnet50
from modelo.svm import Svm


class TipoClassificacao(enum.Enum):
    """
    Enumeração dos tipos de classificação.
    """
    BINARIO = 1
    MULTICLASSE = 2


class ControladorClassificador:
    """
    Controlador responsável pelo modelo.
    """

    def __init__(self, imagem: ImagemRGB):
        """
        Constrói uma nova instância de ControladorModelo
        :param parent_controller: Controlador pai.
        """

        # Tipos de arquivos de modelos
        self.tipos_arquivos_modelos = [
            ("Todos os formatos compatíveis", [".h5", ".hdf5"]),
            ("Hierarchical Data Format", [".h5", ".hdf5"]),
            ("Todos os formatos", "*")
        ]

        # Imagem a ser classificada
        self.imagem = imagem

        # Tipo de classificacao
        self.__tipo_classificacao = None

        # Modelo a ser utilizado
        self.modelo = None

    @property
    def tipo_classificacao(self):
        """
        Obtém o valor do tipo de classificação a ser realizada.
        :return: Tipo de classificação a ser realizada.
        """
        return self.__tipo_classificacao

    @tipo_classificacao.setter
    def tipo_classificacao(self, tipo_classificacao):
        """
        Altera o valor do tipo de classificação a ser realizada.
        :param tipo_classificacao: Tipo de classificação a ser realizada.
        :return:
        """
        self.__tipo_classificacao = tipo_classificacao

    def abrir_modelo(self):
        """
        Abre um modelo a partir de um arquivo.
        :return:
        """
        pass

    def classificar(self):
        """
        Realiza a classificação da imagem.
        :return:
        """
        imagem_preprocessada = self.modelo.pre_processar(self.imagem)
        resultado = self.modelo.predict(numpy.array([imagem_preprocessada]))
        print(resultado)


class ControladorSvm(ControladorClassificador):
    """
    Controlador responsável pelo modelo SVM.
    """

    def abrir_modelo(self):
        """
        Abre um modelo a partir de um arquivo.
        :return:
        """
        caminho = filedialog.askopenfilename(filetypes=self.tipos_arquivos_modelos)
        self.modelo = Svm(load_model(caminho))


class ControladorResnet(ControladorClassificador):
    """
    Controlador responsável pelo modelo Resnet.
    """

    def abrir_modelo(self):
        """
        Abre um modelo a partir de um arquivo.
        :return:
        """
        caminho = filedialog.askopenfilename(filetypes=self.tipos_arquivos_modelos)
        self.modelo = Resnet50(load_model(caminho))

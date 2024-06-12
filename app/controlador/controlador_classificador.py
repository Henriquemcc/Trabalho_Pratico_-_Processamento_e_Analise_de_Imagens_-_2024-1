from tkinter import filedialog

from tensorflow.keras.models import load_model


class ControladorClassificador:
    """
    Controlador responsável pelo modelo.
    """

    def __init__(self):
        """
        Constrói uma nova instância de ControladorModelo
        """

        # Tipos de arquivos de modelos
        self.tipos_arquivos_modelos = [
            ("Todos os formatos compatíveis", [".h5", ".hdf5"]),
            ("Hierarchical Data Format", [".h5", ".hdf5"]),
            ("Todos os formatos", "*")
        ]

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
        caminho = filedialog.askopenfilename(filetypes=self.tipos_arquivos_modelos)
        self.modelo = load_model(caminho)

import tkinter

from controlador.controlador_classificador import ControladorClassificador
from modelo.classifier_types import ClassifierTypes


class FrameClassificador(tkinter.Frame):
    """
    Janela para executar o classificador na imagem atual.
    """

    def __init__(self, parent, controller):
        """
        Constrói uma nova instância do FrameClassificador.
        :param parent: Widget pai.
        :param controller: Controlador que instanciou esta classe.
        """

        # Controladores
        self.parent_controller = controller
        self.int_controller = ControladorClassificador()

        # Inicializando o pai
        tkinter.Frame.__init__(self, parent)

        # Título
        self.titulo = tkinter.Label(self, text="Classificador")
        self.titulo.pack(side="top", fill="x", pady=10)

        # Tipo de classificação: Binário ou multiclasse
        self.titulo_tipo_classificacao = tkinter.Label(self, text="Tipo de classificação")
        self.titulo_tipo_classificacao.pack(side="top", fill="x", pady=10)
        self.selected_radio_button_classificacao = tkinter.IntVar()
        self.radio_button_binario = tkinter.Radiobutton(
            self, text="Binário",
            variable=self.selected_radio_button_classificacao,
            value=1
        )
        self.radio_button_binario.pack(side="top", fill="x", pady=10)
        self.radio_button_multiclasse = tkinter.Radiobutton(
            self, text="Multiclasse",
            variable=self.selected_radio_button_classificacao,
            value=2
        )
        self.radio_button_multiclasse.pack(side="top", fill="x", pady=10)

        # Classificar SVM
        self.botao_classificar_svm = tkinter.Button(
            self,
            text="Classificar SVM",
            command=lambda: self.int_controller.classificar_svm(
                self.parent_controller.controlador.imagem_rgb,
                self.label_classificacao,
                classifier_type=ClassifierTypes(self.selected_radio_button_classificacao.get())
            )
        )
        self.botao_classificar_svm.pack(side="top", fill="x", pady=10)

        # Classificar ResNet
        self.botao_classificar_resnet = tkinter.Button(
            self,
            text="Classificar ResNet50",
            command=lambda: self.int_controller.classificar_resnet(
                self.parent_controller.controlador.imagem_rgb,
                self.label_classificacao,
                classifier_type=ClassifierTypes(self.selected_radio_button_classificacao.get())
            )
        )
        self.botao_classificar_resnet.pack(side="top", fill="x", pady=10)

        # Classificacao
        self.label_classificacao = tkinter.Label(self, text="Classificação: ")
        self.label_classificacao.pack(side="top", fill="x", pady=10)

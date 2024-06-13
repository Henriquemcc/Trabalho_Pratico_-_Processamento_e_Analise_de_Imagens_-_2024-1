import tkinter

from controlador.controlador_classificador import ControladorClassificador


class JanelaClassificador(tkinter.Tk):
    """
    Janela para executar o classificador na imagem atual.
    """

    def __init__(self, controlador, titulo, *args, **kwargs):
        """
        Constrói uma nova instância da JanelaSvm.
        :param nome_classificador: Nome do classificador.
        :param tipo_classificador: Tipo do classificador.
        :param Controlador: Controlador que criou esta classe.
        """

        # Inicializando o pai
        tkinter.Tk.__init__(self, *args, **kwargs)

        # Controlador do classificador
        self.controlador = controlador

        # Definindo o título
        self.title("Classificação")

        # Configurando o tamanho da janela
        screen_width = 500
        screen_height = 300
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        # Título
        titulo = tkinter.Label(self, text="Classificação")
        titulo.pack(side="top", fill="x", pady=10)

        # Abrir modelo
        botao_carregar_modelo = tkinter.Button(
            self,
            text="Carregar modelo",
            command=lambda: self.controlador.abrir_modelo()
        )
        botao_carregar_modelo.pack(side="top", fill="x", pady=10)

        # Tipo de classificação: Binário ou multiclasse
        titulo_tipo_classificacao = tkinter.Label(self, text="Tipo de classificação")
        titulo_tipo_classificacao.pack(side="top", fill="x", pady=10)
        self.selected_radio_button_classificacao = tkinter.IntVar()
        radio_button_binario = tkinter.Radiobutton(
            self, text="Binário",
            variable=self.selected_radio_button_classificacao,
            value=1
        )
        radio_button_binario.pack(side="top", fill="x", pady=10)
        radio_button_multiclasse = tkinter.Radiobutton(
            self, text="Multiclasse",
            variable=self.selected_radio_button_classificacao,
            value=2
        )
        radio_button_multiclasse.pack(side="top", fill="x", pady=10)

        # Classificar
        botao_classificar = tkinter.Button(
            self,
            text="Classificar",
            command=lambda: self.controlador.classificar()
        )
        botao_classificar.pack(side="top", fill="x", pady=10)

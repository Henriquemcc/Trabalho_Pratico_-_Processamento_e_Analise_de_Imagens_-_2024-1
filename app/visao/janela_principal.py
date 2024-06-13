import tkinter

from controlador.controlador import Controlador
from .frame_classificador import FrameClassificador
from .frame_principal import FramePrincipal
from .frame_imagem import FrameImagem
from .janela_zoom import JanelaZoom


class JanelaPrincipal(tkinter.Tk):
    """
    Janela principal
    """

    def __init__(self, *args, **kwargs):
        """
        Constrói uma nova instância da JanelaPrinpal.
        :param controlador: Controlador que está criando esta JanelaPrincipal.
        """
        tkinter.Tk.__init__(self, *args, **kwargs)
        # Controlador que instanciou a janela principal
        self.controlador = Controlador()

        # Definindo o título
        self.title("Trabalho Prático - Processamento e Análise de Imagens - 2024-1")

        # Configurando o tamanho da janela
        screen_width = 500
        screen_height = 300
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        # Barra de menu
        barra_menu = tkinter.Menu(self)

        # Menu arquivo
        menu_arquivo = tkinter.Menu(barra_menu, tearoff=0)
        menu_arquivo.add_command(
            label="Abrir imagem",
            command=lambda: self.controlador.abrir_arquivo_imagem(self.adicionar_imagem)
        )

        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

        # Menu visualizar
        menu_visualizar = tkinter.Menu(barra_menu, tearoff=0)
        menu_visualizar.add_command(
            label="Aumentar Zoom (Simples)",
            command=lambda: self.controlador.set_zoom(
                [[self.controlador.zoom[0][0]+10, self.controlador.zoom[0][1]-10],
                [self.controlador.zoom[1][0]+10, self.controlador.zoom[1][1]-10]],
                self.adicionar_imagem
            )
        )
        menu_visualizar.add_command(
            label="Aumentar Zoom (Avançado)",
            command=lambda: JanelaZoom(self.controlador, self.adicionar_imagem)
        )
        menu_visualizar.add_command(
            label="Remover Zoom",
            command=lambda: self.controlador.set_zoom(self.controlador.max_zoom, self.adicionar_imagem)
        )
        barra_menu.add_cascade(label="Visualizar", menu=menu_visualizar)

        # Menu converter
        menu_converter = tkinter.Menu(barra_menu, tearoff=0)
        menu_converter.add_command(
            label="RGB",
            command=lambda: self.controlador.exibir_imagem_rgb(self.adicionar_imagem)
        )
        menu_converter.add_command(
            label="Tons de cinza",
            command=lambda: self.controlador.exibir_imagem_tons_cinza(self.adicionar_imagem)
        )
        menu_converter.add_command(
            label="HSV",
            command=lambda: self.controlador.exibir_imagem_hsv(self.adicionar_imagem)
        )
        barra_menu.add_cascade(label="Conveter", menu=menu_converter)

        # Menu histogramas
        menu_histograma = tkinter.Menu(barra_menu, tearoff=0)

        submenu_hsv = tkinter.Menu(menu_histograma, tearoff=0)
        submenu_hsv.add_command(
            label="Hue",
            command=lambda: self.controlador.exibir_histograma_hsv_hue(
                self.adicionar_imagem,
                waiting=lambda: self.set_cursor("watch"),
                ending=lambda: self.set_cursor("")
            )
        )
        submenu_hsv.add_command(
            label="Saturation",
            command=lambda: self.controlador.exibir_histograma_hsv_saturation(
                self.adicionar_imagem,
                waiting=lambda: self.set_cursor("watch"),
                ending=lambda: self.set_cursor("")
            )
        )
        submenu_hsv.add_command(
            label="Value",
            command=lambda: self.controlador.exibir_histograma_hsv_value(
                self.adicionar_imagem,
                waiting=lambda: self.set_cursor("watch"),
                ending=lambda: self.set_cursor("")
            )
        )

        menu_histograma.add_command(
            label="Tons de cinza",
            command=lambda: self.controlador.exibir_histograma_tons_cinza(
                self.adicionar_imagem,
                waiting=lambda: self.set_cursor("watch"),
                ending=lambda: self.set_cursor("")
            )
        )
        menu_histograma.add_cascade(label="HSV", menu=submenu_hsv)
        menu_histograma.add_command(
            label="HSV_2D",
            command=lambda: self.controlador.exibir_histograma_hsv_2d(
                self.adicionar_imagem,
                waiting=lambda: self.set_cursor("watch"),
                ending=lambda: self.set_cursor("")
            )
        )
        barra_menu.add_cascade(label="Histogramas", menu=menu_histograma)

        # Menu caracterizar imagem
        menu_caracterizar_imagem = tkinter.Menu(barra_menu, tearoff=0)
        menu_caracterizar_imagem.add_command(label="Descritores de Haralick")
        menu_caracterizar_imagem.add_command(label="Momentos invariantes de Hu")
        barra_menu.add_cascade(label="Caracterizar", menu=menu_caracterizar_imagem)

        # Menu classificar
        barra_menu.add_command(label="Classificar", command=lambda: self.show_frame("FrameClassificador"))

        self.config(menu=barra_menu)

        # Configurando mudança de página
        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Controle de paginas
        self.frames = {}
        for F in (FramePrincipal, FrameImagem, FrameClassificador):
            page_name = F.__name__
            frame = F(container, controller=self)
            self.frames[page_name] = frame

            # Stack the pages on top of each other so theycan be switched
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FramePrincipal")

    def show_frame(self, page_name):
        """Shows the frame correspondent to the page_name"""
        frame = self.frames[page_name]
        frame.tkraise()

    def set_cursor(self, state):
        """
        Altera o cursor do mouse
        :param state: Novo estado do cursor do mouse.
        :return:
        """
        self.config(cursor=state)
        self.update()

    def adicionar_imagem(self, image):
        """
        Adiciona uma imagem na janela.
        :param image: Imagem a ser inserida.
        """
        self.frames["FrameImagem"].image = image
        self.show_frame("FrameImagem")

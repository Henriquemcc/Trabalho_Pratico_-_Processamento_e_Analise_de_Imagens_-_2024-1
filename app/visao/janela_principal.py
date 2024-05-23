import tkinter

import PIL.ImageTk
import PIL.Image

from controlador.controlador import Controlador


class FramePrincipal(tkinter.Frame):
    """
    Frame Principal.
    """

    def __init__(self, parent, controller):
        """
        Constrói uma nova instância do FramePrincipal.
        :param parent: Widget pai.
        :param controller: Controlador que instanciou esta classe.
        """
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        titulo = tkinter.Label(self, text="Trabalho Prático - Processamento e Análise de Imagens - 2024-1")
        titulo.pack(side="top", fill="x", pady=10)
        autor1 = tkinter.Label(self, text="Felipe Costa Amaral")
        autor1.pack(side="top", fill="x", pady=10)
        autor2 = tkinter.Label(self, text="Henrique Mendonça Castelar Campos")
        autor2.pack(side="top", fill="x", pady=10)
        autor3 = tkinter.Label(self, text="Larissa Kaweski Siqueira")
        autor3.pack(side="top", fill="x", pady=10)


class FrameImagem(tkinter.Frame):
    """
    Frame utilizado na exibição de imagens.
    """

    def __init__(self, parent, controller):
        """
        Constrói uma nova instância do FrameImagem.
        :param parent: Widget pai.
        :param controller: Controlador que instanciou esta classe.
        """
        tkinter.Frame.__init__(self, parent)
        self.on_resize = None
        self.controller = controller
        self.label = tkinter.Label(self)
        self.label.pack(fill="both", expand=True)

    def set_imagem(self, image: PIL.Image.Image, legenda=None):
        """
        Atualiza a imagem do Frame Tkinter.
        :param image: Nova imagem a ser adicionada.
        :param legenda: Nova legenda a ser adicionada.
        :return:
        """
        label_width = self.label.winfo_width()
        label_height = self.label.winfo_height()
        if label_width > 1 and label_height > 1:
            image = image.resize((label_width, label_height))
        photo_image = PIL.ImageTk.PhotoImage(image)
        self.label.config(image=photo_image, text=legenda)
        self.label.image = photo_image



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

        # Widget principal
        self.title("Trabalho Prático - Processamento e Análise de Imagens - 2024-1")

        # Maximizando a janela
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

        # Menu editar
        menu_editar = tkinter.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Editar", menu=menu_editar)

        # Menu visualizar
        menu_visualizar = tkinter.Menu(barra_menu, tearoff=0)
        menu_visualizar.add_command(label="Exibir cores")
        menu_visualizar.add_command(label="Exibir tons de cinza")
        menu_visualizar.add_command(label="Aumentar Zoom")
        menu_visualizar.add_command(label="Diminuir Zoom")
        barra_menu.add_cascade(label="Visualizar", menu=menu_visualizar)

        # Menu converter
        menu_converter = tkinter.Menu(barra_menu, tearoff=0)
        menu_converter.add_command(
            label="Tons de cinza",
            command=lambda: self.controlador.converter_imagem_rgb_para_imagem_tons_cinza()
        )
        barra_menu.add_cascade(label="Conveter", menu=menu_converter)

        # Menu gerar
        menu_gerar = tkinter.Menu(barra_menu, tearoff=0)
        submenu_histograma = tkinter.Menu(menu_gerar, tearoff=0)
        submenu_histograma.add_command(label="Tons de cinza")
        submenu_histograma.add_command(label="Cor")
        menu_gerar.add_cascade(label="Histograma", menu=submenu_histograma)
        barra_menu.add_cascade(label="Gerar", menu=menu_gerar)

        # Menu caracterizar imagem
        menu_caracterizar_imagem = tkinter.Menu(barra_menu, tearoff=0)
        menu_caracterizar_imagem.add_command(label="Descritores de Haralick")
        menu_caracterizar_imagem.add_command(label="Momentos invariantes de Hu")
        barra_menu.add_cascade(label="Caracterizar", menu=menu_caracterizar_imagem)

        # Menu classificar
        menu_classificar = tkinter.Menu(barra_menu, tearoff=0)
        menu_classificar.add_command(label="SVM")
        menu_classificar.add_command(label="ResNet50")
        barra_menu.add_cascade(label="Classificar", menu=menu_classificar)

        self.config(menu=barra_menu)

        # Configurando mudança de página
        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Controle de paginas
        self.frames = {}
        for F in (FramePrincipal, FrameImagem):
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

    def adicionar_imagem(self, image: PIL.Image.Image):
        """
        Adiciona uma imagem na janela.
        :param image: Imagem a ser inserida.
        :type caminho: ImageTk.
        """
        self.frames["FrameImagem"].set_imagem(image)
        self.show_frame("FrameImagem")

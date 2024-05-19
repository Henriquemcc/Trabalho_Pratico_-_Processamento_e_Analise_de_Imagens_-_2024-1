import tkinter as tk

from controlador.Controlador import Controlador
from visao.Home import Home


class JanelaPrincipal(tk.Tk):
    """
    Janela principal
    """

    def __init__(self, *args, **kwargs):
        """
        Constrói uma nova instância da JanelaPrinpal.
        :param controlador: Controlador que está criando esta JanelaPrincipal.
        """
        tk.Tk.__init__(self, *args, **kwargs)
        # Controlador que instanciou a janela principal
        self.controlador = Controlador()

        # Widget principal
        self.title("Trabalho Prático - Processamento e Análise de Imagens - 2024-1")

        # Maximizando a janela
        screen_width = 400  #self.winfo_screenwidth()
        screen_height = 300  #self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        # Barra de menu
        barra_menu = tk.Menu(self)

        # Menu arquivo
        menu_arquivo = tk.Menu(barra_menu, tearoff=0)
        menu_arquivo.add_command(
            label="Abrir imagem",
            command=lambda: self.controlador.abrir_arquivo_imagem(self.adicionar_imagem)
        )

        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

        # Menu editar
        menu_editar = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Editar", menu=menu_editar)

        # Menu visualizar
        menu_visualizar = tk.Menu(barra_menu, tearoff=0)
        menu_visualizar.add_command(label="Exibir cores")
        menu_visualizar.add_command(label="Exibir tons de cinza")
        menu_visualizar.add_command(label="Aumentar Zoom")
        menu_visualizar.add_command(label="Diminuir Zoom")
        barra_menu.add_cascade(label="Visualizar", menu=menu_visualizar)

        # Menu converter
        menu_converter = tk.Menu(barra_menu, tearoff=0)
        menu_converter.add_command(label="Tons de cinza")
        barra_menu.add_cascade(label="Conveter", menu=menu_converter)

        # Menu gerar
        menu_gerar = tk.Menu(barra_menu, tearoff=0)
        submenu_histograma = tk.Menu(menu_gerar, tearoff=0)
        submenu_histograma.add_command(label="Tons de cinza")
        submenu_histograma.add_command(label="Cor")
        menu_gerar.add_cascade(label="Histograma", menu=submenu_histograma)
        barra_menu.add_cascade(label="Gerar", menu=menu_gerar)

        # Menu caracterizar imagem
        menu_caracterizar_imagem = tk.Menu(barra_menu, tearoff=0)
        menu_caracterizar_imagem.add_command(label="Descritores de Haralick")
        menu_caracterizar_imagem.add_command(label="Momentos invariantes de Hu")
        barra_menu.add_cascade(label="Caracterizar", menu=menu_caracterizar_imagem)

        # Menu classificar
        menu_classificar = tk.Menu(barra_menu, tearoff=0)
        menu_classificar.add_command(label="SVM")
        menu_classificar.add_command(label="ResNet50")
        barra_menu.add_cascade(label="Classificar", menu=menu_classificar)

        self.config(menu=barra_menu)

        # Configurando mudança de página
        container = tk.Frame(self)
        container.pack(side="top", fill="x", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Controle de paginas
        self.frames = {}
        for F in (Home,):
            page_name = F.__name__
            frame = F(container, controller=self)
            self.frames[page_name] = frame

            # Stack the pages on top of each other so theycan be switched
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        """Shows the frame correspondent to the page_name"""
        frame = self.frames[page_name]
        frame.tkraise()

    def adicionar_imagem(self, foto):
        """
        Adiciona uma imagem na janela.
        :param foto: Imagem a ser inserida.
        :type caminho: ImageTk.
        """
        legenda = tk.Label(self, image=foto)
        legenda.image = foto
        legenda.pack()

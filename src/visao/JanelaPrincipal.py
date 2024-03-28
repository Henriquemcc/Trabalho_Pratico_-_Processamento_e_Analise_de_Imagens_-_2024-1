import tkinter

from controlador import Controlador


class JanelaPrincipal:
    """
    Janela principal
    """
    def __init__(self, controlador: Controlador):
        """
        Constrói uma nova instância da JanelaPrinpal.
        :param controlador: Controlador que está criando esta JanelaPrincipal.
        """

        # Controlador que instanciou a janela principal
        self.controlador = controlador

        # Widget principal
        self.root = tkinter.Tk()
        self.root.title("Trabalho Prático - Processamento e Análise de Imagens - 2024-1")

        # Barra de menu
        barra_menu = tkinter.Menu(self.root)
        self.adicionar_menu_arquivo(barra_menu)
        self.adicionar_menu_editar(barra_menu)
        self.adicionar_menu_visualizar(barra_menu)
        self.adicionar_menu_converter(barra_menu)
        self.adicionar_menu_gerar(barra_menu)
        self.adicionar_menu_caracterizar(barra_menu)
        self.adicionar_menu_classificar(barra_menu)

        # Adicionando barra de menus
        self.root.config(menu=barra_menu)

        # Maximizando a janela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Exibindo a janela principal
        self.root.mainloop()

    def adicionar_menu_caracterizar(self, barra_menu: tkinter.Menu) -> None:
        """
        Adiciona o menu caracterizar á barra de menu.
        :param barra_menu: Barra de menu a qual será adicionada o menu caracterizar.
        :return:
        """

        # Menu caracterizar imagem
        menu_caracterizar_imagem = tkinter.Menu(barra_menu, tearoff=0)
        # Item descritores de Haralick
        menu_caracterizar_imagem.add_command(label="Descritores de Haralick")
        # Item momentos invariantes de Hu
        menu_caracterizar_imagem.add_command(label="Momentos invariantes de Hu")
        # Adicionando menu caracterizar
        barra_menu.add_cascade(label="Caracterizar", menu=menu_caracterizar_imagem)

    def adicionar_menu_gerar(self, barra_menu: tkinter.Menu) -> None:
        """
        Adiciona o menu gerar á barra de menu.
        :param barra_menu: Barra de menu a qual será adicionada o menu gerar.
        :return:
        """

        # Menu gerar
        menu_gerar = tkinter.Menu(barra_menu, tearoff=0)
        # Submenu histograma
        submenu_histograma = tkinter.Menu(menu_gerar, tearoff=0)
        # Subitem tons de cinza
        submenu_histograma.add_command(label="Tons de cinza")
        # Subitem cor
        submenu_histograma.add_command(label="Cor")
        # Item histograma
        menu_gerar.add_cascade(label="Histograma", menu=submenu_histograma)
        # Adicionando menu gerar
        barra_menu.add_cascade(label="Gerar", menu=menu_gerar)

    def adicionar_menu_converter(self, barra_menu: tkinter.Menu) -> None:
        """
        Adiciona o menu converter á barra de menu.
        :param barra_menu: Barra de menu a qual será adicionada o menu converter.
        :return:
        """

        # Menu converter
        menu_converter = tkinter.Menu(barra_menu, tearoff=0)
        # Item tons de cinza
        menu_converter.add_command(label="Tons de cinza")
        # Adicionando menu converter
        barra_menu.add_cascade(label="Conveter", menu=menu_converter)

    def adicionar_menu_editar(self, barra_menu: tkinter.Menu) -> None:
        """
        Adiciona o menu editar á barra de menu.
        :param barra_menu: Barra de menu a qual será adicionada o menu editar.
        :return:
        """

        # Menu editar
        menu_editar = tkinter.Menu(barra_menu, tearoff=0)
        # Adicionando menu editar
        barra_menu.add_cascade(label="Editar", menu=menu_editar)

    def adicionar_menu_arquivo(self, barra_menu: tkinter.Menu) -> None:
        """
        Adiciona o menu arquivo á barra de menu.
        :param barra_menu: Barra de menu a qual será adicionada o menu arquivo.
        :return:
        """

        # Menu arquivo
        menu_arquivo = tkinter.Menu(barra_menu, tearoff=0)
        # Item abrir imagem
        menu_arquivo.add_command(label="Abrir imagem", command=self.controlador.abrir_arquivo_imagem)
        # Adicionando menu arquivo
        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

    def adicionar_menu_classificar(self, barra_menu: tkinter.Menu) -> None:
        """
        Adiciona o menu classificar á barra de menu.
        :param barra_menu: Barra de menu a qual será adicionada o menu classificar.
        :return:
        """

        # Menu classificar
        menu_classificar = tkinter.Menu(barra_menu, tearoff=0)
        # Item SVM
        menu_classificar.add_command(label="SVM")
        # Item ResNet50
        menu_classificar.add_command(label="ResNet50")
        # Adicionando menu classificar
        barra_menu.add_cascade(label="Classificar", menu=menu_classificar)

    def adicionar_menu_visualizar(self, barra_menu: tkinter.Menu) -> None:
        """
        Adiciona o menu visualizar á barra de menu.
        :param barra_menu: Barra de menu a qual será adicionada o menu visualizar.
        :return:
        """

        # Menu visualizar
        menu_visualizar = tkinter.Menu(barra_menu, tearoff=0)
        # Item exibir cores
        menu_visualizar.add_command(label="Exibir cores")
        # Item exibir tons de cinza
        menu_visualizar.add_command(label="Exibir tons de cinza")
        # Item Aumentar o Zoom
        menu_visualizar.add_command(label="Aumentar Zoom")
        # Item Diminuir o Zoom
        menu_visualizar.add_command(label="Diminuir Zoom")
        # Adicionando menu visualizar
        barra_menu.add_cascade(label="Visualizar", menu=menu_visualizar)

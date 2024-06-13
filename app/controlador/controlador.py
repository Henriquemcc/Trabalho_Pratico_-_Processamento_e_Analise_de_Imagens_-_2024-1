from io import BytesIO
from tkinter import filedialog

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from modelo.imagem_hsv import ImagemHSV
from modelo.imagem_rgb import ImagemRGB
from modelo.imagem_tons_cinza import ImagemTonsCinza


class Controlador:
    """
    Controlador.
    """

    def __init__(self):

        # Tipos de arquivos de imagem
        self.tipos_arquivos_imagem = [
            ("Todos os formatos compatíveis", [".png", ".jpeg", ".jpg"]),
            ("Portable Network Graphics", ".png"),
            ("Joint Photographic Experts Group", ".jpeg"),
            ("Joint Photographic Experts Group", ".jpg"),
            ("Todos os formatos", "*")
        ]


        self.caminho = None
        self.imagem_rgb = None

        self.imagem_tons_cinza = None
        self.update_tons_cinza = False

        self.imagem_hsv = None
        self.update_hsv = False

        self.histograma_cinza = None
        self.update_histograma_cinza = False

        self.histograma_hsv = None
        self.update_histograma_hsv = False

        self.histograma_hsv_2d = None
        self.update_histograma_hsv_2d = False

        self.last_shown = None
        self.zoom = None
        self.max_zoom = None

    def set_zoom(self, zoom, f):
        if (
                zoom[0][0] < self.max_zoom[0][0] or
                zoom[0][1] > self.max_zoom[0][1] or
                zoom[1][0] < self.max_zoom[1][0] or
                zoom[1][1] > self.max_zoom[1][1] or
                zoom[0][0] >= zoom[0][1] or
                zoom[1][0] >= zoom[1][1]
        ):
            raise Exception("Zoom out of bounds of image")

        self.zoom = zoom

        if self.last_shown == 'rgb':
            f(self.imagem_rgb.to_image(zoom=self.zoom))
        elif self.last_shown == 'cinza':
            f(self.imagem_tons_cinza.to_image(zoom=self.zoom))
        elif self.last_shown == 'hsv':
            f(self.imagem_hsv.to_image(zoom=self.zoom))

    def abrir_arquivo_imagem(self, f) -> None:
        """
        Realiza a abertura de um arquivo de imagem.
        :return:
        """
        self.caminho = filedialog.askopenfilename(filetypes=self.tipos_arquivos_imagem)
        self.imagem_rgb = ImagemRGB.from_file(self.caminho)
        self.last_shown = 'rgb'
        self.zoom = self.max_zoom = [[0, self.imagem_rgb.matriz.shape[0]], [0, self.imagem_rgb.matriz.shape[1]]]
        self.update_tons_cinza = self.update_hsv = True
        self.update_histograma_cinza = self.update_histograma_hsv = self.update_histograma_hsv_2d = True
        f(self.imagem_rgb.to_image(zoom=self.zoom))

    def __gerar_imagem_cinza(self):
        """
        Gera uma imagem em tons de cinza.
        :return:
        """
        if self.update_tons_cinza:
            self.imagem_tons_cinza = ImagemTonsCinza.from_image(self.imagem_rgb)
            self.update_tons_cinza = False

    def __gerar_imagem_hsv(self):
        """
        Gera uma imagem HSV.
        :return:
        """
        if self.update_hsv:
            self.imagem_hsv = ImagemHSV.from_image(self.imagem_rgb)
            self.update_hsv = False

    def exibir_imagem_rgb(self, f):
        """
        Exibe uma imagem RGB.
        :param f: Função passada pela janela principal a ser executada por esta função com a imagem a ser exibida.
        :return:
        """
        self.last_shown = 'rgb'
        f(self.imagem_rgb.to_image(zoom=self.zoom))

    def exibir_imagem_tons_cinza(self, f) -> None:
        """
        Exibe uma imagem RGB em uma imagem em tons de cinza.
        :param f: Função passada pela janela principal a ser executada por esta função com a imagem a ser exibida.
        :return:
        """
        self.last_shown = 'cinza'
        self.__gerar_imagem_cinza()
        f(self.imagem_tons_cinza.to_image(zoom=self.zoom))

    def exibir_imagem_hsv(self, f) -> None:
        """
        Exibe uma imagem RGB em uma imagem em tons de cinza.
        :param f: Função passada pela janela principal a ser executada por esta função com a imagem a ser exibida.
        :return:
        """
        self.last_shown = 'hsv'
        self.__gerar_imagem_hsv()
        f(self.imagem_hsv.to_image(zoom=self.zoom))

    def __gerar_histograma_cinza(self, waiting=lambda: None, ending=lambda: None):
        """
        Gera o histograma de tons de cinza.
        :param waiting: Função lambda para setar o ponteiro carregando do mouse.
        :param ending: Função lambda para setar o ponteiro padrão do mouse.
        :return:
        """
        if self.update_histograma_cinza:
            waiting()
            self.histograma_cinza = self.imagem_tons_cinza.to_histograma()
            ending()
            self.update_histograma_cinza = False

    def __gerar_histograma_hsv(self, waiting=lambda: None, ending=lambda: None):
        """
        Gera o histograma HSV.
        :param waiting: Função lambda para setar o ponteiro carregando do mouse.
        :param ending: Função lambda para setar o ponteiro padrão do mouse.
        :return:
        """
        if self.update_histograma_hsv:
            waiting()
            self.histograma_hsv = self.imagem_hsv.to_histograma()
            ending()
            self.update_histograma_hsv = False

    def __gerar_histograma_hsv_2d(self, waiting=lambda: None, ending=lambda: None):
        """
        Gera o histograma 2D.
        :param waiting: Função lambda para setar o ponteiro carregando do mouse.
        :param ending: Função lambda para setar o ponteiro padrão do mouse.
        :return:
        """
        if self.update_histograma_hsv_2d:
            waiting()
            self.histograma_hsv_2d = self.imagem_hsv.to_histograma_2d()
            ending()
            self.update_histograma_hsv_2d = False

    def exibir_histograma_tons_cinza(self, f, waiting=lambda: None, ending=lambda: None) -> None:
        """
        Exibe o histograma de tons de cinza.
        :param f: Função a ser executada com o valor da variável plot (que contém o histograma de tons de cinza).
        :param waiting: Função lambda para setar o ponteiro carregando do mouse.
        :param ending: Função lambda para setar o ponteiro padrão do mouse.
        :return:
        """
        self.__gerar_imagem_cinza()
        self.__gerar_histograma_cinza(waiting=waiting, ending=ending)
        plot = self.__extract_2d_bar(self.histograma_cinza)
        f(plot)

    def exibir_histograma_hsv_hue(self, f, waiting=lambda: None, ending=lambda: None) -> None:
        """
        Exibe o histograma HUE do HSV.
        :param f: Função a ser executada com o valor da variável plot (que contém o histograma HUE HSV).
        :param waiting: Função lambda para setar o ponteiro carregando do mouse.
        :param ending: Função lambda para setar o ponteiro padrão do mouse.
        :return:
        """
        self.__gerar_imagem_hsv()
        self.__gerar_histograma_hsv(waiting=waiting, ending=ending)
        plot = self.__extract_2d_bar(self.histograma_hsv[0])
        f(plot)

    def exibir_histograma_hsv_saturation(self, f, waiting=lambda: None, ending=lambda: None) -> None:
        """
        Exibe o histograma Saturation do HSV.
        :param f: Função a ser executada com o valor da variável plot (que contém o histograma Saturation HSV).
        :param waiting: Função lambda para setar o ponteiro carregando do mouse.
        :param ending: Função lambda para setar o ponteiro padrão do mouse.
        :return:
        """
        self.__gerar_imagem_hsv()
        self.__gerar_histograma_hsv(waiting=waiting, ending=ending)
        plot = self.__extract_2d_bar(self.histograma_hsv[1])
        f(plot)

    def exibir_histograma_hsv_value(self, f, waiting=lambda: None, ending=lambda: None) -> None:
        """
        Exibe o histograma Value do HSV.
        :param f: Função a ser executada com o valor da variável plot (que contém o histograma Value HSV).
        :param waiting: Função lambda para setar o ponteiro carregando do mouse.
        :param ending: Função lambda para setar o ponteiro padrão do mouse.
        :return:
        """
        self.__gerar_imagem_hsv()
        self.__gerar_histograma_hsv(waiting=waiting, ending=ending)
        plot = self.__extract_2d_bar(self.histograma_hsv[2])
        f(plot)

    def exibir_histograma_hsv_2d(self, f, waiting=lambda: None, ending=lambda: None) -> None:
        """
        Exibe o histograma 2D Hue por Value do HSV.
        :param f: Função a ser executada com o valor da variável plot (que contém o histograma 2D Hue por Value HSV).
        :param waiting: Função lambda para setar o ponteiro carregando do mouse.
        :param ending: Função lambda para setar o ponteiro padrão do mouse.
        :return:
        """
        self.__gerar_imagem_hsv()
        self.__gerar_histograma_hsv_2d(waiting=waiting, ending=ending)
        plot = self.__extract_3d_bar(self.histograma_hsv_2d)
        f(plot)

    @staticmethod
    def __extract_2d_bar(dict_histogram, n_bin=16):
        """
        Extraí um gráfico 2D de barras a partir de um dicionário de histograma.
        :param dict_histogram: Dicionário de histograma.
        :param n_bin:
        :return: Imagem com o gráfico 2D.
        """
        dado = list(dict_histogram.items())
        dado.sort(key=lambda x: x[0])
        x, y = zip(*dado)
        fig, ax = plt.subplots()
        ax.bar(x, y, width=(256 // n_bin) - 1)
        imagem = Controlador.__buffer_plot_and_get(fig)
        plt.close(fig)
        return imagem

    @staticmethod
    def __extract_3d_bar(dict_histogram, n_bin=(16, 128)):
        """
        Extraí um gráfico 3D de barras a partir de um dicionário de histograma.
        :param dict_histogram: Dicionário de histograma.
        :param n_bin:
        :return: Imagem com o gráfico 3D.
        """
        dados = list(dict_histogram.items())  # p2

        dados.sort(key=lambda x: x[0][1])
        dados.sort(key=lambda x: x[0][0])

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        _x = [x[0][0] for x in dados[::n_bin[1]]]
        _y = [y[0][1] for y in dados[:n_bin[1]]]
        _xx, _yy = np.meshgrid(_x, _y)
        x, y = _xx.ravel(), _yy.ravel()

        top = [z[1] for z in dados]
        bottom = np.zeros_like(top)
        width = (256 // n_bin[0]) - 1
        depth = (256 // n_bin[1]) - 1

        ax.bar3d(x, y, bottom, width, depth, top, shade=True)
        imagem = Controlador.__buffer_plot_and_get(fig)
        plt.close(fig)
        return imagem

    @staticmethod
    def __buffer_plot_and_get(fig):
        """
        Obtém uma imagem a partir da figura a ser plotada
        :param fig: Figura a ser plotada.
        :return: Imagem obtida a partir da figura.
        """
        buf = BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        return Image.open(buf)

    def exibir_janela_classificador(self):
        pass

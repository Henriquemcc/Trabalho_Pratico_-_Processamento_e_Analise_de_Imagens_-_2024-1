from tkinter import filedialog

from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

from modelo.imagem_rgb import ImagemRGB
from modelo.imagem_tons_cinza import ImagemTonsCinza
from modelo.imagem_hsv import ImagemHSV

class Controlador:
    """
    Controlador.
    """

    def __init__(self):
        self.tipos_arquivos = [
            ("Todos os formatos compatíveis", [".png", ".jpeg", ".jpg"]),
            ("Portable Network Graphics", ".png"),
            ("Joint Photographic Experts Group", ".jpeg"),
            ("Joint Photographic Experts Group", ".jpg"),
            ("Todos os formatos", "*")
        ]

        self.caminho = None
        self.imagem_rgb = None

        self.update_tons_cinza = False
        self.imagem_tons_cinza = None

        self.update_histograma_cinza = False
        self.histograma_cinza = None

        self.update_hsv = False
        self.imagem_hsv = None

        self.update_histograma_hsv = False
        self.histograma_hsv = None
        self.update_histograma_hsv_2d = False
        self.histograma_hsv_2d = None

        self.photo_image = None

    def abrir_arquivo_imagem(self, f) -> None:
        """
        Realiza a abertura de um arquivo de imagem.
        :return:
        """
        self.caminho = filedialog.askopenfilename(filetypes=self.tipos_arquivos)
        self.imagem_rgb = ImagemRGB.from_file(self.caminho)
        self.update_tons_cinza=self.update_hsv=True
        self.update_histograma_cinza=self.update_histograma_hsv=self.update_histograma_hsv_2d=True
        f(self.imagem_rgb.to_image())

    def __gerar_imagem_cinza(self):
        if(self.update_tons_cinza):
            self.imagem_tons_cinza = ImagemTonsCinza.from_image(self.imagem_rgb)
            self.update_tons_cinza=False

    def __gerar_imagem_hsv(self):
        if(self.update_hsv):
            self.imagem_hsv = ImagemHSV.from_image(self.imagem_rgb)
            self.update_hsv=False

    def exibir_imagem_rgb(self,f):
        f(self.imagem_rgb.to_image())

    def exibir_imagem_tons_cinza(self, f) -> None:
        """
        Converte uma imagem RGB em uma imagem em tons de cinza.
        :return:
        """
        self.__gerar_imagem_cinza()
        f(self.imagem_tons_cinza.to_image())

    def exibir_imagem_hsv(self, f) -> None:
        """
        Converte uma imagem RGB em uma imagem em tons de cinza.
        :return:
        """
        self.__gerar_imagem_hsv()
        f(self.imagem_hsv.to_image())

    def __gerar_histograma_cinza(self):
        if (self.update_histograma_cinza):
            self.histograma_cinza = self.imagem_tons_cinza.to_histograma()
            self.update_histograma_cinza = False

    def __gerar_histograma_hsv(self):
        if (self.update_histograma_hsv):
            self.histograma_hsv = self.imagem_hsv.to_histograma()
            self.update_histograma_hsv = False

    def exibir_histograma_tons_cinza(self, f) -> None:
        self.__gerar_imagem_cinza()
        self.__gerar_histograma_cinza()
        plot = self.__extract_2d_bar(self.histograma_cinza)
        f(plot)

    def exibir_histograma_hsv_hue(self, f) -> None:
        self.__gerar_imagem_hsv()
        self.__gerar_histograma_hsv()
        plot = self.__extract_2d_bar(self.histograma_hsv[0])
        f(plot)

    def exibir_histograma_hsv_saturation(self, f) -> None:
        self.__gerar_imagem_hsv()
        self.__gerar_histograma_hsv()
        plot = self.__extract_2d_bar(self.histograma_hsv[1])
        f(plot)

    def exibir_histograma_hsv_value(self, f) -> None:
        self.__gerar_imagem_hsv()
        self.__gerar_histograma_hsv()
        plot = self.__extract_2d_bar(self.histograma_hsv[2])
        f(plot)

    @staticmethod
    def __extract_2d_bar(dict_histogram):
        dado = list(dict_histogram.items())
        dado.sort(key=lambda x: x[0])
        x, y = zip(*dado)
        fig, ax = plt.subplots()
        ax.bar(x, y, width=15.0)
        return Controlador.__buffer_plot_and_get(fig)

    @staticmethod
    def __buffer_plot_and_get(fig):
        buf = BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        return Image.open(buf)

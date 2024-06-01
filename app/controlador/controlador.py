from tkinter import filedialog

import PIL.Image
import PIL.ImageTk

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

        self.update_hsv = False
        self.imagem_hsv = None

        self.photo_image = None

    def abrir_arquivo_imagem(self, f) -> None:
        """
        Realiza a abertura de um arquivo de imagem.
        :return:
        """
        self.caminho = filedialog.askopenfilename(filetypes=self.tipos_arquivos)
        self.imagem_rgb = ImagemRGB.from_file(self.caminho)
        self.update_tons_cinza=self.update_hsv=True
        f(self.imagem_rgb.to_image())

    def exibir_imagem_rgb(self,f):
        f(self.imagem_rgb.to_image())

    def exibir_imagem_tons_cinza(self, f) -> None:
        """
        Converte uma imagem RGB em uma imagem em tons de cinza.
        :return:
        """
        if(self.update_tons_cinza):
            self.imagem_tons_cinza = ImagemTonsCinza.from_image(self.imagem_rgb)
            self.update_tons_cinza=False
        f(self.imagem_tons_cinza.to_image())

    def exibir_imagem_hsv(self, f) -> None:
        """
        Converte uma imagem RGB em uma imagem em tons de cinza.
        :return:
        """
        if(self.update_hsv):
            self.imagem_hsv = ImagemHSV.from_image(self.imagem_rgb)
            self.update_hsv=False
        f(self.imagem_hsv.to_image())

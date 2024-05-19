from tkinter import filedialog

import PIL.Image
import PIL.ImageTk

from modelo.imagem_rgb import ImagemRGB
from modelo.imagem_tons_cinza import ImagemTonsCinza


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
        self.imagem_tons_cinza = None
        self.imagem = None
        self.foto = None

    def abrir_arquivo_imagem(self, f) -> None:
        """
        Realiza a abertura de um arquivo de imagem.
        :return:
        """
        self.caminho = filedialog.askopenfilename(filetypes=self.tipos_arquivos)
        print("caminho =", self.caminho, sep=" ")

        self.imagem = PIL.Image.open(self.caminho)
        self.imagem_rgb = ImagemRGB(caminho_arquivo=self.caminho)
        self.foto = PIL.ImageTk.PhotoImage(self.imagem)

        f(self.foto)

    def converter_imagem_rgb_para_imagem_tons_cinza(self) -> None:
        """
        Converte uma imagem RGB em uma imagem em tons de cinza.
        :return:
        """
        self.imagem_tons_cinza = ImagemTonsCinza(imagem_rgb=self.imagem_rgb)

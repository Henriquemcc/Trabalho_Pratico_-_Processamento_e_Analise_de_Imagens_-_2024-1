from tkinter import filedialog

import PIL.Image
import PIL.ImageTk


class Controlador:
    """
    Controlador.
    """

    def __init__(self):
        self.tipos_arquivos = [
            ("Portable Network Graphics", ".png"),
            ("Joint Photographic Experts Group", ".jpeg"),
            ("Joint Photographic Experts Group", ".jpg")
        ]

        self.caminho = None
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
        self.foto = PIL.ImageTk.PhotoImage(self.imagem)

        f(self.foto)

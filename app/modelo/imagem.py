import PIL
import PIL.Image


class Imagem:
    """
    Super classe de ImagemRGB e ImagemTonsCinza.
    """
    def __init__(self, matriz):
        """
        Constrói uma nova instância de ImagemRGB.
        :param matriz: Matriz RGB.
        """
        self.matriz = matriz

    def to_image(self) -> PIL.Image.Image:
        """
        Converte ImagemRGB em uma PIL.Image.Image
        :return: PIL.Image.Image gerada a partir de ImagemRGB.
        """
        return PIL.Image.fromarray(self.matriz)

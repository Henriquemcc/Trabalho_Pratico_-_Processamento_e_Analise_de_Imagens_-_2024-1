from PIL import Image


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

    def to_image(self) -> Image:
        """
        Converte ImagemRGB em uma Image
        :return: Image gerada a partir de ImagemRGB.
        """
        return Image.fromarray(self.matriz)

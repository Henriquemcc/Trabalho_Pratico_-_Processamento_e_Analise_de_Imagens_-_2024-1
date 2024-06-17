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

    def to_image(self, zoom=None) -> Image:
        """
        Converte ImagemRGB em uma Image
        :return: Image gerada a partir de ImagemRGB.
        """
        if zoom is not None:
            return Image.fromarray(self.matriz[zoom[0][0]:zoom[0][1], zoom[1][0]:zoom[1][1]])
        return Image.fromarray(self.matriz)

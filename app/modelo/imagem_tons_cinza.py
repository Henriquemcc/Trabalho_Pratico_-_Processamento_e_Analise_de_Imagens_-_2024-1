import PIL.Image


class ImagemTonsCinza:
    """
    Representa uma matriz de tons de cinza.
    """

    def __init__(self, matriz):
        """
        Constrói uma nova instância da classe ImagemTonsCinza.
        :param matriz: Matriz de tons de cinza.
        """
        self.matriz = matriz

    def to_image(self) -> PIL.Image.Image:
        """
        Converte ImagemTonsCinza em uma PIL.Image.Image
        :return: PIL.Image.Image gerada a partir de ImagemTonsCinza.
        """
        return PIL.Image.fromarray(self.matriz, mode='L')

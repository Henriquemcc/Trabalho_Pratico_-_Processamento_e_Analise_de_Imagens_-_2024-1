import numpy

from modelo.imagem_rgb import ImagemRGB


class ImagemTonsCinza:
    """
    Representa uma matriz de tons de cinza.
    """

    def __init__(self, matriz=None, imagem_rgb: ImagemRGB = None):
        """
        Constrói uma nova instância da classe ImagemTonsCinza.
        :param matriz: Matriz de tons de cinza.
        :param imagem_rgb: Instância da classe ImagemRGB a ser convertida.
        """
        if matriz is not None:
            self.matriz = matriz
        elif imagem_rgb is not None:
            self.matriz = numpy.dot(imagem_rgb.matriz[..., :3], [0.2989, 0.5870, 0.1140])

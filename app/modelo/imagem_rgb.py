import PIL.Image
import numpy


class ImagemRGB:
    """
    Representa uma imagem RGB.
    """
    def __init__(self, matriz=None, caminho_arquivo=None):
        """
        Constrói uma nova instância de ImagemRGB.
        :param matriz: Matriz RGB.
        :param caminho_arquivo: Caminho do arquivo.
        """
        if matriz is not None:
            self.matriz = matriz
        elif caminho_arquivo is not None:
            imagem = PIL.Image.open(caminho_arquivo)
            imagem_rgb = imagem.convert('RGB')
            self.matriz = numpy.array(imagem_rgb)

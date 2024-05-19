import PIL.Image
import numpy


class ImagemRGB:
    """
    Representa uma imagem RGB.
    """
    def __init__(self, matriz):
        """
        Constrói uma nova instância de ImagemRGB.
        :param matriz: Matriz RGB.
        """
        self.matriz = matriz

    @staticmethod
    def abrir_arquivo(caminho):
        """
        Constrói uma instância da classe ImagemRGB a partir de um arquivo.
        :param caminho: Caminho do arquivo de imagem.
        :return: Instância da classe ImagemRGB.
        """
        imagem = PIL.Image.open(caminho)
        imagem_rgb = imagem.convert('RGB')
        return ImagemRGB(numpy.array(imagem_rgb))

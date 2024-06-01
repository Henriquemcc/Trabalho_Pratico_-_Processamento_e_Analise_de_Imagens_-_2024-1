from PIL import Image
import numpy

from .imagem import Imagem
from .imagem_hsv import ImagemHSV
from .imagem_tons_cinza import ImagemTonsCinza


class ImagemRGB(Imagem):
    """
    Representa uma imagem RGB.
    """

    @staticmethod
    def from_file(file_path):
        """
        Cria uma classe ImagemRGB a partir de um arquivo de imagem (.png, .jpg ou .jpeg).
        :param file_path: Caminho do arquivo da imagem.
        :return: Instância da classe ImagemRGB criado a partir do arquivo de imagem.
        """
        imagem = Image.open(file_path)
        imagem = imagem.convert('RGB')
        return ImagemRGB(numpy.array(imagem))

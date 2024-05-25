import PIL.Image
import numpy

from modelo.imagem import Imagem
from modelo.imagem_tons_cinza import ImagemTonsCinza


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
        imagem = PIL.Image.open(file_path)
        imagem_rgb = imagem.convert('RGB')
        return ImagemRGB(numpy.array(imagem_rgb))

    def to_imagem_tons_cinza(self) -> ImagemTonsCinza:
        """
        Gera uma instância da classe ImagemTonsCinza a partir da classe ImagemRGB.
        :return: ImagemTonsCinza gerado a partir de ImagemRGB.
        """
        return ImagemTonsCinza(numpy.array(self.to_image().convert('L')))

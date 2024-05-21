import PIL.Image
import numpy

from modelo.imagem_tons_cinza import ImagemTonsCinza


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

    def to_image(self) -> PIL.Image.Image:
        """
        Converte ImagemRGB em uma PIL.Image.Image
        :return: PIL.Image.Image gerada a partir de ImagemRGB.
        """
        return PIL.Image.fromarray(self.matriz)

    def to_imagem_tons_cinza(self) -> ImagemTonsCinza:
        """
        Gera uma instância da classe ImagemTonsCinza a partir da classe ImagemRGB.
        :return: ImagemTonsCinza gerado a partir de ImagemRGB.
        """
        return ImagemTonsCinza(numpy.dot(self.matriz[..., :3], [0.2989, 0.5870, 0.1140]))

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

import numpy

from PIL import Image
from .imagem import Imagem


class ImagemHSV(Imagem):
    """
    Representa uma imagem HSV.
    """

    @staticmethod
    def from_file(file_path):
        """
        Cria uma classe ImagemHSV a partir de um arquivo de imagem (.png, .jpg ou .jpeg).
        :param file_path: Caminho do arquivo da imagem.
        :return: Instância da classe ImagemHSV criado a partir do arquivo de imagem.
        """
        imagem = Image.open(file_path)
        imagem = imagem.convert('HSV')
        return ImagemHSV(numpy.array(imagem))

    @staticmethod
    def from_image(imagem):
        """
        Cria uma ImagemHSV a partir de uma imagem.
        :param imagem: Imagem a partir da qual será criada a imagem HSV.
        :return: Instância da classe ImagemHSV criado a partir da imagem.
        """
        return ImagemHSV(numpy.array(imagem.to_image().convert('HSV')))

    def to_histograma(self, n_bin=(16, 16, 16)):
        """
        Gera um histograma da imagem HSV.
        """
        intervalo = [256 // bin_ for bin_ in n_bin]
        histograma_hue = {x*intervalo[0] : 0 for x in range(n_bin[0])}
        histograma_saturation = {x*intervalo[1] : 0 for x in range(n_bin[1])}
        histograma_value = {x*intervalo[2] : 0 for x in range(n_bin[2])}
        for linha in range(self.matriz.shape[0]):
            for coluna in range(self.matriz.shape[1]):

                # Obtendo os valores de hue, saturation e value do pixel
                hue, saturation, value = self.matriz[linha][coluna]

                # Contando a quantidade de pixels com cada valor de hue
                hue = (hue // intervalo[0]) * intervalo[0]
                if hue in histograma_hue:
                    histograma_hue[hue] += 1
                else:
                    histograma_hue[hue] = 1

                # Contando a quantidade de pixels com cada valor de saturation
                saturation = (saturation // intervalo[1]) * intervalo[1]
                if saturation in histograma_saturation:
                    histograma_saturation[saturation] += 1
                else:
                    histograma_saturation[saturation] = 1

                # Contando a quantidade de pixels com cada valor de value
                value = (value // intervalo[2]) * intervalo[2]
                if value in histograma_value:
                    histograma_value[value] += 1
                else:
                    histograma_value[value] = 1

        return histograma_hue, histograma_saturation, histograma_value

    def to_histograma_2d(self, n_bin=(16, 128)):
        """
        Gera um histograma 2D da imagem HSV.
        """
        intervalo = [256 // bin_ for bin_ in n_bin]
        histograma_2d = {pair: 0 for pair in ((x*intervalo[0], y*intervalo[1]) for x in range(n_bin[0]) for y in range(n_bin[1]))}
        print(histograma_2d)
        for linha in range(self.matriz.shape[0]):
            for coluna in range(self.matriz.shape[1]):

                # Obtendo os valores de hue e value do pixel
                hue, _, value = self.matriz[linha][coluna]
                hue = (hue // intervalo[0]) * intervalo[0]
                value = (value // intervalo[1]) * intervalo[1]

                # Contando a quantidade de pixels com cada valor de hue e value
                histograma_2d[(hue, value)] += 1

        return histograma_2d

import cv2
import numpy

from .imagem import Imagem
from PIL import Image


class ImagemTonsCinza(Imagem):
    """
    Representa uma matriz de tons de cinza.
    """

    @staticmethod
    def from_file(file_path):
        """
        Cria uma classe ImagemTonsCinza a partir de um arquivo de imagem (.png, .jpg ou .jpeg).
        :param file_path: Caminho do arquivo da imagem.
        :return: Instância da classe ImagemTonsCinza criado a partir do arquivo de imagem.
        """
        imagem = Image.open(file_path)
        imagem = imagem.convert('L')
        return ImagemTonsCinza(numpy.array(imagem))

    @staticmethod
    def from_image(imagem):
        """
        Cria uma ImagemTonsCinza a partir de uma imagem.
        :param imagem: Imagem a partir da qual será criada a imagem em tons de cinza.
        :return: Instância da classe ImagemTonsCinza criado a partir da imagem.
        """
        return ImagemTonsCinza(numpy.array(imagem.to_image().convert('L')))

    def to_histograma(self, n_bin=16):
        """
        Gera um histograma da imagem.
        :param n_bin: Número de caixas do histograma.
        """
        histograma = {}
        intervalo = 256 // n_bin
        for linha in range(self.matriz.shape[0]):
            for coluna in range(self.matriz.shape[1]):
                pixel = (self.matriz[linha][coluna] // intervalo) * intervalo
                if pixel in histograma:
                    histograma[pixel] += 1
                else:
                    histograma[pixel] = 1
        return histograma

    def to_momentos_invariantes_hu(self):
        """
        Calcula os Momentos Invariantes de Hu.
        """
        momentos = cv2.moments(self.matriz)
        momentos_hu = cv2.HuMoments(momentos)
        return momentos_hu

import cv2

from modelo.imagem import Imagem


class ImagemTonsCinza(Imagem):
    """
    Representa uma matriz de tons de cinza.
    """

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

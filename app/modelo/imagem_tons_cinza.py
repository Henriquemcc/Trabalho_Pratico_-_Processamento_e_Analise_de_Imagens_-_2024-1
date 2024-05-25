from modelo.imagem import Imagem


class ImagemTonsCinza(Imagem):
    """
    Representa uma matriz de tons de cinza.
    """

    def to_histograma(self):
        """
        Gera um histograma da imagem.
        """
        histograma = {}
        for linha in range(self.matriz.shape[0]):
            for coluna in range(self.matriz.shape[1]):
                pixel = self.matriz[linha][coluna]
                if pixel in histograma:
                    histograma[pixel] += 1
                else:
                    histograma[pixel] = 1
        return histograma

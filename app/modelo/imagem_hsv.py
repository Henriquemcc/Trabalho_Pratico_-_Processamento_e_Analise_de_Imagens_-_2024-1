from modelo.imagem import Imagem


class ImagemHSV(Imagem):
    """
    Representa uma imagem HSV.
    """
    def to_histograma(self):
        """
        Gera um histograma da imagem HSV.
        """
        histograma_hue = {}
        histograma_saturation = {}
        histograma_value = {}
        for linha in range(self.matriz.shape[0]):
            for coluna in range(self.matriz.shape[1]):

                # Obtendo os valores de hue, saturation e value do pixel
                hue, saturation, value = self.matriz[linha][coluna]

                # Contando a quantidade de pixels com cada valor de hue
                if hue in histograma_hue:
                    histograma_hue[hue] += 1
                else:
                    histograma_hue[hue] = 1

                # Contando a quantidade de pixels com cada valor de saturation
                if saturation in histograma_saturation:
                    histograma_saturation[saturation] += 1
                else:
                    histograma_saturation[saturation] = 1

                # Contando a quantidade de pixels com cada valor de value
                if value in histograma_value:
                    histograma_value[value] += 1
                else:
                    histograma_value[value] = 1

        return histograma_hue, histograma_saturation, histograma_value

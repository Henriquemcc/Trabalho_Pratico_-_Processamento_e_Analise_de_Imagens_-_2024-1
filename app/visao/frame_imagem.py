import tkinter

from PIL import ImageTk


class FrameImagem(tkinter.Frame):
    """
    Frame utilizado na exibição de imagens.
    """

    def __init__(self, parent, controller):
        """
        Constrói uma nova instância do FrameImagem.
        :param parent: Widget pai.
        :param controller: Controlador que instanciou esta classe.
        """
        tkinter.Frame.__init__(self, parent)
        self.__image = None
        self.__legenda = None
        self.controller = controller
        self.label = tkinter.Label(self)
        self.label.pack(fill="both", expand=True)

    @property
    def image(self):
        """
        Obtém a imagem atual.
        :return:
        """
        return self.__image

    @image.setter
    def image(self, image):
        """
        Altera a imagem atual.
        :param image: Imagem a ser colocada no lugar.
        :return:
        """
        self.__image = image
        self.__imagem_atualizada()

    @property
    def legenda(self):
        """
        Obtém a legenda atual.
        :return: Legenda atual.
        """
        return self.__legenda

    @legenda.setter
    def legenda(self, legenda):
        """
        Altera a legenda atual.
        :param legenda: Legenda a ser colocada no lugar.
        :return:
        """
        self.__legenda = legenda
        self.__imagem_atualizada()

    def __imagem_atualizada(self):
        """
        Ação executada quando a imagem é atualizada.
        :return:
        """
        image = self.image
        label_width = self.label.winfo_width()
        label_height = self.label.winfo_height()
        if label_width > 1 and label_height > 1:
            image = image.resize((label_width, label_height))
        photo_image = ImageTk.PhotoImage(image)
        self.label.config(image=photo_image, text=self.legenda)
        self.label.image = photo_image

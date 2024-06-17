import tkinter


class FrameDescritoresHaralick(tkinter.Frame):
    """
    Classe responsável por criar um frame que exibe os descritores de Haralick.
    """

    def __init__(self, parent, controller):
        """
        Constrói uma nova instância do FrameDescritoresHaralick.
        :param parent: Widget pai.
        :param controller: Controlador que instanciou esta classe.
        """
        self.__descritores_haralick = None
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        titulo = tkinter.Label(self, text="Descritores de Haralick")
        titulo.pack(side="top", fill="x", pady=10)
        self.label_descritor_haralick = []
        for i in range(7):
            label = tkinter.Label(self, text="")
            label.pack(side="top", fill="x", pady=10)
            self.label_descritor_haralick.append(label)

    @property
    def descritores_haralick(self):
        """
        Obtém o valor do atributo descritores_haralick.
        :return: Valor do atributo descritores_haralick.
        """
        return self.__descritores_haralick

    @descritores_haralick.setter
    def descritores_haralick(self, value):
        """
        Altera o valor do atributo descritores_haralick.
        :param value: Novo valor para o atributo descritores_haralick.
        :return:
        """
        self.__descritores_haralick = value
        for i in range(min(6, len(value))):
            self.label_descritor_haralick[i].config(text="{}: {}".format(value[i][0], value[i][1]))

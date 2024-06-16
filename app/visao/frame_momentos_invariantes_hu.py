import tkinter


class FrameMomentosInvariantesHu(tkinter.Frame):
    """
    Frame para mostrar os momentos invariantes de Hu.
    """

    def __init__(self, parent, controller):
        """
        Constrói uma nova instância do FrameMomentosInvariantesHu.
        :param parent: Widget pai.
        :param controller: Controlador que instanciou esta classe.
        """
        self.__momentos_hu = None
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        titulo = tkinter.Label(self, text="Momentos Invariante de Hu")
        titulo.pack(side="top", fill="x", pady=10)
        self.label_momento_hu = []
        for i in range(7):
            label = tkinter.Label(self, text="")
            label.pack(side="top", fill="x", pady=10)
            self.label_momento_hu.append(label)

    @property
    def momentos_hu(self):
        """
        Obtém o valor do atributo momentos_hu.;
        :return: Valor do atributo momentos_hu.
        """
        return self.__momentos_hu

    @momentos_hu.setter
    def momentos_hu(self, value):
        """
        Altera o valor do atributo momentos_hu.
        :param value: Novo valor para o atributo momentos_hu.
        :return:
        """
        print(value)
        self.__momentos_hu = value
        for i in range(min(7, len(value))):
            self.label_momento_hu[i].config(text=value[i][0])



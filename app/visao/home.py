import tkinter


class Home(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        """
        Constrói uma nova instância da JanelaPrinpal.
        :param controlador: Controlador que está criando esta JanelaPrincipal.
        """
        self.controller = controller

        label = tkinter.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

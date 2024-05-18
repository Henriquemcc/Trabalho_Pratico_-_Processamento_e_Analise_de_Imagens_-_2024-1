import tkinter as tk

class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        """
        Constrói uma nova instância da JanelaPrinpal.
        :param controlador: Controlador que está criando esta JanelaPrincipal.
        """
        self.controller = controller

        label = tk.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

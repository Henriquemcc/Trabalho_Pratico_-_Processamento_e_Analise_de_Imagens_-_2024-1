import tkinter

class FramePrincipal(tkinter.Frame):
    """
    Frame Principal.
    """

    def __init__(self, parent, controller):
        """
        Constrói uma nova instância do FramePrincipal.
        :param parent: Widget pai.
        :param controller: Controlador que instanciou esta classe.
        """
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        titulo = tkinter.Label(self, text="Trabalho Prático - Processamento e Análise de Imagens - 2024-1")
        titulo.pack(side="top", fill="x", pady=10)
        autor1 = tkinter.Label(self, text="Felipe Costa Amaral")
        autor1.pack(side="top", fill="x", pady=10)
        autor2 = tkinter.Label(self, text="Henrique Mendonça Castelar Campos")
        autor2.pack(side="top", fill="x", pady=10)
        autor3 = tkinter.Label(self, text="Larissa Kaweski Siqueira")
        autor3.pack(side="top", fill="x", pady=10)

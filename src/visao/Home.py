from tkinter import Frame,Label
from PIL import Image, ImageTk

class Home(Frame):

    def __init__(self, parent, controlador=None, image_controlador=None):
        Frame.__init__(self, parent)
        """
        Constrói uma nova instância da JanelaPrinpal.
        :param controlador: Controlador que está criando esta JanelaPrincipal.
        """

        # Controlador que instanciou a janela principal
        self.controlador = controlador
        self.image_controlador = image_controlador

        label = Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)
        self.image_label = Label(self, text="This is the image spot", image=None)
        self.image_label.pack(side="top", fill="both")

        image_controlador.on_image_loaded.append(self.when_image_loaded)

    def when_image_loaded(self):
        print("when image from home")
        if self.image_controlador.image is not None:
            print("has image from home")
            # Convert the image to Tkinter-compatible format
            tk_image = ImageTk.PhotoImage(self.image_controlador.image)

            # Create a label widget to display the image
            self.image_label.config(text="", image=tk_image)
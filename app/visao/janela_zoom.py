import tkinter as tk
import tkinter


class JanelaZoom(tkinter.Tk):
    def __init__(self, controlador, adicionar_imagem):
        # Cria a janela principal
        super().__init__()
        self.title("Janela de Zoom")

        self.controlador = controlador
        self.adicionar_imagem = adicionar_imagem

        # Labels e entradas para as coordenadas
        tk.Label(self, text="Min X: {}".format(controlador.max_zoom[0][0])).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Max X: {}".format(controlador.max_zoom[0][1])).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="Min Y: {}".format(controlador.max_zoom[1][0])).grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self, text="Max Y: {}".format(controlador.max_zoom[1][1])).grid(row=2, column=1, padx=5, pady=5)

        self.min_x_entry = tk.Entry(self)
        self.max_x_entry = tk.Entry(self)
        self.min_y_entry = tk.Entry(self)
        self.max_y_entry = tk.Entry(self)

        self.min_x_entry.grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=10)
        self.max_x_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=10, ipady=10)
        self.min_y_entry.grid(row=3, column=0, padx=5, pady=5, ipadx=10, ipady=10)
        self.max_y_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=10, ipady=10)

        # Botão aplicar
        aplicar_button = tk.Button(self, text="Aplicar", command=self.aplicar_zoom)
        aplicar_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")

        # Inicia o loop principal da janela
        self.mainloop()

    def aplicar_zoom(self):
        self.controlador.set_zoom(
            [
                [int(self.min_x_entry.get()), int(self.max_x_entry.get())],
                [int(self.min_y_entry.get()), int(self.max_y_entry.get())]
            ],
            self.adicionar_imagem
        )
        self.destroy()

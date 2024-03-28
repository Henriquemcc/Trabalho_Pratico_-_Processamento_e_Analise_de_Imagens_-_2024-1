import tkinter.filedialog


class DialogoArquivo:
    """
    Exibe um diálogo ao abrir ou salvar arquivos.
    """
    def __init__(self, file_types):
        """
        Constrói uma nova instância da classe DialogoArquivo.
        :param file_types: Iterável com tuplas dos tipos de arquivos que podem ser abertos ou salvos e sua descrição.
        """
        self.file_types = file_types

    def abrir_arquivo(self) -> str:
        """
        Exibe uma caixa de diálogo para abrir um arquivo.
        :return: Caminho do arquivo escolhido.
        """
        return tkinter.filedialog.askopenfilename(filetypes=self.file_types)

    def salvar_arquivo(self) -> str:
        """
        Exibe uma caixa de diálogo para salvar um arquivo.
        :return: Caminho do arquivo escolhido.
        """
        return tkinter.filedialog.asksaveasfilename(filetypes=self.file_types)

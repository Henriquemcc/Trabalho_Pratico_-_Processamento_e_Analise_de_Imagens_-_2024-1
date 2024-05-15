from visao.DialogoArquivo import DialogoArquivo
from visao.JanelaPrincipal import JanelaPrincipal


class Controlador:
    """
    Controlador.
    """

    def __init__(self):
        """
        Constrói uma nova instância de Controlador.
        """
        self.janela_principal = JanelaPrincipal(self)
        self.janela_principal.exibir()

    def abrir_arquivo_imagem(self) -> None:
        """
        Realiza a abertura de um arquivo de imagem.
        :return:
        """
        tipos_arquivos = [("Portable Network Graphics", ".png"), ("Joint Photographic Experts Group", ".jpeg"), ("Joint Photographic Experts Group", ".jpg")]
        dialogo_arquivo = DialogoArquivo(tipos_arquivos)
        caminho = dialogo_arquivo.abrir_arquivo()
        print("caminho =", caminho, sep=" ")
        self.janela_principal.adicionar_imagem(caminho)


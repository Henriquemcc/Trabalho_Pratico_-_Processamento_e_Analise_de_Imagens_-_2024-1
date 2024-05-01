from visao.DialogoArquivo import DialogoArquivo
from PIL import Image

class ImageController:
    """
    Controlador.
    """

    def __init__(self):
        """
        Constrói uma nova instância de Controlador.
        """
        self.caminho = None
        self.image = None

        self.on_image_loaded = []

    def abrir_arquivo_imagem(self) -> None:
        """
        Realiza a abertura de um arquivo de imagem.
        :return:
        """
        tipos_arquivos = [("Portable Network Graphics", ".png"), ("Joint Photographic Experts Group", ".jpeg"), ("Joint Photographic Experts Group", ".jpg")]
        dialogo_arquivo = DialogoArquivo(tipos_arquivos)

        self.caminho = dialogo_arquivo.abrir_arquivo()
        self.image = Image.open(self.caminho)
        print("loaded image at controler")
        for event in self.on_image_loaded:
            event()

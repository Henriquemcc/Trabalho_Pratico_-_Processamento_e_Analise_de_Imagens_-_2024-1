import pandas
import os
import PIL.Image

# Definindo variáveis
data_frame = pandas.read_csv("classifications.csv")
data_set_dir = os.path.join(os.getcwd(), "dataset")
destination_image_dir = os.path.join(os.getcwd(), "dataset_converted")

# Criando diretório de destino
if not os.path.exists(destination_image_dir):
    os.mkdir(destination_image_dir)

# Cortando imagens
for index, row in data_frame.iterrows():

    source_image_path = os.path.join(data_set_dir, row['image_filename'])

    classe = row['bethesda_system']
    diretorio_classe = os.path.join(destination_image_dir, classe)
    if not os.path.exists(diretorio_classe):
        os.mkdir(diretorio_classe)
    
    destination_image_path = os.path.join(diretorio_classe, "{}.png".format(row['cell_id']))
    
    if os.path.exists(source_image_path):
        with PIL.Image.open(source_image_path) as image:
            esquerda = row['nucleus_x'] - 50
            direita = row['nucleus_x'] + 50
            inferior = row['nucleus_y'] - 50
            superior = row['nucleus_y'] + 50
            cropped_image = image.crop((esquerda, inferior, direita, superior))
            cropped_image.save(destination_image_path) 
    



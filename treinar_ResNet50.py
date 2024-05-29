# Treina o modelo ResNet50

# Importando requisitos
print('Importando requisitos...')
from app.modelo.imagem_rgb import ImagemRGB
import sklearn.model_selection
import pandas
import tensorflow
import os
import numpy
import pickle
import random

# Definindo variáveis
print('Definindo variáveis...')
image_directory = os.path.join(os.getcwd(), 'dataset_converted')
num_classes = 6

# Abrindo base de dados
print('Abrindo base de dados...')
data_frame = pandas.read_csv("classifications.csv")
data_frame['random'] = data_frame[data_frame.columns[0]].apply(lambda _: random.random())
data_frame.sort_values(
    by='random',
    inplace=True
)

# Separando o x
print('Separando o x...')
x = []
for index, row in data_frame.iterrows():
    x.append(os.path.join(image_directory, row['bethesda_system'], "{}.png".format(row['cell_id'])))
x = pandas.array(x)

# Separando o y
print('Separando o y...')
y = data_frame.iloc[:, 4].values
label_encoder = sklearn.preprocessing.LabelEncoder()
y = label_encoder.fit_transform(y)

# Separando o conjunto de treino e teste
print('Separando o conjunto de treino e teste...')
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y)

# Exportando x_test, x_train, y_test, y_train para um arquivo externo
print('Exportando x_test, x_train, y_test, y_train para um arquivo externo...')
with open('data.pkl', mode='wb') as file:
    pickle.dump([x_train, x_test, y_train, y_test], file)

# Aplicando o ResNet50
print('Aplicando o ResNet50...')

# Construindo o modelo
print('Construindo o modelo...')
input_tensor = tensorflow.keras.layers.Input(shape=(100, 100, 3))
modelo_base = tensorflow.keras.applications.resnet50.ResNet50(weights='imagenet', include_top=False, input_tensor=input_tensor)
mbo = modelo_base.output
mbo = tensorflow.keras.layers.GlobalAveragePooling2D()(mbo)
mbo = tensorflow.keras.layers.Dense(1024, activation='relu')(mbo)
predicoes = tensorflow.keras.layers.Dense(num_classes, activation='softmax')(mbo)

modelo = tensorflow.keras.models.Model(inputs=modelo_base.input, outputs=predicoes)

for layer in modelo_base.layers:
    layer.trainable = False

# Compilando
print('Compilando...')
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy', 'recall', 'precision'])

# Treinando o modelo
print('Treinando o modelo...')
def preprocessar_imagem(imagem):
    if isinstance(imagem, numpy.ndarray):
        imagem = imagem/255.0
    else:
        raise ValueError("Imagem deve ser um numpy array")
    
    imagem = tensorflow.convert_to_tensor(imagem, dtype=tensorflow.float32)
    imagem = tensorflow.expand_dims(imagem, axis=0)
    return imagem

for index, image_path in enumerate(x_train):
    if (os.path.exists(image_path)):
        imagem_rgb = ImagemRGB.from_file(image_path)
        imagem_preprocessada = preprocessar_imagem(imagem_rgb.matriz)
        label = tensorflow.keras.utils.to_categorical(y_train[index], num_classes)
        label = tensorflow.convert_to_tensor(label, dtype=tensorflow.int8)
        label = tensorflow.expand_dims(label, axis=0)
        modelo.fit(x=numpy.array(imagem_preprocessada), y=label)

# Exportando o modelo treinado
print('Exportando o modelo treinado...')
modelo.save('modelo.keras')
modelo.save_weights('pesos.weights.h5')

# Testando o modelo
print('Testando o modelo...')
predicoes = []
for index, image_path in enumerate(x_test):
    if (os.path.exists(image_path)):
        imagem_rgb = ImagemRGB.from_file(image_path)
        imagem_preprocessada = preprocessar_imagem(imagem_rgb.matriz)
        predicao = modelo.predict(imagem_preprocessada)
        predicoes.append(predicao)
predicoes = numpy.array(predicoes)

# Exportando as predições
print('Exportando as predições...')
with open('predicoes.pkl', mode='wb') as file:
    pickle.dump(predicoes, file)
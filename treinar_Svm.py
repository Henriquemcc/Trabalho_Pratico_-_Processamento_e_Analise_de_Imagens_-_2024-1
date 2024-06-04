# %% [markdown]
# # SVM

# %% [markdown]
# Instalando requisitos

# %%
#%pip install -r requirements.txt -q
#%pip install pandas -q
#%pip install scikit-learn -q
#%pip install tensorflow -q
#%pip install numpy -q

# %% [markdown]
# Importando requisitos

# %%
from app.modelo.imagem_rgb import ImagemRGB
import sklearn.model_selection
import pandas
import tensorflow
import os
import numpy
import pickle
import random
from sklearn import svm

# %% [markdown]
# Definindo variáveis

# %%
image_directory = os.path.join(os.getcwd(), 'dataset_converted')
num_classes = 6

# %% [markdown]
# Abrindo base de dados

# %%
data_frame = pandas.read_csv("classifications.csv")

# %% [markdown]
# Adicionando coluna path

# %%
for index, row in data_frame.iterrows():
    data_frame.at[index, 'path'] = os.path.join(image_directory, row['bethesda_system'], "{}.png".format(row['cell_id']))

# %%
data_frame

# %% [markdown]
# Adicionando coluna random e ordenando por meio dela

# %%
data_frame['random'] = data_frame[data_frame.columns[0]].apply(lambda _: random.random())

# %%
data_frame.sort_values(
    by='random',
    inplace=True
)

# %% [markdown]
# Removendo imagens que não existem

# %%
for index, row in data_frame.iterrows():
    if not os.path.exists(row['path']):
        data_frame.drop(index, inplace=True)

# %%
data_frame

# %% [markdown]
# Separando o x

# %%
data_frame['path'].iloc[0]

# %%
xi = ImagemRGB.from_file(data_frame['path'].iloc[0]).matriz.flatten()
xi

# %%
xi.shape

# %%
x = []
for index, row in data_frame.iterrows():
    image = ImagemRGB.from_file(row['path'])
    x.append(image.matriz.flatten()/255)
x = numpy.array(x)

# %%
x.shape

# %%
x

# %% [markdown]
# Separando o y

# %%
y = data_frame.iloc[:, 4].values
#label_encoder = sklearn.preprocessing.LabelEncoder()
#y = label_encoder.fit_transform(y)

# %%
labels = list(set(data_frame.iloc[:, 4].values))

# %%
labels

# %%
y = [[1 if label==lbl else 0 for lbl in labels] for label in y]

# %%
y = numpy.array(y)

# %%
y

# %%
type(y)

# %%
y.shape

# %% [markdown]
# Separando o conjunto de treino e teste

# %%
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y)

# %%
y_train

# %%
x_train.shape

# %%
y_train.shape

# %%
x_test.shape

# %%
y_test.shape

# %% [markdown]
# Exportando x_test, x_train, y_test, y_train para um arquivo externo

# %%
#with open('data.pkl', mode='wb') as file:
    #pickle.dump([x_train, x_test, y_train, y_test], file)

# %% [markdown]
# # Aplicando o SVM

# %% [markdown]
# Construindo o modelo

# %%
modelo = svm.SVC()

# %% [markdown]
# Treinando o modelo

# %%
modelo.fit(x_train, y_train)

# %%
import joblib
joblib.dump(modelo, 'modelo.pkl')

# %%
with open('modelo.pkl', mode='wb') as file:
    pickle.dump(modelo, file)

# %%




[Versão em Português](README.md)

# Practical Work - Image Processing and Analysis - 2024-1

## Statement

### Cell recognition in Pap smears

**Delivery date:** 06/11/2024 until 11:00 pm via Canvas

**Value: 35** points

**Penalty for delay: Full amount, no delay allowed!**

**Groups:** 2 or 3 components

#### Description:

The Pap smear is a histological examination performed to detect changes in the cells of the cervix. being the main method of detecting lesions for the early diagnosis of cervical cancer. In this work, you must implement an application that reads Pap smear images and enables automatic recognition of cancer cells.

#### Program specifications:

a) The program must be implemented in C++, Python or Java.

b) The use of elementary library functions is permitted. An elementary function means a basic image manipulation function, the result of which is not the final solution to the problem. Ex: reading files, calculating histograms, filters, calculating distances, converting between image formats, calculating features, classifiers. The main code that uses the functions must be original to the group.

#### 1st stage:

1\) The data used in training and testing the classifiers must be preprocessed. Through the classifications.csv spreadsheet. Obtain the coordinates of the cell nuclei from the images available in the dataset (only a part of the images is available). Crop the images, generating a 100x100 sub-image for each cell and store in sub-directories according to their class. The image name must be the cell number in the worksheet. The README.md file contains the description of the classes.

2\) Implement a fully graphical environment with a menu for the following functionalities:

- Menu to read and view images in PNG and JPG formats. Images can have any resolution;
- Menu to convert the image to grayscale and display it.
- Menu to generate the grayscale and color histogram in HSV space and display them.
- Menu to characterize the image in gray tones using Haralick descriptors, showing the calculated values.
- Menu to characterize the image in grayscale and color channels through the invariant moments of Hu showing the calculated values.
- Menu to classify a sub-image using the techniques selected for the group, indicating which class was found.

3\) Implement the functionality of reading and displaying images in colors and grayscale with zoom option;

4\) Implement the grayscale histogram generation functionality for the image with 16 tones.

5\) Implement the functionality for generating image color histograms with quantization of 16 values for the H channel and 8 values for the V (2D histogram with 16*8 inputs).

6\) Calculate the co-occurrence matrices Ci,i where i=1,2,4,8,16 and 32, considering 16 shades of gray.

7\) Calculate the Haralick Entropy, Homogeneity and Contrast descriptors for the co-occurrence matrices of the previous item (3*6 characteristics)

8\) Calculate the Hu invariant moments for the image in 256 shades of gray and for the 3 original channels of the HSV model (4*7 features)

#### 2nd step: To specify this step, calculate the following numbers:

NF=(sum of the registration numbers of the group components) mod 3

NC=(sum of the registration numbers of the group components) mod 2

ND=((sum of registration numbers of group components) mod 4) div 2

If NF=0, the features used will be the 2D histogram values (HxV, 16 *8 features) Otherwise if N=1, the features used will be the calculated Haralick descriptors (3* 6 features), Otherwise the features used will be the Hu moments (4*7 characteristics).

If NC=0, the shallow classifier will be SVM, otherwise it will be XGBoost.

If ND=0, the deep classifier will be ResNet50 otherwise it will be EfficientNet.

1\) Separate the data into 2 randomly drawn sets: the training set must have 80% of the data and the test set 20%. Each class must be separated in this 4:1 ratio into the training and testing sets to ensure balance.

2\) Implement two shallow classifiers for the problem, according to NC, the first being binary (negative class X too many) and the second with 6 classes. Evaluate the accuracy and show the confusion matrices for each. The features used as input to the classifiers depend on NF.

3\) Implement two deep classifiers for the problem, according to ND, the first being binary (negative class X too many) and the second with 6 classes. Adjust the weights already available in the libraries that were trained with ImageNet (fine tuning). Evaluate the accuracy and show the confusion matrices for each one. Plot learning graphs (training and testing accuracy after each epoch). The inputs to the classifiers are the cropped sub-images.

4\) Compare the results obtained between the solutions.

5\) The documentation IN LATEX FORMAT AND CORRESPONDING PDF must be in the form of an article with SBC style, containing:

    a) Description of the problem.

    b) Description of the techniques implemented for the solution, mainly the classifiers and characteristics.

    c) References of libraries used in the implementation.

    d) Execution time measurements for various images, descriptors and hyperparameters of the classifier.

    e) Analysis of the results obtained in the tests, examples of errors and successes of the methods.

    f) Bibliographic references.

#### What to deliver:

Source files and documentation. Place all files in the root of a directory whose name must be the registration number of one of the components. Compress the directory and post to Canvas (link in drive does not work) by the specified time. The total size of the files must not exceed 20 Mbytes. DO NOT INCLUDE THE DATABASE!

Note: Higher quality work may earn extra points.

#### Reference article:

Rezende, M.T., Silva, R., Bernardo, F.d.O. et al. Cric searchable image database as a public platform for conventional pap smear cytology data. Sci Data 8, 151 (2021). https://doi.org/10.1038/s41597-021-00933-8

## Screenshots

![A window with a frame and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The window frame contains the names of the group members: 'Felipe Costa Amaral', 'Henrique Mendonça Castelar Campos' and 'Larissa Kaweski Siqueira'](screenshots/Captura_de_tela_2024-06-10_094756.png)

*Main window, when the program starts.*

![A window with an image frame and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The image frame contains an image of a Pap smear cell.](screenshots/Captura_de_tela_2024-06-10_094827.png)

*Main window, when an image is opened.*

![A window with an image frame and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The image frame contains an image of a Pap smear cell. The image is in black and white.](screenshots/Captura_de_tela_2024-06-10_094843.png)

*Main window, displaying a grayscale image.*

![A window with an image frame and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The image frame contains an image of a Pap smear cell. The image has a different color scheme.](screenshots/Captura_de_tela_2024-06-10_094858.png)

*Main window, displaying an HSV image.*

![A window with a frame with a histogram and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The histogram is represented by a 13-bar bar graph.](screenshots/Captura_de_tela_2024-06-10_094919.png)

*Main window, displaying the histogram of an image in shades of gray.*

![A window with a frame with a histogram and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The histogram is represented by a 16-bar bar graph.](screenshots/Captura_de_tela_2024-06-10_094944.png)

*Main window, displaying the Hue histogram of the HSV image.*

![A window with a frame with a histogram and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The histogram is represented by a bar graph.](screenshots/Captura_de_tela_2024-06-10_095002.png)

*Main window, displaying the Saturation histogram of the HSV image.*

![A window with a frame with a histogram and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The histogram is represented by a bar graph.](screenshots/Captura_de_tela_2024-06-10_095102.png)

*Main window, displaying the Value histogram of the HSV image.*

![A window with a frame with a histogram and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The histogram is represented by a 2D bar graph.](screenshots/Captura_de_tela_2024-06-10_095121.png)

*Main window, displaying the 2D histogram of the HSV image.*

![A window with the image classification frame and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The image classification frame has the title: 'Classificador' (Classifier), and a subtitle 'Tipo de classificação' (Classification type), the radio buttons 'Binário' (Binary) and 'Multiclasse' (Multiclass), and the buttons 'Classificar SVM' (Classify SVM) and 'Classificar ResNet50' (Classify ResNet50), and the texts 'ASC-H' and 'Trmpo gasto: 0.0720735s' (Time taken: 0.0720735s).](screenshots/Captura_de_tela_2024-06-16_120712.png)

*Main window, displaying options for classifying the image.*

![A window with a frame with Hu Invariant Moments and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The frame with the Invariant Moments of Hu has the title 'Momentos Invariante de Hu' (Invariant Moments of Hu), and the texts: '2.9908410420185008', '8.579090833437313', '11.120241129487834', '11.037662984594114', '-22.1187638' 5396171', '-15.528629006286437' and '23.11996647629501'.](screenshots/Captura_de_tela_2024-06-16_215855.png)

*Main window, showing Hu Invariant Moments.*

![A window with a frame with Haralick Descriptors and a menu bar. The menu bar contains the menus: 'Arquivo' (File), 'Visualizar' (View), 'Converter' (Convert), 'Histogramas' (Histograms), 'Caracterizar' (Characterize) and 'Classificar' (Classify). The frame with Haralick Descriptors has the title 'Descritores de Haralick' (Haralick Descriptors), and the texts: 'contrast: 109.5192490562188', 'dissimilarity: 7.208828690949891', 'homogeneity: 0.1580393989047433', 'energy: 0.020326476858 105555', 'correlation: 0.9743702523392569', 'ASM: 0.0004155669006214171'](screenshots/Captura_de_tela_2024-06-16_215907.png)

*Main window, showing Haralick Descriptors.*

## How to run

To run the program, follow these steps:

### Use a virtual environment (optional)

#### Create the virtual environment

In the shell (Terminal, Command Prompt or PowerShell) inside the project folder, type:

```
python3 -m venv venv
```

or

```
python -m venv venv
```

#### Activate the virtual environment

If your shell (Terminal, Command Prompt or PowerShell) is Linux or Mac OS Bash, inside the project folder, type:

```
source venv/bin/activate
```

If your shell (Terminal, Command Prompt or PowerShell) is Windows Command Prompt, inside the project folder, type:

```
venv\Scripts\activate.bat
```

If your shell (Terminal, Command Prompt or PowerShell) is Windows PowerShell, inside the project folder, type:

```
.\venv\Scripts\Activate.ps1
```

### Install the dependencies

In the shell (Terminal, Command Prompt or PowerShell) inside the project folder, type:

```
pip install -r requirements.txt
```

### Download the classification models

In [releases](https://github.com/Henriquemcc/Trabalho_Pratico_-_Processamento_e_Analise_de_Imagens_-_2024-1/releases), download the file ['inteligencia-20240617T013308Z-001.zip'](https://github.com/Henriquemcc/Trabalho_Pratico_-_Processamento_e_Analise_de_Imagens_-_2024-1/releases/download/0/inteligencia-20240617T013308Z-001.zip) and extract it.

Create a folder called 'inteligencia' in the root of the project and place the files 'svm.pkl' and 'resnet50.h5' inside it.

### Run the program

In the shell (Terminal, Command Prompt or PowerShell) inside the project folder, type:

```
python3 app
```

or

```
python app
```

And a program window will open.

## Group members

[Felipe Costa Amaral](https://github.com/Flipecs)

[Henrique Mendonça Castelar Campos](https://github.com/Henriquemcc)

[Larissa Kaweski Siqueira](https://github.com/larissakaweski)
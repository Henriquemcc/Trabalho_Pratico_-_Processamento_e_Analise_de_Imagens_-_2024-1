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

## Group members

[Felipe Costa Amaral]()

[Henrique Mendonça Castelar Campos]()

[Larissa Kaweski Siqueira]()
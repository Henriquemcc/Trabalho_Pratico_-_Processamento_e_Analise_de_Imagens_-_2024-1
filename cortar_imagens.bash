#!/bin/bash

# Loading virtual environment
source ./venv/bin/activate

# Installing requirements
bash ./instalar_requisitos.bash

# Moving output files to trash
gio trash ./dataset_converted

# Creating logs directory
mkdir -p ./logs

# Loading python script
python3 ./cortar_imagens.py 2>&1 | tee "./logs/cortar_imagens.$(date "+%d-%m-%Y_%H:%M:%S").log"

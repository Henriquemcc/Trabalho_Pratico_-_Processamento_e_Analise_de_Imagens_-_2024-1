#!/bin/bash

# Loading virtual environment
source ./venv/bin/activate

# Installing requirements
bash ./instalar_requisitos.bash

# Creating logs directory
mkdir -p ./logs

# Getting current date
date="$(date "+%d-%m-%Y_%H:%M:%S")"

# Loading python script
python3 ./treinar_ResNet50.py 2>&1 | tee "./logs/treinar_ResNet50.${date}.log"

# Adding timestamp to created files
mv ./modelo.h5 "./logs/modelo.${date}.h5"
mv ./modelo.keras "./logs/modelo.${date}.keras"
mv ./pesos.weights.h5 "./logs/pesos.${date}.weights.h5"
mv ./predicoes.pkl "./logs/predicoes.${date}.pkl"
mv ./data.pkl "./logs/data.${date}.pkl"

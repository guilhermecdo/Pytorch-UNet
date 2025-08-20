#!/bin/bash
now=$(date +"%Y%m%d_%H%M%S")

#constantes para todos os treinamentos
epochs=300
learning_rate=1e-5
classes=20
scale=1
validation=10.0
load="/home/guilherme/Documents/Pytorch-UNet/regression.pth"
#load="/media/guilherme/SSD/unet-data/SEE-Combined-Data/checkpoints/combined_withbase.pth"
#variaveis de cada experimento
#usar um batch de 3 para imagens stacked e sidebyside usar 10 para standart e combined

directory="/media/guilherme/SSD/unet-data/Coverage-SideBySide/"
batch=3

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \
                            #-f=$load
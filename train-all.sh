#!/bin/bash
now=$(date +"%Y%m%d_%H%M%S")

#constantes para todos os treinamentos
epochs=100
learning_rate=1e-4
classes=20
scale=1
validation=10.0
load="/home/guilherme/Documents/Pytorch-UNet/regression.pth"

# Stacked

directory="/media/guilherme/SSD/unet-data/SEE-Stacked-Data/"
batch=3

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \

# Stacked - with base

directory="/media/guilherme/SSD/unet-data/SEE-Stacked-Data-base/"
batch=3

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \
                            -f=$load

# Combined 

directory="/media/guilherme/SSD/unet-data/SEE-Combined-Data/"
batch=10

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \

# Combined - with base

directory="/media/guilherme/SSD/unet-data/SEE-Combined-Data/"
batch=10

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \
                            -f=$load

# SideBySide 

directory="/media/guilherme/SSD/unet-data/SEE-SideBySide-Data-base/"
batch=3

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \

# SideBySide  - with base

directory="/media/guilherme/SSD/unet-data/SEE-SideBySide-Data-base/"
batch=3

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \
                            -f=$load



# Standart Images

directory="/media/guilherme/SSD/unet-data/SEE-Standart-Data/"
batch=10

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \

# Standart Images - with base

directory="/media/guilherme/SSD/unet-data/SEE-Standart-Data/"
batch=10

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \
                            -f=$load

# Coverage + Base + Combined
directory="/media/guilherme/SSD/unet-data/Cocerage-Combined/"
batch=10

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \
                            -f=$load


# Coverage + base + Stack
directory="/media/guilherme/SSD/unet-data/Cocerage-Stacked/"
batch=3

python3 train-regression.py -e=$epochs -b=$batch -l=$learning_rate \
                            --scale=$scale -v=$scale  \
                            --classes=$classes -d=$directory \
                            -f=$load

# Coverage + base + SideBySide
# Coverage + base + Standart
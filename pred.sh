#!/bin/bash
now=$(date +"%Y%m%d_%H%M%S")

model=/media/guilherme/SSD/coverage-mission-1-data/UNET/checkpoints/coverage-mission-1.pth
input=/media/guilherme/SSD/coverage-mission-1-data/UNET/imgs/coverage-1-P900-auv-0-84.png
output=/media/guilherme/SSD/coverage-mission-1-data/UNET/teste.png
#viz=1
no_save=1
mask_threshold=0
scale=1.0
bilinear=1
classes=20

python3 predict.py --model=$model --input=$input --output=$output \
    --viz --mask-threshold=$mask_threshold \
    --scale=$scale --classes=$classes
#!/bin/bash
#SBATCH -n 1
#SBATCH -t 5:00:00
#SBATCH --mem=500G
#SBATCH -o plot_ROC.out

python plot_ROC.py 
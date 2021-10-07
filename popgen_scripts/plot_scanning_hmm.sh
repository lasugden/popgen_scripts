#!/bin/bash
#SBATCH -n 1
#SBATCH -t 5:00:00
#SBATCH --mem=200G
#SBATCH -o plot_scanning_hmm.out

python plot_scanning_hmm.py 
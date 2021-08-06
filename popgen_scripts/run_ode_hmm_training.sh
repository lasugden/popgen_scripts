#!/bin/bash
#SBATCH -n 1
#SBATCH -t 5:00:00
#SBATCH --mem=200G
#SBATCH -o ode_hmm_training.out

python run_ode_hmm_training.py 
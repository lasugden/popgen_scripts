#!/bin/bash
#SBATCH -n 1
#SBATCH -t 100:00:00
#SBATCH --mem=200G
#SBATCH -o make_window_allstats.out

python run_windowstats.py 
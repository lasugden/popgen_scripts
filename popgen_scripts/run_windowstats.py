from popgen_utils.snp_statistics import window_stats

window_stats.run_window_stats(project_name='sweep_hmm',
             model_name='gravel_sweep_400kb_uniform_scoeff',type='sweep', 
             windowsize=2000)

window_stats.run_window_stats(project_name='sweep_hmm',
             model_name='gravel_neutral_400kb',type='neutral', 
             windowsize=2000)


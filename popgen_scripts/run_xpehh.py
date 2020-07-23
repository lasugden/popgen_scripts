from popgen_utils.snp_statistics import selscan
# selscan.run_xpehh(project_name='sweep_hmm',
#              model_name='gravel_sweep_100kb_uniform_scoeff',type='sweep')

# selscan.run_xpehh(project_name='sweep_hmm',
#              model_name='gravel_neutral_100kb',type='neutral')

selscan.run_xpehh(project_name='sweep_hmm',
             model_name='gravel_sweep_400kb_uniform_scoeff',type='sweep')

selscan.run_xpehh(project_name='sweep_hmm',
             model_name='gravel_neutral_400kb',type='neutral')
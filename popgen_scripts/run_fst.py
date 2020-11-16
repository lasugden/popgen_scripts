from popgen_utils.snp_statistics import fst

fst.run_fst(project_name='sweep_hmm',
             model_name='gravel_sweep_400kb_uniform_scoeff',type='sweep')

fst.run_fst(project_name='sweep_hmm',
             model_name='gravel_neutral_400kb',type='neutral')
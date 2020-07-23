from popgen_utils.haplotype_simulation import process_slim_output
# process_slim_output.slim_out_to_selscan(project_name='sweep_hmm',
#              model_name='gravel_sweep_100kb_uniform_scoeff',type='sweep')

# process_slim_output.slim_out_to_selscan(project_name='sweep_hmm',
#              model_name='gravel_neutral_100kb',type='neutral')

process_slim_output.slim_out_to_selscan(project_name='sweep_hmm',
             model_name='gravel_sweep_400kb_uniform_scoeff',type='sweep')

process_slim_output.slim_out_to_selscan(project_name='sweep_hmm',
             model_name='gravel_neutral_400kb',type='neutral')
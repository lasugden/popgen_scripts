from popgen_utils.haplotype_simulation import slim
slim.slim_definition_to_input('gravel_model_100kb',
                        		      selection_coefficient_min=0.02,
                             		      selection_coefficient_max=0.12,
                             		      sweep_population=['p1', 'p2', 'p3'],
                             		      sweep_time=[5,10,15,20],
                             		      project_name='sweep_hmm',
                             		      model_name='gravel_sweep_100kb_uniform_scoeff')


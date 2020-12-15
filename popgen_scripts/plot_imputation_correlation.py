from popgen_utils.performance_analysis import imputation_analysis 

imputation_analysis.read_files_neutral(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
										pop_of_interest='p1', figure_out_path='swifr_testing/p1') 

imputation_analysis.read_files_neutral(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
										pop_of_interest='p2', figure_out_path='swifr_testing/p2') 

imputation_analysis.read_files_neutral(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
										pop_of_interest='p3', figure_out_path='swifr_testing/p3') 

imputation_analysis.read_files_sweep(project_name='sweep_hmm', model_name='gravel_sweep_400kb_uniform_scoeff',
										pop_of_interest='p1', figure_out_path='swifr_testing/p1')

imputation_analysis.read_files_sweep(project_name='sweep_hmm', model_name='gravel_sweep_400kb_uniform_scoeff',
										pop_of_interest='p2', figure_out_path='swifr_testing/p2')

imputation_analysis.read_files_sweep(project_name='sweep_hmm', model_name='gravel_sweep_400kb_uniform_scoeff',
										pop_of_interest='p3', figure_out_path='swifr_testing/p3')
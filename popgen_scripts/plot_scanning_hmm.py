from popgen_utils.performance_analysis import scanning_plots

scanning_plots.make_plots(project_name='sweep_hmm', swifr_out_path='swifr_testing/p1',
	swifr_train_path='gravel_400kb_p1_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p1',
	sim_length=400000, numbins=20, with_hmm=True, hmm_out_path='hmm_testing/p1')

scanning_plots.make_plots(project_name='sweep_hmm', swifr_out_path='swifr_testing/p2',
	swifr_train_path='gravel_400kb_p2_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p2',
	sim_length=400000, numbins=20, with_hmm=True, hmm_out_path='hmm_testing/p2')

scanning_plots.make_plots(project_name='sweep_hmm', swifr_out_path='swifr_testing/p3',
	swifr_train_path='gravel_400kb_p3_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p3',
	sim_length=400000, numbins=20, with_hmm=True, hmm_out_path='hmm_testing/p3')
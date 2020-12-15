from popgen_utils.performance_analysis import ROC_analysis

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p1',
	swifr_train_path='gravel_400kb_p1_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p1',
	mode_neg='neutral', mode_pos='linked')

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p1',
	swifr_train_path='gravel_400kb_p1_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p1',
	mode_neg='neutral', mode_pos='sweep')

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p1',
	swifr_train_path='gravel_400kb_p1_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p1',
	mode_neg='linked', mode_pos='sweep')

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p2',
	swifr_train_path='gravel_400kb_p2_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p2',
	mode_neg='neutral', mode_pos='sweep')

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p2',
	swifr_train_path='gravel_400kb_p2_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p2',
	mode_neg='neutral', mode_pos='linked')

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p2',
	swifr_train_path='gravel_400kb_p2_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p2',
	mode_neg='linked', mode_pos='sweep')

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p3',
	swifr_train_path='gravel_400kb_p3_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p3',
	mode_neg='neutral', mode_pos='sweep')

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p3',
	swifr_train_path='gravel_400kb_p3_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p3',
	mode_neg='neutral', mode_pos='linked')

ROC_analysis.make_ROC_curves(project_name='sweep_hmm', swifr_out_path='swifr_testing/p3',
	swifr_train_path='gravel_400kb_p3_swifr', model_name_neutral='gravel_neutral_400kb',
	model_name_sweep='gravel_sweep_400kb_uniform_scoeff', sweep_pos=200000, pop_of_interest='p3',
	mode_neg='linked', mode_pos='sweep')




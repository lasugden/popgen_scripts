from popgen_utils.misc import run_trained_swifr

run_trained_swifr.run_swifr_on_training_data(project_name='sweep_hmm', model_name='gravel_sweep_400kb_uniform_scoeff',
	type = 'sweep', pop_of_interest='p1', swifr_trained_path='gravel_400kb_p1_swifr', outpath='swifr_testing/p1/',
	pivec=[0.99989, 0.00001, 0.0001])

run_trained_swifr.run_swifr_on_training_data(project_name='sweep_hmm', model_name='gravel_neutral_400kb_uniform_scoeff',
	type = 'sweep', pop_of_interest='p2', swifr_trained_path='gravel_400kb_p2_swifr', outpath='swifr_testing/p2/',
	pivec=[0.99989, 0.00001, 0.0001])

run_trained_swifr.run_swifr_on_training_data(project_name='sweep_hmm', model_name='gravel_sweep_400kb_uniform_scoeff',
	type = 'sweep', pop_of_interest='p3', swifr_trained_path='gravel_400kb_p3_swifr', outpath='swifr_testing/p3/',
	pivec=[0.99989, 0.00001, 0.0001])

run_trained_swifr.run_swifr_on_training_data(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
	type = 'neutral', pop_of_interest='p1', swifr_trained_path='gravel_400kb_p1_swifr', outpath='swifr_testing/p1/',
	pivec=[0.99989, 0.00001, 0.0001])

run_trained_swifr.run_swifr_on_training_data(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
	type = 'neutral', pop_of_interest='p2', swifr_trained_path='gravel_400kb_p2_swifr', outpath='swifr_testing/p2/',
	pivec=[0.99989, 0.00001, 0.0001])

run_trained_swifr.run_swifr_on_training_data(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
	type = 'neutral', pop_of_interest='p3', swifr_trained_path='gravel_400kb_p3_swifr', outpath='swifr_testing/p3/',
	pivec=[0.99989, 0.00001, 0.0001])
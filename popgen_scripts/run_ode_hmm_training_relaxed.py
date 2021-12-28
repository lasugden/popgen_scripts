from popgen_utils.hmm import run_ode_hmm

run_ode_hmm.run_ode_hmm_on_training_data(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
	type='neutral', pop_of_interest='p1', swifr_trained_path='gravel_400kb_p1_swifr', 
	out_path = 'hmm_testing_relaxed/p1/neutral', trans_type='relaxed')

run_ode_hmm.run_ode_hmm_on_training_data(project_name='sweep_hmm', model_name='gravel_sweep_400kb_uniform_scoeff',
	type='sweep', pop_of_interest='p1', swifr_trained_path='gravel_400kb_p1_swifr', 
	out_path = 'hmm_testing_relaxed/p1/sweep', trans_type='relaxed')

run_ode_hmm.run_ode_hmm_on_training_data(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
	type='neutral', pop_of_interest='p2', swifr_trained_path='gravel_400kb_p2_swifr', 
	out_path = 'hmm_testing_relaxed/p2/neutral', trans_type='relaxed')

run_ode_hmm.run_ode_hmm_on_training_data(project_name='sweep_hmm', model_name='gravel_sweep_400kb_uniform_scoeff',
	type='sweep', pop_of_interest='p2', swifr_trained_path='gravel_400kb_p2_swifr', 
	out_path = 'hmm_testing_relaxed/p2/sweep', trans_type='relaxed')

run_ode_hmm.run_ode_hmm_on_training_data(project_name='sweep_hmm', model_name='gravel_neutral_400kb',
	type='neutral', pop_of_interest='p3', swifr_trained_path='gravel_400kb_p3_swifr', 
	out_path = 'hmm_testing_relaxed/p3/neutral', trans_type='relaxed')

run_ode_hmm.run_ode_hmm_on_training_data(project_name='sweep_hmm', model_name='gravel_sweep_400kb_uniform_scoeff',
	type='sweep', pop_of_interest='p3', swifr_trained_path='gravel_400kb_p3_swifr', 
	out_path = 'hmm_testing_relaxed/p3/sweep', trans_type='relaxed')


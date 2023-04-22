"""
Settings for extracting data from dataset
"""

# enter your path to main dataset
data_path = r'/home/tobias/Schreibtisch/Uni/Bachlorarbeit/TrainingSet_5/'
# whether to print infos during process
verbose = True
# specify, which state should be included for each subject
state = ['EC', 'EO']
# whether to normalize with the sklearn.preprocessing.MinMaxScaler
normalize = False
# flatten the data if True (False has no meaningful implementation jet)
flatten = True
# subjects to ignore (leave default, because subjects are missing in the main dataset)
bad_subj = [8, 15, 139, 148, 237, 256, 295, 362, 475, 485, 521, 575, 584, 592, 610, 619, 633, 680, 693, 859, 864, 899,
            944, 969, 974, 1008, 1062, 1154]
# derive the mean over features
mean_features = True

split_epochs = 5

freq_bands = {
    'delta': [0.5, 4],
    'theta': [4, 8],
    'alpha': [8, 14],
    'beta': [14, 30],
    'whole_spec': [0.5, 30]
}

methods = [
    # 'variance',
    # 'std',
    # 'ptp_amp',
    # 'wavelet_coef_energy',
    # 'quantile',
    'pow_freq_bands',
    # 'line_length',
    # 'zero_crossings',
    # 'skewness',
    # 'kurtosis',
    # 'spect_entropy',
    # 'higuchi_fd',
    # 'samp_entropy',
    # 'mean',
    # 'hjorth_complexity',
    # 'hurst_exp',
    # 'hjorth_mobility',
    # 'hjorth_mobility_spect',
    # 'hjorth_complexity_spect',
]

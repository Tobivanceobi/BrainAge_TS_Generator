# BrainAge_TS_Generator
This program helps to extract a training set of the main data set.

## Getting Started

### Prerequisites
After Installing all packages in the requirements.txt file, 
you only have to specify \
the path to the main data set to extract from.

This can be done in the config/config.py file.

### Settings for training set generation

In the `config/config.py` file you can specify the data that should be used to form the data set.\
After that, you only have to run the main.py file.\
The dataset will than be stored in the `output/training_sets` directory.

## Feature Extraction
The Base set `TrainingSet_5` contains following features:
- variance 
- std 
- ptp_amp
- wavelet_coef_energy
- quantile
- pow_freq_bands
- line_length 
- zero_crossings
- skewness
- kurtosis
- spect_entropy
- higuchi_fd
- samp_entropy
- mean
- hjorth_complexity
- hurst_exp
- hjorth_mobility
- hjorth_mobility_spect
- hjorth_complexity_spect

You can add them as a string to the `methods` list in the config.
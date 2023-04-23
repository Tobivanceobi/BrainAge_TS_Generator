import pickle
import numpy as np
import pandas as pd
import config.config as conf
from sklearn.preprocessing import normalize


class Subject:

    def __init__(self, subj_id: int, state):
        self.subject_id = subj_id
        self.state = state
        self.data = {}
        self.data_picks = []
        self.age = self.load_target_age()

    def pick_data(self) -> list:
        """
        Picks the data of the subject out of the main data set specified in the config.
        :return: List of datapoints, or a single datapoint.
        """
        if conf.verbose:
            print(f"Subject {self.subject_id} {self.state}: picking data from raw file data")
        if self.data == {}:
            print("Error during pick_data data: no data was loaded")
            return []

        features = []

        # if a subject should be split into n-datapoints (n=conf.split_epochs)
        if conf.split_epochs:
            features = [[] for i in range(conf.split_epochs)]

        # for all frequency bands in config
        for fb in conf.freq_bands:
            # for all methods in config
            for method in conf.methods:
                # 'pow_freq_bands' should only be used from the 'whole_spec' frequency band.
                if method == 'pow_freq_bands' and fb != 'whole_spec':
                    continue
                # load in the features as values x channels x features (some features can have multiple values)
                data = self.data[fb]['features'][method]
                # if mean over epochs for each value and channel
                if conf.mean_features:
                    for val in data:
                        for chan in val:
                            # if a subject should be split into n-datapoints (n=conf.split_epochs)
                            if conf.split_epochs:
                                # split channel epochs into n bins (n=conf.split_epochs)
                                chan_split = np.array_split(chan, conf.split_epochs)
                                for group in range(0, len(chan_split)):
                                    # add the mean of the bin to the feature bin
                                    features[group].append(np.mean(chan_split[group]))
                            else:
                                # add the mean of all epochs
                                features.append(np.mean(chan))
                else:
                    # if a subject should be split into n-datapoints (n=conf.split_epochs)
                    if conf.split_epochs:
                        for val in data:
                            for chan in val:
                                chan_split = np.array_split(chan, conf.split_epochs)
                                for group in range(0, len(chan_split)):
                                    # add each epoch value to feature bin (no mean)
                                    features[group].append(chan_split[group])
                    else:
                        # add each epoch value to features (no mean)
                        features.append(data)
        self.data_picks = features

        # flatten the data
        if conf.flatten:
            self.data_picks = [np.array(x).flatten() for x in self.data_picks]

        return self.data_picks

    def load_target_age(self) -> float:
        """
        Load the age of the subject from the .csv file in the main data set
        :return: age of the subject as float.
        """
        target_df = pd.read_csv(conf.data_path + 'train_subjects.csv')
        targets = np.array(target_df[['id', 'age']])
        self.age = targets[self.subject_id - 1][1]
        return self.age

    def load_subject_from_file(self) -> dict:
        """
        Loads the subject data from the main data set.
        :return: The Subject data of the main data set.
        """
        if conf.verbose:
            print(f"Subject {self.subject_id} {self.state}: loading data from file")
        try:
            with open(self.get_subject_fname(), "rb") as f:
                self.data = pickle.load(f)
                return self.data
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)

    def get_subject_fname(self) -> str:
        """
        Creates the subjects filename in the main data set.
        :return: Subjects file name in the main data set.
        """
        return conf.data_path + 'subj_' + str(self.subject_id) + '/' + self.state + ".pickle"

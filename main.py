import os
import pickle

import numpy as np

import config.config as conf
from data_loader.subject import Subject
from sklearn.preprocessing import MinMaxScaler


def save_object(obj, fname):
    try:
        with open(fname + ".pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


if __name__ == '__main__':
    training_set = {
        'x': [],
        'y': [],
        'group': []
    }
    for i in range(1, 1201):

        # filter subjects that had bad recordings
        if i in conf.bad_subj:
            continue

        # define x_i in X (X: training data)
        x_i = []

        # iterate states in config
        for state in conf.state:

            # define subject
            subj = Subject(i, state)

            subj.load_subject_from_file()

            # pick data specified in config
            subj.pick_data()
            x_i.append(subj.data_picks)

        if conf.split_epochs:
            for group in range(conf.split_epochs):
                # pick EC and EO data for 'sub subjects'
                training_set['x'].append(np.concatenate([x_i[0][group], x_i[1][group]]))

                # add the subject age to als splits
                training_set['y'].append(subj.age)

                # add the subject ID as group for all splits
                training_set['group'].append(i)
        else:
            # add the subject age to the targets
            training_set['y'].append(subj.age)
            # concatenate EC and EO data and add vector to x
            training_set['x'].append(np.concatenate(x_i))
            # add the subject ID as group
            training_set['group'].append(i)

    if conf.normalize:
        if conf.verbose:
            print('Normalizing training set')
        scaler = MinMaxScaler()
        training_set['x'] = scaler.fit_transform(training_set['x'])

    # create a new dir_name for set to save
    set_id = len([x for x in os.walk('./output/training_sets')]) - 1
    new_set_dir_path = './output/training_sets/' + 'Set_' + str(set_id)

    if not os.path.isdir(new_set_dir_path):
        # create the directory and save the training set
        os.mkdir(new_set_dir_path)
        save_object(training_set, new_set_dir_path + '/training_set')

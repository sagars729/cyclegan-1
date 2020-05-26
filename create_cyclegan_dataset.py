"""Create datasets for training and testing."""
import csv
import os
import random

import click

#import cyclegan_datasets


def create_list(foldername, fulldir=True, suffix=".jpg"):
    """

    :param foldername: The full path of the folder.
    :param fulldir: Whether to return the full path or not.
    :param suffix: Filter by suffix.

    :return: The list of filenames in the folder with given suffix.

    """
    file_list_tmp = os.listdir(foldername)
    file_list = []
    if fulldir:
        for item in file_list_tmp:
            if item.endswith(suffix):
                file_list.append(os.path.join(foldername, item))
    else:
        for item in file_list_tmp:
            if item.endswith(suffix):
                file_list.append(item)
    return file_list

def create_dataset(image_path_a, image_path_b,
                   dataset_name, do_shuffle,
                   DATASET_TO_SIZES, DATASET_TO_IMAGETYPE, PATH_TO_CSV):
    list_a = create_list(image_path_a, True,
                         DATASET_TO_IMAGETYPE[dataset_name])
    list_b = create_list(image_path_b, True,
                         DATASET_TO_IMAGETYPE[dataset_name])

    output_path = PATH_TO_CSV[dataset_name]

    num_rows = DATASET_TO_SIZES[dataset_name]
    all_data_tuples = []
    for i in range(num_rows):
        all_data_tuples.append((
            list_a[i % len(list_a)],
            list_b[i % len(list_b)]
        ))
    if do_shuffle is True:
        random.shuffle(all_data_tuples)
    with open(output_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for data_tuple in enumerate(all_data_tuples):
            csv_writer.writerow(list(data_tuple[1]))


if __name__ == '__main__':
    create_dataset()

"""Contains the standard train/test splits for the cyclegan data."""
"""The size of each dataset. Usually it is the maximum number of images from each domain."""
DATASET_TO_SIZES = {
'facades_train': 401,
'facades_test': 107,
'summer2winter_yosemite_train': 1232,
'summer2winter_yosemite_test': 310,}
DATASET_TO_IMAGETYPE = {
'facades_train': '.jpg',
'facades_test': '.jpg',
'summer2winter_yosemite_train': '.jpg',
'summer2winter_yosemite_test': '.jpg',}
PATH_TO_CSV = {
'facades_train': './input/facades/facades_train.csv',
'facades_test': './input/facades/facades_test.csv',
'summer2winter_yosemite_train': './input/summer2winter_yosemite/summer2winter_yosemite_train.csv',
'summer2winter_yosemite_test': './input/summer2winter_yosemite/summer2winter_yosemite_test.csv',}

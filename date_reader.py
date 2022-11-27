import pandas as pd
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join

input_folder_path = "data/split_data/"

files_in_input = [join(input_folder_path, f) for f in listdir(input_folder_path) if isfile(join(input_folder_path, f))]


df = pd.DataFrame()
for file_path in files_in_input:
    temp_df = pd.read_csv(file_path)
    df = pd.concat([df, temp_df])


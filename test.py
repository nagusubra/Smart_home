import pandas as pd
from datetime import datetime
from datetime import timezone
import os
from os import listdir
from os.path import isfile, join

input_folder_path = "data/split_data/"


files_in_input = [join(input_folder_path, f) for f in listdir(input_folder_path) if isfile(join(input_folder_path, f))]
file_name = []
for file_path in files_in_input:
    file_name = file_path.split("/")
    file_name = file_name[len(file_name)-1]
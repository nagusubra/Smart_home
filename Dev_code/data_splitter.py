import pandas as pd
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join

input_folder_path = "data"
output_folder_path = "data/split_data/"

files_in_input = [join(input_folder_path, f) for f in listdir(input_folder_path) if isfile(join(input_folder_path, f))]


df = pd.DataFrame()
for file_path in files_in_input:
    temp_df = pd.read_csv(file_path)
    df = pd.concat([df, temp_df])

file_naming_number = 0
start_index = 0
range_list = list(range(0, len(df), 50000))
range_list.append(len(df)+1)
for df_index_limit in range_list:
    stop_index = df_index_limit
    temp_df = df.iloc[start_index:stop_index,:]
    file_name = "Home_csv_part_"+str(file_naming_number)+".csv"
    temp_df.to_csv(output_folder_path + file_name, index=False)

    file_naming_number+=1
    start_index = stop_index

import pandas as pd
from datetime import datetime
from datetime import timezone
import os
from os import listdir
from os.path import isfile, join

input_folder_path = "data/split_data/"
output_folder_path = "data/cleaned_data/"

files_in_input = [join(input_folder_path, f) for f in listdir(input_folder_path) if isfile(join(input_folder_path, f))]

def get_raw_data():

    df = pd.DataFrame()
    for file_path in files_in_input:
        temp_df = pd.read_csv(file_path)

        # converting unix time column to UTC
        temp_df["UTC_time"] = temp_df["time"].apply(lambda x: datetime.fromtimestamp(x, tz=timezone.utc))
        temp_df["UTC_time"] = temp_df["UTC_time"] .apply(lambda x: datetime.strftime(x, "%Y-%m-%d %H:%M:%S"))
        temp_df = temp_df.set_index("UTC_time")
        temp_df = temp_df.drop(columns="time")


        temp_df = temp_df.reset_index()
        file_name = file_path.split("/")
        file_name = file_name[len(file_name)-1]
        temp_df.to_csv(output_folder_path + file_name, index=False)
        
        
        temp_df = temp_df.set_index("UTC_time")
        df = pd.concat([df, temp_df])
    return df


df = get_raw_data()
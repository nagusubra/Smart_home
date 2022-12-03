import pandas as pd
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join

input_folder_path = "data/cleaned_data/"
output_folder_path = "data/usable_data/"

def get_data_for_analysis(save):

    # Pool price data transformation
    pool_price_data = "data/HistoricalPoolPriceReportServlet_Alberta.csv"

    pool_price_df = pd.read_csv(pool_price_data)
    pool_price_df = pool_price_df[["Date (HE)","Price ($)"]]
    pool_price_df["Date (HE)"] = pool_price_df["Date (HE)"].apply(lambda x: str(x)[:10] + "-" + str(int(str(x)[10:])-1))
    pool_price_df["Date (HE)"] = pool_price_df["Date (HE)"].apply(lambda x: datetime.strptime(x, "%d/%m/%Y-%H"))
    pool_price_df = pool_price_df.rename(columns = {"Date (HE)": "UTC_time", "Price ($)":"Price ($/MWh)"})



    # raw data transformation
    files_in_input = [join(input_folder_path, f) for f in listdir(input_folder_path) if isfile(join(input_folder_path, f))]

    df = pd.DataFrame()
    for file_path in files_in_input:
        temp_df = pd.read_csv(file_path)
        temp_df = temp_df[['UTC_time','use [kW]', 'gen [kW]', 'House overall [kW]']]
        df = pd.concat([df, temp_df])

    df["UTC_time"] = df["UTC_time"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    df["House overall [kW]"] = df["use [kW]"] - df["gen [kW]"]


    # merging the pool price and the raw data
    whole_df = df.merge(pool_price_df, on="UTC_time", how = "left")
    whole_df["Price ($/MWh)"] = whole_df["Price ($/MWh)"].ffill(axis = 0)
    whole_df = whole_df[['UTC_time','House overall [kW]','Price ($/MWh)','use [kW]', 'gen [kW]']]

    if (save == True):
        file_naming_number = 0
        start_index = 0
        range_list = list(range(0, len(whole_df), 50000))
        range_list.append(len(whole_df)+1)
        for df_index_limit in range_list:
            stop_index = df_index_limit
            temp_df = whole_df.iloc[start_index:stop_index,:]
            file_name = "Home_csv_part_"+str(file_naming_number)+".csv"
            temp_df.to_csv(output_folder_path + file_name, index=False)

            file_naming_number+=1
            start_index = stop_index

    return whole_df



# whole_df = get_data_for_analysis(True)
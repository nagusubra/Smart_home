import pandas as pd
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join

input_folder_path = "data/HistoricalPoolPriceReportServlet_Alberta.csv"
output_folder_path = "data/usable_data/HistoricalPoolPrice_Alberta.csv"


pool_price_df = pd.read_csv(input_folder_path)
pool_price_df = pool_price_df[["Date (HE)","Price ($)"]]
pool_price_df["Date (HE)"] = pool_price_df["Date (HE)"].apply(lambda x: str(x)[:10] + "-" + str(int(str(x)[10:])-1))
pool_price_df["Date (HE)"] = pool_price_df["Date (HE)"].apply(lambda x: datetime.strptime(x, "%d/%m/%Y-%H"))
pool_price_df = pool_price_df.rename(columns = {"Date (HE)": "Datetime", "Price ($)":"Price ($/MWh)"})
pool_price_df.to_csv(output_folder_path, index=False)




input_folder_path = "data/Hourly_Metered_Volumes_and_Pool_Price_and_AIL.csv"
output_folder_path = "data/usable_data/Hourly_Pool_Price_Alberta.csv"


pool_price_df = pd.read_csv(input_folder_path)
pool_price_df = pool_price_df[["Date_Begin_GMT","ACTUAL_POOL_PRICE"]]
#pool_price_df["Date_Begin_GMT"] = pool_price_df["Date_Begin_GMT"].apply(lambda x: str(x)[:1].zfill(2) + "/" + str(x)[3:4].zfill(2) + "/" str(int(str(x)[10:])-1))
pool_price_df["Date_Begin_GMT"] = pool_price_df["Date_Begin_GMT"].apply(lambda x: datetime.strptime(x, "%m/%d/%Y %H:%M"))
pool_price_df = pool_price_df.rename(columns = {"Date_Begin_GMT": "Datetime", "ACTUAL_POOL_PRICE":"Price ($/MWh)"})
pool_price_df.to_csv(output_folder_path, index=False)
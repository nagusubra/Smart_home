import date_reader
import pandas as pd
from datetime import datetime
from datetime import timezone

raw_data = date_reader.get_raw_data()


overal_home = raw_data[['use [kW]', 'gen [kW]', 'House overall [kW]', 'Solar [kW]']]



last_row = raw_data.iloc[len(raw_data)-5:len(raw_data),:]
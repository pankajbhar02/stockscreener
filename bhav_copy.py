#!/usr/bin/env python
# coding: utf-8

# In[6]:
"""
 Holiday list based on Zipline calendar library's holiday calendar
 Reference:    https://github.com/quantopian/trading_calendars/blob/master/trading_calendars/exchange_calendar_xbom.py
"""

holidays_str = [
    '1997-01-23',
    '1997-03-07',
    '1997-03-24',
    '1997-04-08',
    '1997-04-14',
    '1997-04-16',
    '1997-04-18',
    '1997-05-01',
    '1997-05-08',
    '1997-08-15',
    '1997-08-18',
    '1997-08-25',
    '1997-10-02',
    '1997-10-28',
    '1997-10-29',
    '1997-10-31',
    '1997-12-25',
    '1998-04-09',
    '1998-04-14',
    '1998-04-28',
    '1998-12-25',
    '1999-01-01',
    '1999-01-20',
    '1999-01-26',
    '1999-03-02',
    '1999-03-18',
    '1999-03-25',
    '1999-03-29',
    '1999-04-02',
    '1999-04-14',
    '1999-04-27',
    '1999-04-30',
    '1999-09-13',
    '1999-10-19',
    '1999-11-08',
    '1999-11-10',
    '1999-11-23',
    '1999-12-31',
    '2000-01-26',
    '2000-03-17',
    '2000-03-20',
    '2000-04-14',
    '2000-04-21',
    '2000-05-01',
    '2000-08-15',
    '2000-09-01',
    '2000-10-02',
    '2000-12-25',
    '2001-01-01',
    '2001-01-26',
    '2001-03-06',
    '2001-04-05',
    '2001-04-13',
    '2001-05-01',
    '2001-08-15',
    '2001-08-22',
    '2001-10-02',
    '2001-10-26',
    '2001-11-16',
    '2001-11-30',
    '2001-12-17',
    '2001-12-25',
    '2002-03-25',
    '2002-03-29',
    '2002-05-01',
    '2002-08-15',
    '2002-09-10',
    '2002-10-02',
    '2002-10-15',
    '2002-11-06',
    '2002-11-19',
    '2002-12-25',
    '2003-02-13',
    '2003-03-14',
    '2003-03-18',
    '2003-04-14',
    '2003-04-18',
    '2003-05-01',
    '2003-08-15',
    '2003-10-02',
    '2003-11-26',
    '2003-12-25',
    '2004-01-01',
    '2004-01-26',
    '2004-02-02',
    '2004-03-02',
    '2004-04-09',
    '2004-04-14',
    '2004-04-26',
    '2004-10-13',
    '2004-10-22',
    '2004-11-15',
    '2004-11-26',
    '2005-01-21',
    '2005-01-26',
    '2005-03-25',
    '2005-04-14',
    '2005-07-28',
    '2005-08-15',
    '2005-09-07',
    '2005-10-12',
    '2005-11-03',
    '2005-11-04',
    '2005-11-15',
    '2006-01-11',
    '2006-01-26',
    '2006-02-09',
    '2006-03-15',
    '2006-04-06',
    '2006-04-11',
    '2006-04-14',
    '2006-05-01',
    '2006-08-15',
    '2006-10-02',
    '2006-10-24',
    '2006-10-25',
    '2006-12-25',
    '2007-01-01',
    '2007-01-26',
    '2007-01-30',
    '2007-02-16',
    '2007-03-27',
    '2007-04-06',
    '2007-05-01',
    '2007-05-02',
    '2007-08-15',
    '2007-10-02',
    '2007-12-21',
    '2007-12-25',
    '2008-03-06',
    '2008-03-20',
    '2008-03-21',
    '2008-04-14',
    '2008-04-18',
    '2008-05-01',
    '2008-05-19',
    '2008-08-15',
    '2008-09-03',
    '2008-10-02',
    '2008-10-09',
    '2008-10-30',
    '2008-11-13',
    '2008-11-27',
    '2008-12-09',
    '2008-12-25',
    '2009-01-08',
    '2009-01-26',
    '2009-02-23',
    '2009-03-10',
    '2009-03-11',
    '2009-04-03',
    '2009-04-07',
    '2009-04-10',
    '2009-04-14',
    '2009-04-30',
    '2009-05-01',
    '2009-09-21',
    '2009-09-28',
    '2009-10-02',
    '2009-10-13',
    '2009-10-19',
    '2009-11-02',
    '2009-12-25',
    '2009-12-28',
    '2010-01-01',
    '2010-01-26',
    '2010-02-12',
    '2010-03-01',
    '2010-03-24',
    '2010-04-02',
    '2010-04-14',
    '2010-09-10',
    '2010-11-17',
    '2010-12-17',
    '2011-01-26',
    '2011-03-02',
    '2011-04-12',
    '2011-04-14',
    '2011-04-22',
    '2011-08-15',
    '2011-08-31',
    '2011-09-01',
    '2011-10-06',
    '2011-10-27',
    '2011-11-07',
    '2011-11-10',
    '2011-12-06',
    '2012-01-26',
    '2012-02-20',
    '2012-03-08',
    '2012-04-05',
    '2012-04-06',
    '2012-05-01',
    '2012-08-15',
    '2012-08-20',
    '2012-09-19',
    '2012-10-02',
    '2012-10-24',
    '2012-11-14',
    '2012-11-28',
    '2012-12-25',
    '2013-03-27',
    '2013-03-29',
    '2013-04-19',
    '2013-04-24',
    '2013-05-01',
    '2013-08-09',
    '2013-08-15',
    '2013-09-09',
    '2013-10-02',
    '2013-10-16',
    '2013-11-04',
    '2013-11-15',
    '2013-12-25',
    '2014-02-27',
    '2014-03-17',
    '2014-04-08',
    '2014-04-14',
    '2014-04-18',
    '2014-04-24',
    '2014-05-01',
    '2014-07-29',
    '2014-08-15',
    '2014-08-29',
    '2014-10-02',
    '2014-10-03',
    '2014-10-06',
    '2014-10-15',
    '2014-10-24',
    '2014-11-04',
    '2014-11-06',
    '2014-12-25',
    '2015-01-26',
    '2015-02-17',
    '2015-03-06',
    '2015-04-02',
    '2015-04-03',
    '2015-04-14',
    '2015-05-01',
    '2015-09-17',
    '2015-09-25',
    '2015-10-02',
    '2015-10-22',
    '2015-11-12',
    '2015-11-25',
    '2015-12-25',
    '2016-01-26',
    '2016-03-07',
    '2016-03-24',
    '2016-03-25',
    '2016-04-14',
    '2016-04-15',
    '2016-04-19',
    '2016-07-06',
    '2016-08-15',
    '2016-09-05',
    '2016-09-13',
    '2016-10-11',
    '2016-10-12',
    '2016-10-31',
    '2016-11-14',
    '2017-01-26',
    '2017-02-24',
    '2017-03-13',
    '2017-04-04',
    '2017-04-14',
    '2017-05-01',
    '2017-06-26',
    '2017-08-15',
    '2017-08-25',
    '2017-10-02',
    '2017-10-20',
    '2017-12-25',
    '2018-01-26',
    '2018-02-13',
    '2018-03-02',
    '2018-03-29',
    '2018-03-30',
    '2018-05-01',
    '2018-08-15',
    '2018-08-22',
    '2018-09-13',
    '2018-09-20',
    '2018-10-02',
    '2018-10-18',
    '2018-11-08',
    '2018-11-23',
    '2018-12-25',
    '2019-01-26',
    '2019-03-02',
    '2019-03-04',
    '2019-03-21',
    '2019-04-17',
    '2019-04-19',
    '2019-04-29',
    '2019-05-01',
    '2019-06-05',
    '2019-08-12',
    '2019-08-15',
    '2019-09-02',
    '2019-09-10',
    '2019-10-02',
    '2019-10-08',
    '2019-10-21',
    '2019-10-28',
    '2019-11-12',
    '2019-12-25',
    '2020-02-21',
    '2020-03-10',
    '2020-04-02',
    '2020-04-06',
    '2020-04-10',
    '2020-04-14',
    '2020-05-01',
    '2020-05-25',
    '2020-07-31',
    '2020-10-02',
    '2020-11-16',
    '2020-11-30',
    '2020-12-25',
    '2021-01-26',
    '2021-03-11',
    '2021-03-29',
    '2021-04-02',
    '2021-04-14',
    '2021-04-21',
    '2021-05-13',
    '2021-07-21',
    '2021-08-19',
    '2021-09-10',
    '2021-10-15',
    '2021-11-05',
    '2021-11-19',
    '2022-01-26',
    '2022-03-01',
    '2022-03-18',
    '2022-04-14',
    '2022-04-15',
    '2022-05-03',
    '2022-08-09',
    '2022-08-15',
    '2022-08-31',
    '2022-10-05',
    '2022-10-24',
    '2022-10-26',
    '2022-11-08',
    '2023-01-26',
    '2023-02-18',  # weekend
    '2023-03-07',
    '2023-03-30',
    '2023-04-04',
    '2023-04-07',
    '2023-04-14',
    '2023-04-22',  # weekend
    '2023-05-01',
    '2023-06-29',
    '2023-07-29',  # weekend
    '2023-08-15',
    '2023-09-19',
    '2023-10-02',
    '2023-10-24',
    '2023-11-12',  # weekend
    '2023-11-14',
    '2023-11-27',
    '2023-12-25'
]

from datetime import datetime

holidays_date = [
    datetime.strptime(date_str, '%Y-%m-%d').date() for date_str in holidays_str
]

# In[18]:

import pandas as pd
from datetime import datetime, timedelta

# Set the start and end dates
end_date = datetime(2023, 1, 1).date()
start_date = datetime.now().date()

# Get the current datetime
current_datetime = datetime.now()

# Check if the current time is before 20:00 hours
if current_datetime.time() < datetime.strptime('20:00:00', '%H:%M:%S').time():
  # Exclude the current date
  current_date = current_datetime.date()
else:
  current_date = start_date

# Create an empty list to store workday dates
workday_dates = []

# Loop through the dates from start to end, excluding weekends, holidays, and current date (if applicable)
# current_date -= timedelta(days=1)  # Move one day back from the current date
while current_date > end_date:
  if current_date.weekday(
  ) < 5 and current_date not in holidays_date:  # Monday to Friday (0-4) and not a holiday
    workday_dates.append(current_date)
  current_date -= timedelta(days=1)

# Reverse the list to get the dates in ascending order
workday_dates.reverse()

# Create the DataFrame
df_workdates = pd.DataFrame({'Workdate': workday_dates})

# Print the DataFrame
print(df_workdates)

# In[ ]:

import datetime
import os
import pandas as pd
import requests

# Define the base URL
base_url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_"

# Create the folder if it doesn't exist
folder_name = "bhav_copy"
if not os.path.exists(folder_name):
  os.makedirs(folder_name)

# Iterate over the dates in the DataFrame
for index, row in df_workdates.iterrows():
  # Get the date from the DataFrame
  current_date = row["Workdate"]

  # Generate the formatted date
  formatted_date = current_date.strftime("%d%m%Y")

  # Construct the URL
  url = base_url + formatted_date + ".csv"

  # Download the file
  response = requests.get(url)
  file_path = os.path.join(folder_name, formatted_date + ".csv")
  with open(file_path, "wb") as file:
    print(f"Downloading symbol: {formatted_date}")
    file.write(response.content)
    print(f"Data for {formatted_date} downloaded and saved as {file_path}")

# In[ ]:

import os
import pandas as pd


def append_csv_to_dataframe(folder_path):
  dfs = []
  for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
      file_path = os.path.join(folder_path, file_name)
      df = pd.read_csv(file_path)
      # Strip leading and trailing whitespaces from column names
      df.columns = df.columns.str.strip()
      # Filter symbols where SERIES column is 'EQ'
      df = df[df['SERIES'].str.strip() == 'EQ']
      # Convert date column to date format
      df['DATE1'] = pd.to_datetime(df['DATE1'], format=' %d-%b-%Y')
      dfs.append(df)
  appended_df = pd.concat(dfs, ignore_index=True)
  return appended_df


def create_symbol_dataframes(appended_df, output_folder):
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)
  grouped_df = appended_df.groupby("SYMBOL")
  for symbol, group in grouped_df:
    symbol_file_path = os.path.join(output_folder, symbol + ".csv")
    group.set_index("DATE1", inplace=True)
    group.sort_index(ascending=True, inplace=True)
    # Rename columns in symbol-specific DataFrame
    group.rename(columns={
        'DATE1': 'Date',
        'OPEN_PRICE': 'Open',
        'CLOSE_PRICE': 'Close',
        'HIGH_PRICE': 'High',
        'LOW_PRICE': 'Low'
    },
                 inplace=True)
    group.to_csv(symbol_file_path)
    print(f"Saved symbol {symbol} to {symbol_file_path}")


# Specify the folder where the CSV files are located
csv_folder = "bhav_copy"

# Append CSV files into a single DataFrame
appended_df = append_csv_to_dataframe(csv_folder)

# Specify the folder to save the symbol-specific DataFrames
output_folder = "NSE_data"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
  os.makedirs(output_folder)
  print(f"Created folder: {output_folder}")

# Create separate DataFrames based on the SYMBOL and save them
create_symbol_dataframes(appended_df, output_folder)

# In[ ]:

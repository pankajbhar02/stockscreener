#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
import os
import sys
import numpy as np


def ABC(folder_path):

  # Create the 'ABC' folder if it doesn't exist
  ma_folder = os.path.join('ABC')
  if not os.path.exists(ma_folder):
    os.makedirs(ma_folder)

# Download the Nifty 500 list
  nifty500_df = pd.read_csv(
      "https://archives.nseindia.com/content/indices/ind_nifty50list.csv")
  symbols = nifty500_df['Symbol'].tolist()

  # Iterate over files in the folder
  for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if file_name.endswith(".csv") and file_name.split(".csv")[0] in symbols:
      # Read the CSV file and create a DataFrame
      df = pd.read_csv(file_path)
      # Check if the DataFrame has at least one row of data
      if len(df) > 0:
        # Compute the 50-day moving average
        df['50SMA'] = df['Close'].rolling(window=50).mean()

        # Create the "is_rising" column and set initial value as 'N'
        df['is_rising'] = 'N'

        # Loop through the DataFrame and check if the 50-day SMA is rising
        for i in range(1, len(df)):
          if df['50SMA'].iloc[i] > df['50SMA'].iloc[i - 1]:
            df.at[df.index[i], 'is_rising'] = 'Y'

        # Create the "is_rising_10d" column and set initial value as empty string
        df['is_rising_10d'] = ''

        # Loop through the DataFrame and check for consecutive 10 "Y" values
        for i in range(10, len(df)):
          if all(df['is_rising'].iloc[i - 10:i + 1] == 'Y'):
            df.at[df.index[i], 'is_rising_10d'] = 'rising'

        # Create the "is_Bullish" column and set initial value as 'N'
        df['is_Bullish'] = 'N'

        # Loop through the DataFrame and check if the close price is greater than the open price
        for i in range(len(df)):
          if df['Close'].iloc[i] > df['Open'].iloc[i]:
            df.at[df.index[i], 'is_Bullish'] = 'Y'

        # Create the "is_hammer" column and set initial value as 'N'
        df['is_hammer'] = 'N'

        # Loop through the DataFrame and check for the hammer pattern conditions
        for i in range(len(df)):
          open_ = df['Open'].iloc[i]
          close = df['Close'].iloc[i]
          low = df['Low'].iloc[i]
          if (df['is_rising_10d'].iloc[i] == 'rising'
              and df['is_Bullish'].iloc[i] == 'N' and (open_ - close) != 0
              and (close - low) / (open_ - close) >= 2):
            df.at[df.index[i], 'is_hammer'] = 'Y'

        # Create the "50_support" column and set initial value as 'N'
        df['50_support'] = 'N'

        # Loop through the DataFrame and check for the 50_support conditions
        for i in range(len(df)):
          sma = df['50SMA'].iloc[i]
          close = df['Close'].iloc[i]
          open_ = df['Open'].iloc[i]
          high = df['High'].iloc[i]
          low = df['Low'].iloc[i]

          if (abs((sma - close) / sma) <= 0.01 or abs(
              (sma - open_) / sma) <= 0.01 or abs((sma - high) / sma) <= 0.01
              or abs((sma - low) / sma) <= 0.01 or (high > sma > low)):
            df.at[df.index[i], '50_support'] = 'Y'

        # Compute the 20-day moving average
        df['20SMA'] = df['Close'].rolling(window=20).mean()

        # Compute the 20-day standard deviation
        df['20STD'] = df['Close'].rolling(window=20).std()

        # Compute the lower Bollinger Band (LBB)
        df['LBB'] = df['20SMA'] - 2 * df['20STD']

        # Create the "LBB_support" column and set initial value as 'N'
        df['LBB_support'] = 'N'

        # Loop through the DataFrame and check for the 50_support conditions
        for i in range(len(df)):
          BB = df['LBB'].iloc[i]
          close = df['Close'].iloc[i]
          open_ = df['Open'].iloc[i]
          high = df['High'].iloc[i]
          low = df['Low'].iloc[i]

          if (abs((BB - close) / BB) <= 0.01 or abs((BB - open_) / BB) <= 0.01
              or abs((BB - high) / BB) <= 0.01 or abs(
                  (BB - low) / BB) <= 0.01 or (high > BB > low)):
            df.at[df.index[i], 'LBB_support'] = 'Y'

        # Create the "decision" column and set initial value as blank
        df['decision'] = ''

        # Define the conditions for the "BUY" decision
        conditions = ((df['is_rising_10d'] == 'rising') &
                      (df['50_support'] == 'Y') & ((df['is_Bullish'] == 'Y') |
                                                   (df['is_hammer'] == 'Y')) &
                      (df['LBB_support'] == 'Y'))

        # Update the "decision" column with "BUY" where the conditions are met
        df.loc[conditions, 'decision'] = 'BUY'

        # Save the DataFrame as a CSV file, overwriting if it already exists
        ma_file_path = os.path.join(ma_folder, file_name)
        df.to_csv(ma_file_path, index=False)

        # Print a message to confirm the file download
        print(f"Data for {file_name} processed and saved as {ma_file_path}")
      else:
        print(f"No data available for {file_name}")

if __name__ == "__main__":
  folder_path = "NSE_data"
  # Get the folder path from the command line arguments
  #     if len(sys.argv) < 2:
  #         print("Please provide the folder path as a command line argument.")
  #         sys.exit(1)

  #     folder_path = sys.argv[1]
  if not os.path.exists(folder_path):
    print("The specified folder path does not exist.")
#         sys.exit(1)

  ABC(folder_path)

# In[ ]:

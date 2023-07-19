#!/usr/bin/env python
# coding: utf-8

# In[3]:

import os
import pandas as pd


def import_symbol_data(folder_path):
  symbol_data = {}

  csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

  for csv_file in csv_files:
    symbol = os.path.splitext(csv_file)[0]
    csv_path = os.path.join(folder_path, csv_file)
    df_symbol = pd.read_csv(csv_path)
    symbol_data[symbol] = df_symbol

  return symbol_data


def find_buy_opportunities(folder_path):
  symbol_data = import_symbol_data(folder_path)

  df_opportunities = pd.DataFrame()

  for symbol, df_symbol in symbol_data.items():
    if not df_symbol.empty:
      last_row = df_symbol.iloc[-1].copy()
      if last_row["decision"] == "BUY":
        last_row["Symbol"] = symbol
        last_row["Prev Low"] = df_symbol.iloc[-2]["Low"]
        df_opportunities = pd.concat(
            [df_opportunities, last_row.to_frame().T], ignore_index=True)

  return df_opportunities


def modify_df_opportunities(df_opportunities):
  df_opportunities.rename(columns={"DATE1": "Date"}, inplace=True)
  df_opportunities = df_opportunities[[
      "Date", "Symbol", "decision", "High", "Low", "Prev Low"
  ]]
  df_opportunities = df_opportunities.copy()
  df_opportunities["Entry Price"] = (df_opportunities["High"] *
                                     1.001).apply(lambda x: round(x, 2))
  df_opportunities["Stop Loss"] = df_opportunities[["Low",
                                                    "Prev Low"]].min(axis=1)
  df_opportunities["Target"] = df_opportunities["Entry Price"] + 2 * (
      df_opportunities["Entry Price"] - df_opportunities["Stop Loss"])
  df_opportunities["Qty"] = (
      1000 / (df_opportunities["Entry Price"] -
              df_opportunities["Stop Loss"])).apply(lambda x: round(x, 0))
  df_opportunities[
      "Capital"] = df_opportunities["Qty"] * df_opportunities["Entry Price"]

  return df_opportunities


if __name__ == "__main__":
  folder_path = "ABC"

  # Find buy opportunities
  df_opportunities = find_buy_opportunities(folder_path)

  # Modify the opportunities DataFrame
  df_opportunities = modify_df_opportunities(df_opportunities)

  # Get the current date
  current_date = pd.Timestamp.now().strftime("%Y%m%d")

  # Define the output file path
  output_file = os.path.join("Output/", f"ABC_{current_date}.xlsx")

  # Save the DataFrame as a CSV file
  df_opportunities.to_excel(output_file, index=False)

  print(f"Output saved to {output_file}")

# In[ ]:

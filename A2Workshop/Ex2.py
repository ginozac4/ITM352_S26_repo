# Read in a file from a URL and save a local CSV file with the first 10 rows.
#

# Name: Cassiddy Ginoza
# Date: Mar. 31, 2026

import time
import pandas as pd
import numpy as np
import pyarrow

pd.set_option('display.max_columns', None)  # Show all columns in the output, for small datasets


def load_csv(filepath):
    print(f"Loading data from {filepath}...")
    start_time = time.time()
    try:     # if try fails, it will return exception
        df = pd.read_csv(filepath, engine='pyarrow')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {df.columns.tolist()}") # convert to list for better readability
        df['order_date'] = pd.to_datetime(df['order_date'], format='%m-%d-%Y', errors='coerce') #convert order_date to datetime, coercing errors to NaT
#        df.fillna(0, inplace=True) # fill NaN values with 0 for numeric columns
        df['sales'] = df['quantity'] * df['unit_price'] # calculate sales as quantity multiplied by unit price

        required_columns = ['quantity', 'unit_price', 'order_date']
        # check if required columns are present
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing columns in the CSV file: {missing_columns}")
        else:
            print("All required columns are present.")

        return df
    
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# call load_csv to load the data and print the first 10 rows
filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
# filename = "sales_data_test.csv"
sales_data = load_csv(filename)

print(sales_data.head(10))
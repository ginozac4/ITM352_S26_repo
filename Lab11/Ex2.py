# Name: Cassiddy Ginoza
# Date: Mar. 31, 2026

import pandas as pd
import numpy as np
import pyarrow

filename = "sales_data.csv"

pd.set_option('display.max_columns', None)  # Show all columns in the output

df = pd.read_csv(filename, engine='pyarrow')
df['order_date'] = pd.to_datetime(df['order_date'], format='%m-%d-%Y', errors='coerce')

#coerce quantity and unit_price to numeric, setting errors to NaN
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales'] = df['quantity'] * df['unit_price']

pivot_table = df.pivot_table(values='sales',
                             index='sales_region',
                             columns='order_type',
                             aggfunc='sum',
                             margins=True,
                             margins_name='Total Sales')

print(pivot_table)
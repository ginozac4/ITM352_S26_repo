# Name: Cassiddy Ginoza
# Date: Apr. 7, 2026

# grab 1 month interest rate data from the Treasury website

import ssl
import pandas as pd
import urllib.request
import lxml

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"

ssl._create_default_https_context = ssl._create_unverified_context

print("Opening URL: ", url)
web_page = urllib.request.urlopen(url)
data_frame = pd.read_html(web_page)

# print(data_frame[0].info())
# print(data_frame[0])

print("Column names in the DataFrame: ")
print(data_frame[0].columns)

# extract the 1 month interest rate data
one_month_rate = data_frame[0].loc[0, "1 Mo"]
print(f"1 month interest rate on 2026-03-07: {one_month_rate}")

'''# iterate through the data using iterrows() to find the 1 month interest rate for each date
for index, row in data_frame[0].iterrows():
    if row["Date"] == "2026-03-07":
        one_month_rate = row["1 Mo"]
        print(f"1 month interest rate on 2026-03-07: {one_month_rate}")
        break'''
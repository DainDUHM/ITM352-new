import pandas as pd

# Enable display of all columns
pd.set_option('display.max_columns', None)

# URL for the sales data CSV file
url = "C:\Users\User\Documents\GitHub\ITM352_Fall24_repo\sales_data.csv"


try:
 
    df = pd.read_csv(url, engine='pyarrow', on_bad_lines='skip')

    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    print("First 5 rows of the sales data:")
    print(df.head())

except Exception as e:
    print(f"An error occurred: {e}")




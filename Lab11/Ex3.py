import pandas as pd
import numpy as np

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', "${:,.2f}".format)


try:
    
    df = pd.read_csv(url, engine='pyarrow', on_bad_lines='skip')

   
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')

    
    df['sales'] = df['quantity'] * df['unit_price']

    
    df['sales'].fillna(0, inplace=True)

    print("First 5 rows after calculating sales:")
    print(df.head())

    pivot_table = pd.pivot_table(df, values='sales', 
                                 index='region', 
                                 columns='order_type', 
                                 aggfunc=[np.sum, np.mean],  
                                 margins=True, margins_name='Total')

 
    print("\nPivot table with total and average sales by region and order_type:")
    print(pivot_table)

except Exception as e:
    print(f"An error occurred: {e}")

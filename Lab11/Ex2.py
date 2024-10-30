import pandas as pd
import numpy as np


url = "C:\Users\User\Documents\GitHub\ITM352_Fall24_repo\sales_data.csv"


pd.set_option('display.max_columns', None)


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
                                 aggfunc=np.sum, 
                                 margins=True, margins_name='Total')

 
    print("\nPivot table aggregating sales by region and order_type:")
    print(pivot_table)

except Exception as e:
    print(f"An error occurred: {e}")

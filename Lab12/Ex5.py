#Get a JSOn file of data using a sequel like query, select data about driver types and group.

import requests
import pandas as pd

#Create a REST query tjat returns the account of licenses by driver type

search_results = requests.get("https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type").json()

#Convert search results to Data Frame 

results_df = pd.DataFrame.from_records(search_results)

#print(results_df.head())


results_df.columns = ["count", "driver_type"]
results_df = results_df.set_index("driver_type")

#Print results
print(results_df)


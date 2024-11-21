#Create a scatter plot of fares and distances

import matplotlib.pyplot as plt
import pandas as pd

trips_df = pd.read_json("../Trips from area 8.json")

trip_miles_gt_0 = trips_df[['trip_miles', 'fare']].query('trip_miles > 0')
fare_series = trip_miles_gt_0.fare 
trip_miles = trip_miles_gt_0.trip_miles

plt.plot(fare_series, trip_miles,)
import numpy as np

import pandas as pd


percentile_income_data = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]


percentile_income_array = np.array(percentile_income_data)


array_shape = percentile_income_array.shape
num_elements = percentile_income_array.size


print(f"Array Shape: {array_shape}")
print(f"Number of Elements: {num_elements}\n")


df = pd.DataFrame(percentile_income_data, columns=["Percentile", "Income"])
print("Percentile and Household Income Table:")
print(df)




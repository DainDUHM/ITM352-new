import pandas as pd


ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]


age_gender_list = list(zip(ages, gender))


df = pd.DataFrame(age_gender_list, index=names, columns=["Age", "Gender"])


print("DataFrame:")
print(df)

print("\nSummary of the DataFrame:")
print(df.describe())


average_age_by_gender = df.groupby("Gender")["Age"].mean()
print("\nAverage Age by Gender:")
print(average_age_by_gender)

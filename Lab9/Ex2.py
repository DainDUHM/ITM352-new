import csv

file_path = 'survey_1000.csv'

realinc_values = []


with open(file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader) 

    for row in csv_reader:
        try:
            
            realinc_value = float(row[5456])
            if realinc_value > 0:
                realinc_values.append(realinc_value)
        except (IndexError, ValueError):
            
            continue

if realinc_values:
    total = sum(realinc_values)
    count = len(realinc_values)
    average = total / count
    maximum = max(realinc_values)
    minimum = min(realinc_values)

    print(f"Number of REALINC values greater than 0: {count}")
    print(f"Average REALINC value: {average:.2f}")
    print(f"Maximum REALINC value: {maximum:.2f}")
    print(f"Minimum REALINC value: {minimum:.2f}")
else:
    print("No REALINC values greater than 0 were found.")
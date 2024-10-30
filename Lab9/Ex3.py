import csv

file_path = 'taxi_1000.csv'

fare_total = 0
fare_count = 0
max_trip_distance = 0


with open(file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  

    for row in csv_reader:
        try:
            
            fare = float(row[4])
            trip_miles = float(row[5])
            
           
            fare_total += fare
            fare_count += 1
            
            
            if trip_miles > max_trip_distance:
                max_trip_distance = trip_miles
        except (IndexError, ValueError):
            
            continue


if fare_count > 0:
    average_fare = fare_total / fare_count
    
    print(f"Total of all fares: ${fare_total:.2f}")
    print(f"Average fare: ${average_fare:.2f}")
    print(f"Maximum trip distance: {max_trip_distance:.2f} miles")
else:
    print("No fare data found.")
trip_miles = [1.1, 0.8, 2.5, 2.6]

trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

trips = { 

"miles": trip_miles,

 "fares": trip_fares } 

print(trips)

print(f"3rd Trip - Duration: {trips['miles'][2]} miles, Cost: {trips['fares'][2]}")
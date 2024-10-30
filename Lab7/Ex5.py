# Function to determine if the fare is high or low
def check_fare(fares):
    for fare in fares:
        if fare > 12:
            print(f"This fare {fare} is high!")
        else:
            print(f"This fare {fare} is low")

# Test cases
def test_check_fare():
    print("Test Case 1: Sample fares")
    check_fare([8.60, 5.75, 13.25, 21.21])  # Expected output: low, low, high, high

    print("\nTest Case 2: All low fares")
    check_fare([5.00, 6.75, 11.99])  # Expected output: low for all

    print("\nTest Case 3: All high fares")
    check_fare([13.50, 20.00, 15.75])  # Expected output: high for all

    print("\nTest Case 4: Mixed fares")
    check_fare([10.50, 12.00, 12.01])  # Expected output: low, low, high

test_check_fare()

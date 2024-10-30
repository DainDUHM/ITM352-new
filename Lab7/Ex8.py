for num in range(1, 11):
    if num == 5:
        continue  # Skip printing the number if it's 5
    if num == 8:
        print("Loop stopped at 8!")
        break  # Stop the loop if the number is 8
    print(num)

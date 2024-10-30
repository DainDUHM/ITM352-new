def determine_movie_price(age, is_tuesday, is_matinee):

    normal_price = 14

    senior_price = 8 if age >= 65 else normal_price

    tuesday_price = 10

    matinee_price = 5 if age >= 65 else 8

    if is_matinee:

        return matinee_price

    elif is_tuesday:

        return tuesday_price

    else:

        return senior_price

age = int(input("Enter your age: "))

is_tuesday = input("Is it Tuesday? (yes/no): ").lower() == "yes"

is_matinee = input("Is it a matinee? (yes/no): ").lower() == "yes"

price = determine_movie_price(age, is_tuesday, is_matinee)

print(f"Age: {age}")

print(f"Is it Tuesday? {is_tuesday}")

print(f"Is it a matinee? {is_matinee}")

print(f"Movie price: ${price}")
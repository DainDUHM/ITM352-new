import pandas as pd
import ssl
import time
import sys

ssl._create_default_https_context = ssl._create_unverified_context

# Set display to show all columns
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# Import the data file
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

# Function to load CSV file
def load_csv(file_path):
    try:
        print(f"Reading CSV file: {file_path}")
        start_time = time.time()
        sales_data = pd.read_csv(file_path, dtype_backend='pyarrow', on_bad_lines="skip")
        load_time = time.time() - start_time
        print(f"File loaded in {load_time:.2f} seconds")
        print(f"Number of rows: {len(sales_data)}")

        required_columns = ['quantity', 'order_date', 'unit_price']
        missing_columns = [col for col in required_columns if col not in sales_data.columns]

        if missing_columns:
            print(f"\nWarning: The following required columns are missing: {missing_columns}")
        else:
            print("\nAll required columns are present")

        sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format="mixed")
        sales_data.head(10).to_csv('sales_data_test.csv')

        return sales_data
    except FileNotFoundError:
        print(f"Error: the file {file_path} was not found.")
    except pd.errors.EmptyDataError as e:
        print(f"Error: the file {file_path} was empty.")
    except pd.errors.ParserError as e:
        print(f"Error: the file {file_path} had a problem parsing.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

# Function to display user-selected number of rows
def display_rows(data):
    while True:
        num_rows = len(data)
        print("\nEnter number of rows to display:")
        print(f"- Enter a number between 1 and {num_rows}")
        print("- To see all rows enter 'all'")
        print("- To skip, press Enter")
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == '':
            print("Skipping preview")
            break
        elif user_choice == 'all':
            print(data)
            break
        elif user_choice.isdigit() and 1 <= int(user_choice) <= num_rows:
            print(data.head(int(user_choice)))
            break
        else:
            print("Invalid input. Please re-enter")

# Cleanly exit the program
def exit_program(data):
    sys.exit(0)

# Function to print number of unique employees per region
def employees_by_region(data):
    pivot_table = pd.pivot_table(data, index="sales_region", values="employee_id", aggfunc=pd.Series.nunique)
    print("\nNumber of Employees by Region")
    pivot_table.columns = ['Number of Employees']
    print(pivot_table)
    return pivot_table

# Function to generate custom pivot table
def generate_custom_pivot_table(data):
    print("\nGenerating Custom Pivot Table")
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "Select rows:")
    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns (optional):")
    value_options = list(data.select_dtypes(include=['number']).columns)
    values = get_user_selection(value_options, "Select values:")
    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "Select aggregation function:")[0]

    pivot_table = pd.pivot_table(
        data,
        index=rows,
        columns=cols if cols else None,
        values=values,
        aggfunc=agg_func
    )
    print("\nCustom Pivot Table:")
    print(pivot_table)

# Helper function to get user selection
def get_user_selection(options, prompt):
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = input("Enter the number(s) of your choice(s), separated by commas: ")
    selected = [options[int(i) - 1] for i in choice.split(',')] if choice else []
    return selected

# Display the menu of user options
def display_menu(data):
    menu_options = (
        ("Show the first n rows of sales data", display_rows),
        ("Show the number of employees by region", employees_by_region),
        ("Generate a custom pivot table", generate_custom_pivot_table),
        ("Exit the program", exit_program)
    )

    while True:
        print("\nPlease choose from among these options:")
        for index, (description, _) in enumerate(menu_options):
            print(f"{index + 1}: {description}")

        num_choices = len(menu_options)
        try:
            choice = int(input(f"Select an option between 1 and {num_choices}: "))
            if 1 <= choice <= num_choices:
                action = menu_options[choice - 1][1]
                action(data)
            else:
                print("Invalid input. Please re-enter.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Load the CSV data
sales_data = load_csv(url)

# Main loop for user interaction
def main():
    if sales_data is not None:
        display_menu(sales_data)
    else:
        print(f"Failed to load the CSV file {url}")

if __name__ == "__main__":
    main()

import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_descriptipn
import matplotlib.pyplot as plt

# CSV class to handle operations related to the finance CSV file
class CSV:
    CSV_FILE = "finance_data.csv"  # Path to the CSV file
    COLUMNS = ["date", "amount", "category", "description"]  # Column names for the CSV file
    FORMAT = "%d-%m-%Y"  # Date format used in the CSV file

    @classmethod
    def initialize_csv(cls):
        """
        Initializes the CSV file with the defined columns if it does not exist.
        """
        try:
            pd.read_csv(cls.CSV_FILE)  # Try to read the CSV file
        except FileNotFoundError:
            # Create a new DataFrame with the specified columns if file not found
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)  # Save the empty DataFrame as a new CSV file

    @classmethod
    def add_entry(cls, date, amount, category, description):
        """
        Adds a new entry to the CSV file.
        """
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)  # Write the new entry to the CSV file
        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        """
        Retrieves transactions from the CSV file within a specified date range.
        """
        df = pd.read_csv(cls.CSV_FILE)  # Read the CSV file into a DataFrame
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)  # Convert 'date' column to datetime
        start_date = datetime.strptime(start_date, CSV.FORMAT)  # Convert start_date to datetime
        end_date = datetime.strptime(end_date, CSV.FORMAT)  # Convert end_date to datetime

        # Filter the DataFrame for transactions within the specified date range
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range.")
        else:
            # Print the transactions and summary if transactions are found
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )

            # Calculate total income and expenses
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ₹{total_income:.2f}")
            print(f"Total Expense: ₹{total_expense:.2f}")
            print(f"Net Savings: ₹{(total_income - total_expense):.2f}")

        return filtered_df

# Function to handle adding a new transaction
def add():
    CSV.initialize_csv()  # Initialize the CSV file if it does not exist
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
        allow_default=True,
    )  # Get the date of the transaction
    amount = get_amount()  # Get the amount of the transaction
    category = get_category()  # Get the category of the transaction
    description = get_descriptipn()  # Get the description of the transaction
    CSV.add_entry(date, amount, category, description)  # Add the new transaction to the CSV file

# Function to plot transactions over time
def plot_transactions(df):
    df.set_index("date", inplace=True)  # Set 'date' column as the index for plotting
    income_df = (
        df[df["category"] == "Income"]
        .resample("D")  # Resample data by day
        .sum()  # Sum up amounts for each day
        .reindex(df.index, fill_value=0)  # Reindex to ensure all dates are included
    )
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    plt.figure(figsize=(10, 5))  # Set figure size for the plot
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")  # Plot income
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")  # Plot expenses
    plt.xlabel("Date")  # Label for x-axis
    plt.ylabel("Amount")  # Label for y-axis
    plt.title("Income and Expenses Over Time")  # Title of the plot
    plt.legend()  # Show legend
    plt.grid(True)  # Show grid
    plt.show()  # Display the plot

# Main function to handle user input and perform actions based on user choices
def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add()  # Call the function to add a new transaction
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")  # Get start date for transaction range
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")  # Get end date for transaction range
            df = CSV.get_transactions(start_date, end_date)  # Retrieve transactions for the date range
            if input("Do you want to see a plot? (y/n): ").lower() == "y":
                plot_transactions(df)  # Plot transactions if user agrees
        elif choice == "3":
            print("Exiting...")  # Exit the program
            break
        else:
            print("Invalid choice, enter 1, 2, or 3.")  # Handle invalid input

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to start the program

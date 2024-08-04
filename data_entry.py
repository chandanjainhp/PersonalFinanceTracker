from datetime import datetime

date_format = "%d-%m-%Y"  # Define the date format used throughout the application
CATEGORIES = {"I": "Income", "E": "Expense"}  # Map single-letter category codes to full names

def get_date(prompt, allow_default=False):
    """
    Prompts the user to input a date and returns it in the specified format.
    If `allow_default` is True and the user does not provide a date, the function returns today's date.
    """
    date_str = input(prompt)  # Get input from the user
    if allow_default and not date_str:  # Check if a default value is allowed and if input is empty
        return datetime.today().strftime(date_format)  # Return today's date if no input is provided

    try:
        # Attempt to parse the provided date string
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)  # Return the date in the specified format
    except ValueError:
        # Handle invalid date format
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)  # Prompt the user again

def get_amount():
    """
    Prompts the user to input an amount and returns it as a float.
    Ensures that the amount is a positive non-zero value.
    """
    try:
        amount = float(input("Enter the amount: "))  # Convert the user input to a float
        if amount <= 0:
            raise ValueError("Amount must be a non-negative, non-zero value.")
        return amount
    except ValueError as e:
        # Handle invalid input or negative values
        print(e)
        return get_amount()  # Prompt the user again

def get_category():
    """
    Prompts the user to input a category code and returns the full category name.
    Ensures the input is either 'I' for Income or 'E' for Expense.
    """
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()  # Get input and convert to uppercase
    if category in CATEGORIES:
        return CATEGORIES[category]  # Return the full category name based on the input code

    # Handle invalid category input
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()  # Prompt the user again

def get_descriptipn():
    """
    Prompts the user to input a description for the transaction.
    Returns the description as a string (optional field).
    """
    return input("Enter a description (optional): ")  # Return user input as description

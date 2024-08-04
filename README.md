

# 💰 Personal Finance Manager

This Python script helps you manage your personal finances by tracking income and expenses. It allows you to add transactions, view summaries within date ranges, and visualize your financial data.

## ✨ Features

- 📝 Add new transactions with date, amount, category, and description
- 📊 View transactions and summaries within a specified date range
- 📈 Visualize income and expenses over time with a plot
- 💾 Data persistence using CSV file storage

## 🛠️ Requirements

- Python 3.x
- pandas
- matplotlib

## 🚀 Installation

1. Clone this repository or download the script files.
2. Install the required packages:


pip install pandas matplotlib


## 🖥️ Usage

Run the script:

python main.py


The main menu offers three options:

1. ➕ Add a new transaction
2. 👀 View transactions and summary within a date range
3. 🚪 Exit

### 💸 Adding a Transaction

- 📅 Enter the date (format: dd-mm-yyyy) or press Enter for today's date
- 💲 Enter the amount
- 🏷️ Choose the category (Income or Expense)
- 📝 Provide a description for the transaction

### 📊 Viewing Transactions and Summary

- 📅 Enter start and end dates to define the range
- 📜 View a list of transactions, total income, total expenses, and net savings
- 📈 Option to display a plot of income and expenses over time

## 📁 File Structure

- `main.py`: The main script containing the CSV class and core functionality
- `data_entry.py`: Helper functions for user input (not provided in the given code snippet)
- `finance_data.csv`: CSV file storing the transaction data

## 🔧 Customization

You can modify the `CSV_FILE` and `COLUMNS` class variables in the `CSV` class to change the file name or structure of the CSV file.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

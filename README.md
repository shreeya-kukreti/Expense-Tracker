A lightweight, Python-based Command Line Interface (CLI) application to track your daily spending. This tool allows you to log expenses, categorize them, and generate monthly financial reports directly from your terminal.

Features
Log Expenses: Save the date, category, amount, and a brief description.
Persistent Storage: All data is saved to a local expenses.csv file, so your data persists even after closing the program.
Category Summaries: Automatically calculate total spending per category (e.g., Food, Travel, Study).
Monthly Reports: Filter and view total spending for a specific month (YYYY-MM).
Manage Records: View all recorded entries or delete specific expenses to keep your records clean.

Getting Started
Prerequisites
Python 3.x installed on your machine.

Installation
Clone the repository:
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

Run the application:
python expense_tracker.py

Usage
Once the program is running, you will see a menu with the following options:
Add Expense: Enter the category, amount, and description. The date is captured automatically.
View All Expenses: Displays a numbered list of every entry in your CSV file.
Category-wise Summary: Shows a breakdown of total spending for each unique category.
Monthly Report: Enter a month (e.g., 2023-10) to see all matching entries and the total sum for that period.
Delete Expense: Choose a specific entry number to remove it from the records.
Exit: Safely close the application.

Data Storage
The application stores data in a file named expenses.csv in the same directory. The structure of the file is: Date, Category, Amount, Description.

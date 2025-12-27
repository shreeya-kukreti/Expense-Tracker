import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Travel/Study/etc): ").strip()
    amount = float(input("Enter amount: "))
    description = input("Enter description: ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


def view_expenses():
    print("\nAll Expenses:")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for i, row in enumerate(reader, start=1):
            print(f"{i}. {row}")


def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            summary[category] = summary.get(category, 0) + amount

    print("\nCategory-wise Summary:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")


def monthly_report():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    print("\nMonthly Expenses:")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0].startswith(month):
                print(row)
                total += float(row[2])

    print(f"\nTotal spent in {month}: ₹{total}")


def delete_expense():
    expenses = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        expenses = list(reader)

    for i, row in enumerate(expenses, start=1):
        print(f"{i}. {row}")

    choice = int(input("Enter expense number to delete: ")) - 1

    if 0 <= choice < len(expenses):
        expenses.pop(choice)
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(expenses)
        print("Expense deleted successfully!")
    else:
        print("Invalid selection!")


def menu():
    initialize_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Monthly Report")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_report()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Try again.")


menu()
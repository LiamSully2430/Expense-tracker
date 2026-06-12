
from expenses import Expense
import datetime
import calendar

def main():

    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for expense
    expense = get_user_expense()

    # Write expense to file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses
    summarize_expense(expense_file_path,budget)

def get_user_expense():

    expense_name = input('Enter expense name: ')

    expense_amount = float(input('Enter expense amount: '))

    print(f"You've entered {expense_name}, {expense_amount}")
    expense_categories = [
        "Food", 
        "Home", 
        "Work", 
        "Fun", 
        "Misc"
    ]

    while True:
        print("Select catagory")

        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"

        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
            
        except Exception:
            print("Needs to be a number")
            continue

        if selected_index in range(len(expense_categories)):
            selcted_category = expense_categories[selected_index]
            new_expense = Expense(name = expense_name, category = selcted_category, amount = expense_amount)
            return new_expense

        else:
            print("Invalid option")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(expense)
    
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")

def summarize_expense(expense_file_path, budget):
    expenses: list[Expense] = []

    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by Category: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum ([ex.amount for ex in expenses])
    print(f"You've spent {total_spent:.2f} this month")

    remaining_budget = budget - total_spent
    print(f"Budget reamiang for this month: {remaining_budget:.2f}")

    # Get current date
    now = datetime.datetime.now()

    # Get num of days in current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate remaining days in the month
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(f"Budget per day: ${daily_budget:.2f}")

if __name__ == '__main__':
    main()
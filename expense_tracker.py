# Simple Expense Tracker
# Skillvoro Internship Program 2026

expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    description = input("Enter expense description: ").strip()

    if description == "":
        print("Description cannot be empty.")
        return

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Invalid amount! Please enter a number.")

    category = input("Enter category: ").strip()

    if category == "":
        print("Category cannot be empty.")
        return

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['description']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total Expenses: ₹{total:.2f}")


def category_summary():
    print("\n--- Category Summary ---")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


def display_menu():
    print("\n" + "=" * 40)
    print("        EXPENSE TRACKER")
    print("=" * 40)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    print("=" * 40)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
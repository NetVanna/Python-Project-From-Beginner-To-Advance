from expenses import Expense


def main():
    """
    Main application entry point.
    """
    print("=== Expense Tracker ===\n")

    expense_file_path = "expenses.txt"

    # Get user expense
    expense = get_user_expense()

    # Save expense
    save_expense_to_file(expense, expense_file_path)

    # Show summary
    summarize_expense(expense_file_path)


def get_user_expense():
    """
    Ask user for expense information.
    """

    expense_name = input("Enter expense name: ")

    while True:
        try:
            expense_amount = float(
                input("Enter expense amount: ")
            )
            break
        except ValueError:
            print("Please enter a valid number!")

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "🧑‍💼 Work",
        "😜 Fun",
        "🎵 Music",
    ]

    while True:
        print("\nSelect a category:")

        for i, category_name in enumerate(
            expense_categories,
            start=1
        ):
            print(f"{i}. {category_name}")

        try:
            selected_index = (
                int(input("Enter category number: ")) - 1
            )

            if selected_index in range(
                len(expense_categories)
            ):
                selected_category = (
                    expense_categories[selected_index]
                )

                return Expense(
                    expense_name,
                    selected_category,
                    expense_amount
                )

            print("Invalid category!")

        except ValueError:
            print("Please enter a number!")


def save_expense_to_file(
    expense: Expense,
    expense_file_path
):
    """
    Save expense into text file.
    """

    print(
        f"\nSaving Expense: {expense}"
    )

    with open(
        expense_file_path,
        mode="a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{expense.name},"
            f"{expense.category},"
            f"{expense.amount}\n"
        )


def summarize_expense(expense_file_path):
    """
    Read all expenses and display summary.
    """

    print("\n=== Expense Summary ===")

    expenses = []

    with open(
        expense_file_path,
        mode="r",
        encoding="utf-8"
    ) as file:

        for line in file:
            name, category, amount = (
                line.strip().split(",")
            )

            expense = Expense(
                name,
                category,
                float(amount)
            )

            expenses.append(expense)

    # Display expenses
    print("\nExpenses:")

    for expense in expenses:
        print(expense)

    # Total spent
    total_spent = sum(
        expense.amount
        for expense in expenses
    )

    print(
        f"\n💰 Total Spent: ${total_spent:.2f}"
    )

    # Category totals
    print("\n📊 Spending by Category:")

    category_totals = {}

    for expense in expenses:

        if expense.category not in category_totals:
            category_totals[
                expense.category
            ] = 0

        category_totals[
            expense.category
        ] += expense.amount

    for category, amount in (
        category_totals.items()
    ):
        print(
            f"{category}: ${amount:.2f}"
        )

    # Budget
    budget = 2000

    remaining = budget - total_spent

    print(
        f"\n🎯 Budget: ${budget:.2f}"
    )

    print(
        f"💵 Remaining: ${remaining:.2f}"
    )


if __name__ == "__main__":
    main()
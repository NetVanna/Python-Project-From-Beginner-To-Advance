class Expense:
    """
    Represents a single expense.
    """

    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return (
            f"Expense(name={self.name}, "
            f"category={self.category}, "
            f"amount={self.amount:.2f})"
        )
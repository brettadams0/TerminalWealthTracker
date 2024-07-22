# Complete Terminal Finance Tracker

class FinanceTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, source):
        self.balance += amount
        self.transactions.append(('Income', amount, source))

    def add_expense(self, amount, category):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(('Expense', amount, category))
        else:
            print("Insufficient funds for this expense.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

def main():
    tracker = FinanceTracker()

    while True:
        print("\nFinance Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            tracker.add_income(amount, source)
            print(f"Income of {amount} added from {source}.")
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            tracker.add_expense(amount, category)
            print(f"Expense of {amount} added for {category}.")
        elif choice == '3':
            print(f"Current Balance: {tracker.get_balance()}")
        elif choice == '4':
            print("Transactions:")
            for transaction in tracker.get_transactions():
                print(transaction)
        elif choice == '5':
            print("Exiting Finance Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

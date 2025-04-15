class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transaction_history = []
        self.loan_balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount:.2f}")
            print(f"Deposited {amount:.2f} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount:.2f}")
            print(f"Withdrew {amount:.2f} successfully.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def view_balance(self):
        print(f"Current balance: {self.balance:.2f}")

    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

    def apply_for_loan(self, amount, interest_rate, term_years):
        if amount > 0 and interest_rate > 0 and term_years > 0:
            self.loan_balance = amount * ((1 + interest_rate) ** term_years)
            print(f"Loan approved! Total loan balance: {self.loan_balance:.2f}")
        else:
            print("Invalid loan parameters.")

    def view_loan_balance(self):
        print(f"Loan balance: {self.loan_balance:.2f}")


class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1

    def create_account(self, account_holder):
        account_number = self.next_account_number
        self.accounts[account_number] = BankAccount(account_number, account_holder)
        self.next_account_number += 1
        print(f"Account created successfully. Account Number: {account_number}")
        return account_number

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for account in self.accounts.values():
                    data = (
                        f"{account.account_number}|{account.account_holder}|{account.balance}|"
                        f"{account.loan_balance}|{'#'.join(account.transaction_history)}\n"
                    )
                    file.write(data)
            print("Accounts saved successfully.")
        except Exception as e:
            print(f"Error saving accounts to file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    account_number, account_holder, balance, loan_balance, transaction_history = line.strip().split('|')
                    account = BankAccount(int(account_number), account_holder)
                    account.balance = float(balance)
                    account.loan_balance = float(loan_balance)
                    account.transaction_history = transaction_history.split('#') if transaction_history else []
                    self.accounts[int(account_number)] = account
                self.next_account_number = max(self.accounts.keys(), default=0) + 1
            print("Accounts loaded successfully.")
        except Exception as e:
            print(f"Error loading accounts from file: {e}")


def menu():
    system = BankingSystem()

    while True:
        print("\nBanking System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Apply for Loan")
        print("5. View Account Balance")
        print("6. View Transaction History")
        print("7. View Loan Balance")
        print("8. Save Accounts to File")
        print("9. Load Accounts from File")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_holder = input("Enter account holder name: ")
            system.create_account(account_holder)

        elif choice == '2':
            account_number = int(input("Enter account number: "))
            account = system.find_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            account = system.find_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = int(input("Enter account number: "))
            account = system.find_account(account_number)
            if account:
                amount = float(input("Enter loan amount: "))
                interest_rate = float(input("Enter interest rate (as decimal): "))
                term_years = int(input("Enter term in years: "))
                account.apply_for_loan(amount, interest_rate, term_years)
            else:
                print("Account not found.")

        elif choice == '5':
            account_number = int(input("Enter account number: "))
            account = system.find_account(account_number)
            if account:
                account.view_balance()
            else:
                print("Account not found.")

        elif choice == '6':
            account_number = int(input("Enter account number: "))
            account = system.find_account(account_number)
            if account:
                account.view_transaction_history()
            else:
                print("Account not found.")

        elif choice == '7':
            account_number = int(input("Enter account number: "))
            account = system.find_account(account_number)
            if account:
                account.view_loan_balance()
            else:
                print("Account not found.")

        elif choice == '8':
            filename = input("Enter filename to save accounts: ")
            system.save_to_file(filename)

        elif choice == '9':
            filename = input("Enter filename to load accounts: ")
            system.load_from_file(filename)

        elif choice == '10':
            print("Exiting Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()


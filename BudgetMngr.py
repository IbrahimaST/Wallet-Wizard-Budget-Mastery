class BudgetManager:
    def __init__(self, amount):
        self.available_bal = amount
        self.budgets = {}
        self.expenses = {}

    def add_budget(self, name, amount):
        if name in self.budgets:
            raise ValueError("Preexisting Budget")
        if amount > self.available_bal:  # Access available_bal using self
            raise ValueError("Insufficient Funds")
        self.budgets[name] = amount
        self.available_bal -= amount
        self.expenses[name] = 0
        return self.available_bal

    def spend_budget(self, name, amount):
        if name not in self.expenses:
            raise ValueError("No Budget Available For This")
        self.expenses[name] += amount
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def budget_overview(self):
        print('Budget            Budgeted     Spent     Remaining')
        print('---------------- ---------- ----------- -----------')
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenses[name]
            remaining = budgeted - spent
            print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} ' f'{remaining:10.2f}')
            total_budgeted += budgeted
            total_spent += spent
            total_remaining += remaining
        print('---------------- ---------- ----------- -----------')
        print(f'{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f} ' f'{total_budgeted - total_spent:10.2f}')

# Creates an instance of BudgetManager
outgoings = BudgetManager(2500)
outgoings.add_budget("Groceries", 500)
outgoings.add_budget("Rent", 300)
outgoings.add_budget("UberEats",150)
outgoings.spend_budget("UberEats",50)
outgoings.spend_budget("Groceries",432.50)
outgoings.spend_budget("Rent",275.43)
outgoings.budget_overview()

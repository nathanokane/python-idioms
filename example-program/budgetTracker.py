from dataclasses import dataclass, field
from datetime import datetime
from transaction import Transaction
import json


@dataclass
class BudgetTracker:
    transactions : list[Transaction] = field(default_factory=list)

    _valid_types_out = ["loan payment", "morgage payment", "gift out", "purchase", "withdrawl"]
    _valid_types_in = ["gift in", "wage", "deposit"]

    def add_transaction(self, transaction_value, transaction_type, transaction_description):
        if transaction_value == 0:
            print("Invalid transaction value")
            return
        

        if transaction_type not in BudgetTracker._valid_types_in and transaction_type not in BudgetTracker._valid_types_out:
            print("Invalid transaction type")
            return
        
        if transaction_value < 0 and transaction_type in BudgetTracker._valid_types_in:
            print("invalid transaction type, value is positive but transaction type is a withdrawl type")
            return
        elif transaction_value > 0 and transaction_type in BudgetTracker._valid_types_out:
            print("Invalid transaction type, value is negative but transaction type is a deposit type")
            return
        
        newTransaction = Transaction(transaction_value, transaction_type, transaction_description)
        self.transactions.append(newTransaction)
        print("Successfully added new transaction to the list")

    def remove_transaction_by_id(self, id):
        item_removed = False
        for item in self.transactions:
            if item.id == id:
                self.transactions.remove(item)
                item_removed = True
                break

        if item_removed:
            print(f"Transaction with ID {id} was successfully removed")
        else:
            print(f"No item found with id {id}")

    def get_transactions_by_type(self, transaction_type):
        if transaction_type not in BudgetTracker._valid_types_in and transaction_type not in BudgetTracker._valid_types_out:
            print(f"Invalid transaction type, {transaction_type} not found")
            return
        
        matching_transactions = []
        for item in self.transactions:
            if item.category == transaction_type:
                matching_transactions.append(item)

        return matching_transactions
        
    @property
    def transactions_total(self):
        return sum(t.amount for t in self.transactions)
    
    @property
    def print_transactions(self):
        print("Printing transactions...")
        for item in self.transactions:
            print("-"*20)
            print(item)

    def to_dict(self):
        return {
            "transaction_list": [i.to_dict() for i in self.transactions]
        }

    def report_to_json(self):
        print("Printing to JSON file...")
        with open("example-program/report.json", "w") as f:
            json.dump(self, f, default=lambda x: x.to_dict(), indent=4)



tracker1 = BudgetTracker()
tracker1.add_transaction(100, "deposit", "initial deposit")
tracker1.add_transaction(400, "deposit", "second deposit")
print(tracker1.transactions_total)
tracker1.print_transactions
#tracker1.remove_transaction_by_id(1)
print(tracker1.get_transactions_by_type("deposit"))
tracker1.add_transaction(-100, "loan payment", "another payment")
tracker1.report_to_json()

        




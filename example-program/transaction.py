from dataclasses import dataclass, field
from datetime import datetime

##This program was created by Nathan O'Kane on 30/06/25
#Last edited by Nathan O'Kane on 30/06/25

#The following is a dataclass showing how an immutable class object could be made
#There are some functions added to it that evaluate different things
#based on the already defined values in the object, however they DO NOT
#modify them as this class is immutable.

@dataclass(frozen=True)
class Transaction:
    amount: float
    category: str
    description: str
    timestamp: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        if self.amount == 0:
            raise ValueError("Invalid transaction value, cannot be zero")


        object.__setattr__(self, "category", self.category.lower())
        object.__setattr__(self, "amount", self.amount)
        object.__setattr__(self, "description", self.description)

    @property
    def is_income(self):
        return self.amount > 0
    
    @property
    def is_expense(self):
        return self.amount < 0
    
    @property
    def signed_amount(self):
        if self.amount > 0:
            return "+" + str(self.amount)
        else:
            return "-" + str(self.amount)
        
    @property
    def short_description(self):
        if len(self.description) > 30:
            print(self.description[:30] + "...")
        else:
            print(self.description)

    @property
    def timestamp_str(self):
        str_timestamp = str(self.timestamp)
        year = str_timestamp[:4]
        month = str_timestamp[5:7]
        day = str_timestamp[8:10]
        time = str_timestamp[11:]
        return year + "-" + month + "-" + day + " " + time
    
    @property
    def timestamp_day(self):
        return self.timestamp.strftime("%A")


transaction1 = Transaction(amount=12.10, category="deposit", description="input of cash")
print(transaction1.timestamp_str)
print(transaction1.timestamp_day)
    
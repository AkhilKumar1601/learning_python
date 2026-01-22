class Account:

    def __init__(self,balance):
        self._balance = balance;

    @property
    def balance(self):
        return self._balance;

    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance =  value;

    def __str__(self):
        return f"Amount Balance: {self._balance}";

    def __len__(self):
        return len(str(self._balance));

    def __add__(self,other):
        return self._balance + other._balance;

"""
a = Account(5000);
print(a);
print(len(a));
a.balance = 7000;
print(a.balance);
"""
class SavingsAccount(Account):
    
    def __init__(self,balance,interest_rate):
        super().__init__(balance);
        self.interest_rate = interest_rate;

    def add_interest(self):
        self._balance = self._balance + (self._balance * (self.interest_rate / 100));

"""
sa = SavingsAccount(4000,5);
sa2 = Account(2000);
print(sa);
print(len(sa));
sa.balance = 8000;
print(sa.balance);
sa.add_interest();
print(sa.balance);
print(sa + sa2);
"""

a1 = Account(5000)
a2 = SavingsAccount(10000, 5)

print(a1)            # Account Balance: 5000
print(a2)            # Account Balance: 10000

a2.add_interest()
print(a2.balance)   # 10500

print(len(a1))       # 4
print(a1 + a2)       # 15500


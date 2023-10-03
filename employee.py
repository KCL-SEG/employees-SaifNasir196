"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

# from enum import Enum

# abstract class
class Commission:
    # abstract method
    def calc_commission(self):
        pass
   
class Bonus(Commission):
    def __init__(self, bonus) -> None:
        self.bonus = bonus
        
    def calc_commission(self):
        return self.bonus
    
    # e.g. receives a bonus commission of 600
    def __str__(self) -> str:
        return f' and receives a bonus commission of {self.bonus}'
        

class Contract(Commission):
    def __init__(self, no_of_contracts, commissionPerContract) -> None:
        self.no_of_contracts = no_of_contracts
        self.commissionPerContract = commissionPerContract
        
    def calc_commission(self):
        return self.no_of_contracts * self.commissionPerContract

    # e.g. receives a commission for 3 contract(s) at 220/contract
    def __str__(self) -> str:
        return f' and receives a commission for {self.no_of_contracts} contract(s) at {self.commissionPerContract}/contract'

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    # abstract method
    def get_pay(self):
        pass

    def __str__(self):
        commision = ""
        if self.commission:
            commision = str(self.commission)
        return commision
    
    def get_commission(self):
        if not self.commission:
            return 0
        return self.commission.calc_commission()


class Salary_Employee(Employee):
    def __init__(self, name, salary, commission= None):
        super().__init__(name, commission)
        self.salary = salary
    def get_pay(self):
        return self.salary + self.get_commission()
    
    def __str__(self):
        # e.g. Billie works on a monthly salary of 4000
        comm = super().__str__()
        return  f'{self.name} works on a monthly salary of {self.salary}{comm}. Their total pay is {self.get_pay()}.'

class Hourly_Employee(Employee):
    def __init__(self, name, wage, hours, commission= None):
        super().__init__(name, commission)
        self.wage = wage
        self.hours = hours
    def get_pay(self):
        return self.wage * self.hours + self.get_commission()
        
    def __str__(self):
        # Charlie works on a contract of 100 hours at 25/hour
        comm = super().__str__()
        return  f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour{comm}. Their total pay is {self.get_pay()}.'
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary_Employee('Billie', 4000)
# print(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee('Charlie', 25, 100)
# print(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary_Employee('Renee', 3000, Contract(4, 200))
# print(renee)

# # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Employee('Jan', 25, 150, Contract(3, 220))
# print(jan)

# # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary_Employee('Robbie', 2000, Bonus(1500))
# print(robbie)

# # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Employee('Ariel', 30, 120, Bonus(600))
# print(ariel)
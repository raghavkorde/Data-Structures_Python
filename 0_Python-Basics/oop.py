class BankAccount:
    __interest_rate = 0.05  # Private instance variable

    # Constructor used to create instances
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __calculate_interest(self):  # Private instance method
        return self.balance * self.__interest_rate

    @staticmethod
    def get_interest_rate():  # Static instance method
        return BankAccount.__interest_rate

    @classmethod
    def validate_account_number(cls, account_number):  # Class method
        if len(account_number) == 10 and account_number.isdigit():
            return True
        else:
            return False

    def apply_interest(self):
        interest = self.__calculate_interest()
        self.balance += interest
        print("Interest applied. New balance:", self.balance)

    def __str__(self):  # Overloaded __str__() method
        return f"Bank Account - Account Number: {self.account_number}, Balance: {self.balance}"


# Creating a BankAccount instance
account = BankAccount("123456789", 1000)

# Accessing instance attributes
print("Account Number:", account.account_number)
print("Balance:", account.balance)

# Accessing static instance method
interest_rate = BankAccount.get_interest_rate()
print("Interest Rate:", interest_rate)

# Applying interest
account.apply_interest()

# Validating account number using class method
is_valid = BankAccount.validate_account_number(account.account_number)
print("Account Number Validity:", is_valid)

# Overloading print() function
print(account)


"""
Class Method:
    They receive the class itself as the first parameter, conventionally named cls, instead of the instance.
    Class methods are bound to the class rather than individual instances.
    They can access and modify class-level attributes, perform operations related to the class, or provide alternative ways to construct instances.
    Class methods can be called on both the class and its instances.

Class Variable:
    Class variables are declared within the class but outside any instance methods.
    They are shared among all instances of the class.
    Class variables are accessed using the class name, followed by the variable name.
    They can be used to store data or state that is relevant to the entire class, rather than specific to individual instances.

Static Method:
    They do not receive an implicit first parameter (usually named self or cls) like regular methods or class methods.
    Static methods are not bound to the class or instances and do not have access to class or instance attributes.
    They are independent functions within the class and do not require the class or an instance to be called.
    Static methods are typically used for utility functions or operations that are not specific to the class or its instances.

Static Variable:
    They are typically class-level variables that are defined outside any methods within the class.
    Like class variables, static variables are shared among all instances of the class.
    They can be accessed using the class name, followed by the variable name, or through an instance of the class.
    Static variables are useful for storing data or state that is shared across all instances of the class, but not specific to individual instances.
    
"""
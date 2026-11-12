class AccountnotFoundError(Exception):
    def __init__(self, message= "Account not found!"):
        self.message = message
        super().__init__(self.message)

class InvalidPinError(Exception):
    def __init__(self, message= "Pin is not correct!"):
        self.message = message
        super().__init__(self.message)

class InsufficientBalanceError(Exception):
    def __init__(self, message= "Your Balance is low!"):
        self.message = message
        super().__init__(self.message)

class InvalidAmountError(Exception):
    def __init__(self, message= "Your amount is incorrect!"):
        self.message = message
        super().__init__(self.message)

accounts = {
    "1001" : {
        "Name" : "Sahil Khan",
        "Pin" : "1234",
        "Balance" : 50000
    },
    "1002":{
        "Name" : "Sahil Khan",
        "Pin" : "4567",
        "Balance" : 70000

    },
}

def create_account(acc_no,name,pin,balance):
    if not acc_no.isdigit():
        raise ValueError("Account number must be in digit!")
    if not len(acc_no)==4:
        raise ValueError("Account number should be in 4 digit!")
    if not all(char.isalpha() or char == " " for char in name):
        raise ValueError("Name must be character and space!")
    if len(name) >20:
        raise ValueError("Your Name is very lengthy!")
    if not pin.isdigit():
        raise ValueError("Pin must be in digit!")
    if not len(pin)==4:
        raise ValueError("Pin length should be in 4 digit!")
    if balance<=0:
        raise InvalidAmountError("Balance must be positive!")
    if balance > 200000:
        raise InvalidAmountError("Your balance is too big, we cann't store!")
    print("-"*15)
    accounts[acc_no]={"Name":name, "Pin":pin, "Balance":balance}
    print(f"Your account {acc_no} has been created!")
    print("-"*15)
    
    return acc_no,name,pin,balance

    
def check_balance(acc_no,pin):
    if acc_no not in accounts:
        raise AccountnotFoundError(f"Account {acc_no} not found!")
    if accounts[acc_no]["Pin"]!=pin:
        raise InvalidPinError(f"Pin {pin} not matched!")
    print("-"*15)
    print("Your balance is:",accounts[acc_no]["Balance"])
    print("-"*15)
    return acc_no,pin

def deposite_money(acc_no,amount):
    if acc_no not in accounts:
        raise AccountnotFoundError(f"Account {acc_no} not found!")   
    if amount <= 0:
        raise InvalidAmountError(F"Amount {amount} must be to positive!")
    if amount > 200000:
        raise InvalidAmountError("Please Enter less amount!")
    accounts[acc_no]["Balance"]+=amount
    print("-"*15)
    print(f"Money is credited {amount}!")
    print(f"your current balance is:{accounts[acc_no]['Balance']}")
    print("-"*15)
    return acc_no,amount

def withdraw(acc_no,pin,amount):  
    if acc_no not in accounts:
            raise AccountnotFoundError(f"Account{acc_no}not found!")
    if accounts[acc_no]["Pin"]!=pin:
        raise InvalidPinError(f"Pin{pin} not matched!") 
    if amount<=0:
            raise InvalidAmountError(F"Amount{amount} must be to positive!")
    if amount > 200000:
        raise InvalidAmountError("Please Enter less amount!")
    
    if amount > accounts[acc_no]["Balance"]:
        raise InsufficientBalanceError("Your withdraw money should be less than your Balance!")
    accounts[acc_no]["Balance"]-=amount
    print("-"*15)
    print(f"Withdrawn Successfully {amount}!")
    print(f"Now,your current balance is:{accounts[acc_no]['Balance']}")
    print("-"*15)
    return acc_no,pin,amount

while True:
    print("-"*15)
    feature = ["Create Account", "Check Balance", "Deposite Money", "Withdraw","Exit"]
    for index, item in enumerate(feature, start=1):
        print(index,":",item)
    print("-"*15)
        
    print("-"*15)
    for acc_no , details in accounts.items():
        print(acc_no,":",details)
    print("-"*15)    

    try:
        Select = int(input("Enter the one option...:"))
        if Select == 1:
            acc_no = input("Enter the account no:")
            name = input("Enter the name:")
            pin = input("Enter the pin:")
            balance = int(input("Enter the balance:"))
            create_account(acc_no,name,pin,balance)

        elif Select == 2:
            acc_no = input("Enter the account no:")
            pin = input("Enter the pin:")
            check_balance(acc_no,pin)

        elif Select == 3:
            acc_no = input("Enter the account no:")
            amount = int(input("Enter the amount:")) 
            deposite_money(acc_no,amount)

        elif Select == 4:
            acc_no = input("Enter the account no:")
            pin = input("Enter the pin:")
            amount = int(input("Enter the amount!"))
            withdraw(acc_no,pin,amount)
        elif Select == 5:
            print("Thank you for using our Banking System!")   
            print("Program is being close...bye!") 
            break
        else:
            print("Option did not match!")   

    except ValueError as e:
        print("Error:",e)
    except AccountnotFoundError as e:
        print("Error:",e)
    except InvalidPinError as e:
        print("Error:",e)
    except InsufficientBalanceError as e:
        print("Error:",e)
    except InvalidAmountError as e:
        print("Error:",e)                        
    

     




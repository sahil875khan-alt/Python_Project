class FileEmptyError(Exception):
    def __init__(self, message = "File is empty!"):
        self.message = message
        super().__init__(self.message)

def expense_tracker(expense_name,amount):
    if expense_name.strip() == "":
        raise ValueError("Expense name should not be empty!")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0!")
    try:
        with open("Expenses.txt","r") as f:
            data = f.read()
    except FileNotFoundError:
        pass

    return expense_name,amount
while True:
    print("*"*20)
    options = ["Add Expenses","Read Expenses","Exit","Clear all Expenses"]
    for point , option in enumerate(options,start=1):
        print(point,":",option)
    print("*"*20)    
    try:
        select = int(input("Enter the option:"))
    except ValueError:
        print("Please enter a valid number:")
        continue           
    try:
        if select == 1:
            print("="*20)
            print("Unless you will write 'exit',Expense name will be adding continously!")
            while True:
                expense_name = input("Enter the expense name:")
                if expense_name.lower() == "exit":
                    print("ok!Back to menu-->")
                    break
                try:
                    amount = float(input("Enter the amount:"))
                except ValueError:
                    print("Only integer allowed!") 
                    continue 
                try:    
                    expense_tracker(expense_name,amount)
                    with open("Expenses.txt","a") as f:
                        f.write(f"{expense_name},{amount}\n")    
                    print(f"Added:{expense_name}:{amount}") 
                except ValueError as e:
                    print("Error:",e)    
                print("="*20)
                         
        elif select == 2: 
            print("="*20)
            try:            
                with open("Expenses.txt","r") as f:
                    lines = f.readlines()
                if not lines:
                    raise FileEmptyError()    
                for index , entry  in enumerate(lines,start=1):
                    entry = entry.strip()
                    parts = entry.split(",")
                    name = parts[0]
                    amt = parts[1]
                    print(index,":",name,"-",amt) 
            except FileNotFoundError:
                print("File did not find!") 
            except FileEmptyError as e:
                print("Error:",e) 
            print("="*20)                     
        elif select == 3:
            print("Thank you!")
            break
        elif select == 4:
            print("="*20)
            try:   
                with open("Expenses.txt","r") as f:
                    lines = f.readlines()
                if not lines:
                    raise FileEmptyError()    
                confirm = input("Do you want to really delete content(yes/no):")
                if confirm.lower() == "yes":
                    with open("Expenses.txt","w") as f:
                        pass
                    print("All expenses cleared!")  
                elif confirm.lower() == "no":
                    print("Opration failed!")    
            except FileEmptyError as e:
                print("Error:",e)
            except FileNotFoundError:
                print("File does not exist!")
            print("="*20)                 
        else:
            print("Invalid input!") 
    except ValueError as e:
        print("Error:",e)
# avg = int(input("How many people you want to divide expenses?")) 

try:
    print("="*20)
    with open("Expenses.txt","r") as f:
        lines = f.readlines()
    if not lines:
        raise FileEmptyError()    
    total = 0
    for entry in lines:
        entry = entry.strip()
        parts = entry.split(",")
        amount = float(parts[1])
        total += amount
    print(f"\nTotal expense:{total}")
    print("="*20)
    try:
        print("="*20)
        confirm_2 = input("Do you want to divide your expenses(yes/no):")
        if confirm_2.lower() == "yes":
            avg = int(input("How many people you want to divide expenses?")) 
            if avg <=0:
                print("Number of people must be greater than 0!")
            else:          
                divide = total/avg
                print(f"\nAverage:{divide:.2f}")
        else:
            print("Opration Failed!")
        print("="*20)                
    except ValueError:
        print("Only integer number allowed!")  
except FileNotFoundError:
    print("The file has no created yet!") 
except FileEmptyError as e:
    print("Error:",e)



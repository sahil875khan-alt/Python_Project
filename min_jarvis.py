import datetime
def min_jarvis(command,user_name):
    if len(user_name)>=20:
        raise ValueError("Your name is very lenghty!")
    if not command.replace(" ","").isalpha():
        raise ValueError("Command should be is alpha and spaces!")
    command = command.lower()
    if "your name" in command:
        return "My name is Jarvis.Sahil created me."
    elif "hi jarvis" in command:
        return f"Hi,{user_name}!Nice to meet you.How can I assist you today?"
    elif "abhi kya time ho rha hai" in command:
        return f"It is at: {datetime.datetime.now().strftime('%H:%M')}"
    elif "ek joke sunao" in command:
        return "python itna slow kyu hai? kyuki wah snake🐍 hai, Cheetah🐅 nhi "
    else:
        return "I am sorry Sir,Your command did not understand me - Try Again!"
user_name = input("Enter the your name:")    
while True:
    try: 
        user_command = input("Enter the command:")
        if user_command.lower() == "bye":
            print(f"I am greatful to you {user_name}! See you again!")
            break
        print("Jarvis:",min_jarvis(user_command,user_name))
    except ValueError as e:
        print("Error:",e)    
       
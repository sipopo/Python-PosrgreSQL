menu = """ Please select one of following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to programming dairy!"

print(welcome)

user_input = input(menu)
while user_input != "3":
    if user_input == "1":
        print("Adding ...")
    elif user_input == "2":
        print("Viewing ...")
    else:
        print("Invalid option? please try again.")  
    
    user_input = input(menu)  


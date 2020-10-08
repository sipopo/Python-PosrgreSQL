from database import add_entry, get_entries

menu = """ Please select one of following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to programming dairy!"

def prompt_entry():
    entry_content = input("What do you learn :")
    entry_date = input("When do you learn it :")
    add_entry(entry_content, entry_date)

def print_entries():
    entries = get_entries()
    for entry in entries:
        print(f"- - - \n{entry['date']}\n{entry['content']}\n")

print(welcome)

user_input = input(menu)
while user_input != "3":
    if user_input == "1":
        prompt_entry()
    elif user_input == "2":
        print_entries()
    else:
        print("Invalid option? please try again.")  
    
    user_input = input(menu)  


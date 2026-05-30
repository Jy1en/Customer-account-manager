# Customer Account Manager
accounts = {} # Dictionary to store customer accounts

def create_account(name, phone, plan): #creates a reusable function
    accounts[phone] = { #uses the phone number as a unique key to store customer information
        "name": name,
        "phone": phone,
        "plan": plan,
    }
    print(f"Account created for {name}!")

def view_accounts():
    if len(accounts) == 0: #checks if there are no accounts
        print("No accounts found.")
    else:
        print("\n--- All Accounts ---")
        for phone, info in accounts.items(): #Loops through every account
            print(f"Name: {info['name']}, Phone: {phone}, Plan: {info['plan']}")
            #displays each account cleanly

def  update_account(phone, new_plan):
    if phone in accounts: #checks if that phone number exists
        accounts[phone]["plan"] = new_plan #finds that account and updates the plan
        print(f"Account updated! New plan for {accounts[phone]['name']}: {new_plan}")
    else:
        print("Account not found.")

def delete_account(phone):
    if phone in accounts: #checks if the account exists
        name = accounts[phone]["name"] #saves the name before deleting
        del accounts[phone] # deletes the account from the dictionary
        print(f"Account for {name} has been deleted.")
    else:
        print("Account not found.")

def main_menu():
    while True: #keeps the menu running until you choose Exit
        print("\n--- Customer Account Manager ---")
        print("1. create account")
        print("2. View Accounts")
        print("3. Update Account")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Choose an option: ")
        #lets you actually type into the program

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            plan = input(" Enter plan (Basic/Premium/Unlimited): ")
            create_account(name, phone, plan)
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            phone = input("Enter phone number: ")
            new_plan = input("Enter new plan: ")
            update_account(phone, new_plan)
        elif choice == "4":
            phone = input("Enter phone number: ")
            delete_account(phone)
        elif choice == "5":
            print("Goodbye!")
            break #exits the loop when you choose option 5
        else:
            print("Invalid option. Try again.")

main_menu()

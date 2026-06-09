import json
import time
import tos
tos.appdata("loginlib")
# Import core libraries
try:
    # Check if JSON database is already present
    f = open("users.json", "r")
    users_db = json.load(f)
    f.close()
except:
    # Create JSON database if missing
    print("Database not found, creating database...")
    users_db = {"placeholder": "placeholder"}
    f = open("users.json", "w")
    json.dump(users_db, f)
    f.close()

real_username = ""
# Placeholder values to prevent crashes
new_answer_login = ""
print("------------------------------------------")
print("Type 1 for login, 2 for sign up, 3 for exit.")
# User input menu, TUI
answer_login = input()
if answer_login == "1":
    print("Sending you to log in..")
    # Tells user they are going to login page
    # Send user to login when answer is 1
    time.sleep(1)
elif answer_login == "2":
    # Load sign up logic with elif
    print("Sending you to sign up..")
    time.sleep(1)
    print("Please enter the username you want:")
    new_username = input()
    # Store the desired username in a input variable
    print("Please enter the password you want:")
    # Store the desired password in another input variable
    new_password = input()
    users_db[new_username] = new_password
    # Add new user to RAM database
    print("User created successfully!")
    # Print to console that user is created
    f = open("users.json", "w")
    json.dump(users_db, f)
    f.close()
    # Add new user from RAM to JSON databases
    # Remove user information from RAM
    print("Type 1 for login, 2 for exit")
    new_answer_login = input()
    # User menu for post sign up actions
elif answer_login == "3": 
    print("Exiting...")
    # Exit logic if option 3 was selected
    time.sleep(2)
    exit()
if new_answer_login == "1":
    print("Sending you to log in..")
    # Send user to login if post sign up was chosen 1
    time.sleep(1)
elif new_answer_login == "2":
    # Exit logic if post sign up option 2
    print("Exiting..")
    time.sleep(2)
    exit()
else:
    print("Invalid answer!")
    exit()
    # Fallback if option greater than 2 or 3
    
       
while True:
    # Full sign in logic
    print("Please enter your username.")
    # Ask user for username
    input_username = input()
    # Store inputted username in a input variable
    time.sleep(1)
    print("Please enter your password.")
    # Ask user for password
    input_password = input()
    # Store inputted password in a input variable
    if input_username in users_db:
        print("Checking password..")
        time.sleep(2)
        if input_password in users_db[input_username] == input_password:
            # Compare inputted password to JSON database password if username found
            print("Logging in...")
            time.sleep(3)
            print("Login success!")
            print(f"Welcome back {input_username}!")
            # Welcome message using f strings
            print("------------------------------------------")
            break
        else:
            print("Username or password incorrect!")
            # Print a message saying the password or username (credentials) are not correct
    else:
        print("Checking database...")
        # Print verbose message
        time.sleep(1)
        print("Account not found!")
        # Print message stating account does not exist
        time.sleep(1)
        print("Exiting...")
        # Print verbose message
        time.sleep(2)
        # Break the while True: loop
        break
        # Exit the Python script
        exit()
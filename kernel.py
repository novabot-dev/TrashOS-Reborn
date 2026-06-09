import time
import subprocess
import json
import sys

version = "v3.0.0"
f = open("version.json", "w")
json.dump(version, f)
f.close()
# Import libraries
in_shell = False
input_username = ""

# Get boot mode from trashloader
boot_mode = sys.argv[1] if len(sys.argv) > 1 else "normal"
# Set shell var to false
def set_current_user(username):
    global current_user
    current_user = username
def post():
    subprocess.run([sys.executable, 'postanimation.py'])
    # Define post def
def login():
    import json
    import time
    global input_username
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
    if answer_login == "1" or new_answer_login == "1":
        print("Sending you to log in..")
        # Send user to login if chosen 1 or after sign up
        time.sleep(1)
    elif new_answer_login == "2":
        # Exit logic if post sign up option 2
        print("Exiting..")
        time.sleep(2)
        exit()
    else:
        if answer_login != "1":
            print("Invalid answer!")
            exit()
        # Continue to login if answer was 1
        
        
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
            if users_db[input_username] == input_password:
                # Compare inputted password to JSON database password if username found
                print("Logging in...")
                time.sleep(3)
                print("Login success!")
                print(f"Welcome back {input_username}!")
                # Welcome message using f strings
                print("------------------------------------------")
                set_current_user(input_username)
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
        
post()
# Run post script
print(f"TrashOS RB Kernel {version} - Mode: {boot_mode}")
# Print kernel version
login()
time.sleep(11)
subprocess.run([sys.executable, 'bash.py'])
with open("username.txt", "w") as f:
    f.write(input_username)
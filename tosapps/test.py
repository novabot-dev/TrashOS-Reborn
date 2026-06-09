import time
import tos
import os
import random
appdata_pth = tos.appdata.path("guess_game")
root_no_yes = tos.is_root()
print(f"[DEBUG] Saved appdata to {appdata_pth}")
time.sleep(0.2)
print(f"[DEBUG] Is root returned {root_no_yes}")
time.sleep(0.5)
print("Guess the number game")
root_no_yes = tos.is_root()
if root_no_yes == True:
    print("App cannot run as root")
else:
    data = input("Please accept to our partner data terms Y N: ").lower()
appdata_pth = tos.appdata.path("guess_game")
if data == "y":
    answer = random.randint(0,10)
    guess = input("Enter your guess!")
    if guess != answer:
        print("Wrong guess!!")
        print(f"Answer was {answer}")
    elif guess == answer:
        print(f"Correct!! You guessed {answer}")
else:
    print("Declined")
    exit()
time.sleep(0.5)
tos.term.cls()

exit()
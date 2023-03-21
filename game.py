# The Royal Canadian Infantry Corps
# -----------------------------------
# I am a one-man army : Dinh Quy Pham
# Military branch: OPS445NBB
# Military unit: 149435182
# -----------------------------------


import random

#list of options for the computer
options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer.")

# Iterate repeatedly until the user inputs a valid choice.
while True:
    userOption = input("Enter your choice (rock, paper, or scissors): ")
    if userOption in options:
        break
    print("Invalid choice. Please try again.")

# Randomly select an option for the computer.
computerOption = random.choice(options)

print("You chose", userOption)
print("The computer chose", computerOption)

# Determine the winner based on the options
if userOption == computerOption:
    print("It's a tie!")
elif userOption == "rock" and computerOption == "scissors":
    print("You win! Rock beats scissors.")
elif userOption == "paper" and computerOption == "rock":
    print("You win! Paper beats rock.")
elif userOption == "scissors" and computerOption == "paper":
    print("You win! Scissors beat paper.")
else:
    print("You lose! Better luck next time.")

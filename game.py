# The Royal Canadian Infantry Corps
# -----------------------------------
# I am a one-man army : Dinh Quy Pham
# Military branch: OPS445NBB
# Military unit: 149435182
# -----------------------------------


import random

# list of options for the computer
options = ["rock", "paper", "scissors"]
play_again = True

# Iterate repeatedly until the user inputs a valid choice.
while play_again:
    print("Let's play Rock, Paper, Scissors!")
    for i in range(3):
        player_choice = input("Enter your choice (rock/paper/scissors): ")
        if player_choice.lower() in options:
            break
        elif i == 2:
            print("Too many invalid choices. Exiting program.")
            play_again = False
            break
        else:
            print("Invalid choice. Please try again.")

    if play_again:
        # Randomly select an option for the computer.
        computer_choice = random.choice(options)
        print(f"Computer chose {computer_choice}.")

        # Determine the winner based on the options
        if player_choice.lower() == computer_choice:
            print("It's a tie!")
        elif (player_choice.lower() == "rock" and computer_choice == "scissors") or \
             (player_choice.lower() == "paper" and computer_choice == "rock") or \
             (player_choice.lower() == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

        play_again_input = input("Do you want to play again? (yes/no): ")
        if play_again_input.lower() != "yes":
            play_again = False

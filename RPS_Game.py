import random

print("Welcome to Rock-Paper-Scissors!")
print("Enter your choice (rock, paper, or scissors):")

# List of valid choices
choices = ["rock", "paper", "scissors"]

# Get the user's choice
user_choice = input().lower()

# Validate the user's choice
while user_choice not in choices:
    print("Invalid choice. Please try again.")
    user_choice = input().lower()

# Get the computer's choice
computer_choice = random.choice(choices)
print("Computer chose", computer_choice)

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
else:  # user_choice == "scissors"
    if computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")

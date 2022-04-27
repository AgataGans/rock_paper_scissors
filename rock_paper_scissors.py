import random
import inquirer


choices = ["Rock!", "Paper!", "Scissors!"]
user_choice = [inquirer.List('choice', choices = choices)]
answers = inquirer.prompt(user_choice)
user_answer = list(answers.values())[0] # change dict to list
computer_choice = random.choice(choices) # randomly select element from list


print(f"Your answer is {user_answer} and computer answer is {computer_choice}")

if user_answer == "Rock!" and computer_choice == "Paper!":
    print("You've lost")

if user_answer == "Rock!" and computer_choice == "Scissors!":
    print("You've won")

if user_answer == "Paper!" and computer_choice == "Rock!":
    print("You've won")

if user_answer == "Paper!" and computer_choice == "Scissors!":
    print("You've lost")

if user_answer == "Scissors!" and computer_choice == "Rock!":
    print("You've lost")

if user_answer == "Scissors!" and computer_choice == "Paper!":
    print("You've won")
elif user_answer == computer_choice:
    print("It's a draw")

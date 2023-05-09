import random

def play_round(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 0
    elif (user_choice == "stone" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissor") or (user_choice == "scissor" and computer_choice == "stone"):
        return -1
    else:
        return 1

def play_game(rounds):
    choices = ["stone", "paper", "scissor"]
    user_score = 0
    computer_score = 0

    for _ in range(rounds):
        user_choice = input("Enter your choice (stone/paper/scissor): ").lower()
        while user_choice not in choices:
            print("Invalid choice. Please try again.")
            user_choice = input("Enter your choice (stone/paper/scissor): ").lower()

        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)

        round_result = play_round(user_choice, computer_choice)

        if round_result == 1:
            user_score += 1
            print("You win this round!")
        elif round_result == -1:
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

    print("\nGame Over")
    print("User score:", user_score)
    print("Computer score:", computer_score)

    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")


rounds = int(input("How many rounds do you want to play? "))
play_game(rounds)
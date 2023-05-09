import random

def play_game(rounds):
    options = ['stone', 'paper', 'scissor']
    user_score = 0
    computer_score = 0
    
    for _ in range(rounds):
        user_choice = input("Enter your choice (stone/paper/scissor): ").lower()
        computer_choice = random.choice(options)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 'stone':
            if computer_choice == 'paper':
                print("Computer wins this round!")
                computer_score += 1
            else:
                print("You win this round!")
                user_score += 1
        elif user_choice == 'paper':
            if computer_choice == 'scissor':
                print("Computer wins this round!")
                computer_score += 1
            else:
                print("You win this round!")
                user_score += 1
        elif user_choice == 'scissor':
            if computer_choice == 'stone':
                print("Computer wins this round!")
                computer_score += 1
            else:
                print("You win this round!")
                user_score += 1
        else:
            print("Invalid choice. Please enter stone, paper, or scissor.")
        
        print("------------------------")
    
    print("Game over!")
    print(f"You: {user_score} | Computer: {computer_score}")
    
    if user_score > computer_score:
        print("You won the game!")
    elif user_score < computer_score:
        print("Computer won the game!")
    else:
        print("It's a tie!")

# Main program
num_rounds = int(input("Enter the number of rounds you want to play: "))
play_game(num_rounds)

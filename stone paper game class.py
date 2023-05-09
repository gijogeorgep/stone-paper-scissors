import random

class StonePaperScissors:
    def __init__(self):
        self.choices = ["stone", "paper", "scissor"]
        self.player_score = 0
        self.computer_score = 0

    def play_game(self):
        rounds = int(input("How many rounds do you want to play? "))
        for _ in range(rounds):
            player_choice = input("Enter your choice (stone/paper/scissor): ").lower()
            computer_choice = random.choice(self.choices)
            print("Computer's choice:", computer_choice)
            self.compare_choices(player_choice, computer_choice)

        self.print_results()

    def compare_choices(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "stone" and computer_choice == "scissor")
            or (player_choice == "paper" and computer_choice == "stone")
            or (player_choice == "scissor" and computer_choice == "paper")
        ):
            print("You win this round!")
            self.player_score += 1
        else:
            print("Computer wins this round!")
            self.computer_score += 1

    def print_results(self):
        print("Final score:")
        print("Player:", self.player_score)
        print("Computer:", self.computer_score)

        if self.player_score > self.computer_score:
            print("Congratulations, you win!")
        elif self.player_score < self.computer_score:
            print("Computer wins!")
        else:
            print("It's a tie!")

# Create an instance of the game and play
game = StonePaperScissors()
game.play_game()

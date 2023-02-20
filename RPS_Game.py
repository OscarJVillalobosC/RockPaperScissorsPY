
# Defining the player through a class
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = None

# function that describes the choice
    def choose(self):
        self.choice = input(f"{self.name}, please choose (rock, paper, or scissors): ").lower()
        while self.choice not in ["rock", "paper", "scissors"]:
            self.choice = input("Invalid choice. Please try again").lower()

# Defining the Game through a class
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.choices = ["rock", "paper", "scissors"]

    def play_round(self):
        self.player1.choose()
        self.player2.choose()
        print(f"{self.player1.name} chose {self.player1.choice}")
        print(f"{self.player2.name} chose {self.player2.choice} ")

        if self.player1.choice == self.player2.choice:
            print("It's a tie!")
        elif self.player1.choice == "rock":
            if self.player2.choice == "scissors":
                print(f"{self.player1.name} wins!")
                self.player1.score += 1
            else:
                print(f"{self.player2.name} wins!")
                self.player2.score += 1
        elif self.player1.choice == "paper":
            if self.player2.choice == "rock":
                print(f"{self.player1.name} wins!")
                self.player1.score += 1
            else:
                print(f"{self.player2.name} wins!")
                self.player2.score += 1
        else:
            if self.player2.choice == "paper":
                print(f"{self.player1.name} wins!")
                self.player1.score += 1
            else:
                print(f"{self.player2.name} wins!")
                self.player2.score += 1

# Playing the game function 
    def play_game(self):
        while max(self.player1.score, self.player2.score) < 3:
            self.play_round()
        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins the game!")
        else:
            print(f"{self.player2.name} wins the game!")

# Players invoked by objects 
player1 = Player("Player 1")
player2 = Player("Player 2")

# Game invoked by an object
game = Game(player1,player2)

# Invoking the game by calling the function
game.play_game()



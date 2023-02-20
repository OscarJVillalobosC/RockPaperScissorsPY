import random


class Node:
    def __init__(self, player, choice):
        self.player = player
        self.choice = choice
        self.next = None

# Defining the player through a class


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.history = None
        self.tail = None

# method that describes the history of a player's moves

    def add_move_to_history(self, choice):
        if self.history is None:
            self.history = Node(self, choice)
            self.tail = self.history
        else:
            new_node = Node(self, choice)
            self.tail.next = new_node
            self.tail = new_node

# method that describes the choice
    def choose(self):
        choice = input(f"{self.name}, please choose (rock, paper, or scissors): ").lower()
        while choice not in ["rock", "paper", "scissors"]:
            choice = input("Invalid choice. Please try again").lower()
        self.add_move_to_history(choice)
        self.choice = choice
    
    def choose_random(self):
        choice = random.choice(["rock", "paper", "scissors"])
        self.add_move_to_history(choice)
        self.choice = choice

# method that describes the player's move history
    def print_history(self):
        current_node = self.history
        while current_node is not None:
            print(f"{self.name} chose {current_node.choice}")
            current_node = current_node.next

# Defining the Game through a class


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.choices = ["rock", "paper", "scissors"]

    def play_round(self):
        self.player1.choose()
        self.player2.choose_random()
        print(f"{self.player1.name} chose {self.player1.choice}")
        print(f"{self.player2.name} chose {self.player2.choice}")

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
player2 = Player("Computer")


# Game invoked by an object
game = Game(player1, player2)

# Invoking the game by calling the function
game.play_game()

# Print out the move history for each player
player1.print_history

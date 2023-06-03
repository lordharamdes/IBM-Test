#python
# Importing the random module
import random

# Creating a Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

# Creating a Deck class
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        # Creating a list of suits and values
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # Looping through the suits and values and appending a Card object to the cards list
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        # Shuffling the cards list using the random module
        random.shuffle(self.cards)
    
    def deal(self):
        # Popping and returning the last card from the cards list
        return self.cards.pop()

# Creating a Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
    
    def draw(self, deck):
        # Drawing a card from the deck and appending it to the hand list
        self.hand.append(deck.deal())
    
    def show_hand(self):
        # Printing the name and the hand of the player
        print(f"{self.name}'s hand: {self.hand}")
    
    def calculate_score(self):
        # Initializing the score to zero
        self.score = 0
        # Looping through the hand and adding the value of each card to the score
        for card in self.hand:
            if card.value in ["J", "Q", "K"]:
                # Face cards are worth 10 points
                self.score += 10
            elif card.value == "Ace":
                # Ace can be worth 1 or 11 points depending on the score
                if self.score + 11 > 21:
                    self.score += 1
                else:
                    self.score += 11
            else:
                # Other cards are worth their numerical value
                self.score += int(card.value)
    
    def hit_or_stand(self):
        # Asking the player to hit or stand and returning their choice
        choice = input(f"{self.name}, do you want to hit or stand? (h/s) ")
        while choice not in ["h", "s"]:
            choice = input("Invalid input. Please enter h or s: ")
        return choice

# Creating a Dealer class that inherits from the Player class
class Dealer(Player):
    def __init__(self):
        # Calling the parent constructor with the name "Dealer"
        super().__init__("Dealer")
    
    def show_hand(self, hidden=False):
        # Printing the name and the hand of the dealer
        # If hidden is True, hiding the first card of the dealer
        if hidden:
            print(f"{self.name}'s hand: [Hidden], {self.hand[1]}")
        else:
            print(f"{self.name}'s hand: {self.hand}")
    
    def hit_or_stand(self):
        # Deciding whether to hit or stand based on the score of the dealer
        # The dealer must hit until their score is at least 17
        if self.score < 17:
            return "h"
        else:
            return "s"

# Creating a function to check for blackjack (a score of 21 with two cards)
def blackjack(player):
    return len(player.hand) == 2 and player.score == 21

# Creating a function to compare the scores of two players and declare a winner or a tie
def compare_scores(player1, player2):
    if player1.score > player2.score:
        print(f"{player1.name} wins!")
    elif player1.score < player2.score:
        print(f"{player2.name} wins!")
    else:
        print("It's a tie!")

# Creating a function to play a single game of blackjack
def play_game():
    # Creating a deck object and shuffling it
    deck = Deck()
    deck.shuffle()

    # Creating a player object and a dealer object
    player = Player(input("Enter your name: "))
    dealer = Dealer()

    # Drawing two cards for each player and calculating their scores
    for i in range(2):
        player.draw(deck)
        dealer.draw(deck)
    
    player.calculate_score()
    dealer.calculate_score()

    # Showing the hands of both players, hiding the first card of the dealer
    player.show_hand()
    dealer.show_hand(hidden=True)

    # Checking for blackjack for both players
    if blackjack(player) and blackjack(dealer):
        print("Both have blackjack! It's a tie!")
    elif blackjack(player):
        print(f"{player.name} has blackjack! {player.name} wins!")
    elif blackjack(dealer):
        print(f"{dealer.name} has blackjack! {dealer.name} wins!")
    
    else:
        
         # The game loop where each player gets to hit or stand until they bust or stand
        
         game_over = False
        
         while not game_over:

             # Asking the player to hit or stand
            
             player_choice = player.hit_or_stand()
            
             if player_choice == "h":
                 # Drawing a card for the player and calculating their score
                
                 player.draw(deck)
                 player.calculate_score()
                
                 # Showing the player's hand
                
                 player.show_hand()
                
                 if player.score > 21:
                     # The player busts and loses
                    
                     print(f"{player.name} busts! {dealer.name} wins!")
                     game_over = True
                
             else:
                 # The player stands and it's the dealer's turn
                
                 print(f"{player.name} stands.")
                
                 while True:

                     # Asking the dealer to hit or stand
                    
                     dealer_choice = dealer.hit_or_stand()
                    
                     if dealer_choice == "h":
                         # Drawing a card for the dealer and calculating their score
                        
                         dealer.draw(deck)
                         dealer.calculate_score()
                        
                         # Showing the dealer's hand
                        
                         dealer.show_hand(hidden=True)
                        
                         if dealer.score > 21:
                             # The dealer busts and loses

                             print(f"{dealer.name} busts! {player.name} wins!")
                             game_over = True
                        
                     else:
                         # The dealer stands and both scores are compared
                        
                         print(f"{dealer.name} stands.")
                        
                         # Showing both hands
                        
                         player.show_hand()
                         dealer.show_hand()
                        
                         compare_scores(player, dealer)
                         game_over = True
                    
                     if game_over:
                         break

# Asking the user if they want to play again

play_again = input("Do you want to play blackjack? (y/n) ")

while play_again.lower() == "y":
    
     play_game()
     play_again = input("Do you want to play again? (y/n) ")

print("Thanks for playing!")

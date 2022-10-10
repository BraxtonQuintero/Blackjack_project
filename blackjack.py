from random import Random
import itertools, random

class Game:

    def __init__(self, player: str):
        self.player = player
        self.dealer = Dealer
    
    def deal_cards():
        # got help here
        # https://www.programiz.com/python-programming/examples/shuffle-card
        deck = list(itertools.product(range(1,13),['Spade','Heart','Diamond','Club']))

        random.shuffle(deck)
        print("You got:")

        for i in range(2):
            print(deck[i][0], "of", deck[i][1])
             
class Dealer(Game):
    dealer_hand = []
    
    def deal_hit(self):
        if self.dealer >= 17:
            return "Dealer will stand."
        #else
        #self.dealer.hit
        dealt_card = Random.choice(self.deck)
        self.deck -= dealt_card
        return self.dealer_hand.append(dealt_card)
    
    
class Player(Game): # incomplete
    player_hand = []
    def __init__(self, player):
        
class Hand(Dealer, Player):

    def __init__(self, player_hand, dealer_hand):
        if player_hand >=22:
            print("You've busted")
        if dealer_hand >=22:
            print("Dealer has busted")
            
    def win_or_lose(self):
        if self.dealer > self.player:
            return "Dealer Won Hand"
        if self.dealer < self.player:
            print(f"{self.player}'s Hand!")
            return f"{self.player} You won the hand!"

        
def play_blackjack():
    name = input("Welcome to Braxton's BlackJack table! What is your name? ")

    ask = input(f"Welcome {name}, Would you like to play? yes or no ")
    if ask == 'yes':
        # got help here
        # https://www.programiz.com/python-programming/examples/shuffle-card
        deck = list(itertools.product(range(1,13),['Spade','Heart','Diamond','Club']))

        random.shuffle(deck)
        print("You got:")

        for i in range(2):
            print(deck[i][0], "of", deck[i][1])
            player.append(player_hand)
    if ask == 'no':   
        print('Come Back Soon!')

    ask2 = input('Would you like to hit or stand? ')

    if ask2 == 'hit':
        random.shuffle(deck)
        print("You got:")

        for i in range(1):
            print(deck[i][0], "of", deck[i][1])

    if ask2 == 'stand':
        print(f'{name} has chose to stand')
    
play_blackjack()
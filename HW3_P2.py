import random

class Card:
    ranks = []
    suits = {}
    
    def __init__(self):
        self.ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    
    
Deck = Card()
player1_win_num = 0
player2_win_num = 0

def player1Turn(deck):
    global player1_score
    player1_score = 0
    print("Player 1 turn:")
    for _ in range(2):
        rank = random.choice(deck.ranks)
        suit = random.choice(deck.suits)
        if rank in ['J','Q','K','A']:
            if rank == 'J':
                rank = 11
            if rank == 'Q':
                rank = 12
            if rank == 'K':
                rank = 13
            if rank == 'A':
                rank = 1
        player1_score += int(rank)
        #print(rank, suit)
        print("-"*10)
        if (rank in ['10',11,12,13]):
            print("|{}      |".format(rank))
            print("|{}       |".format(suit))
            print("|        |")
            print("|   {}    |".format(suit))
            print("|        |")
            print("|       {}|".format(suit))
            print("|      {}|".format(rank))
            print("-"*10)
        else:
            print("|{}       |".format(rank))
            print("|{}       |".format(suit))
            print("|        |")
            print("|   {}    |".format(suit))
            print("|        |")
            print("|       {}|".format(suit))
            print("|       {}|".format(rank))
            print("-"*10)
                
    print("Player 1 score: {}".format(player1_score))
    
def player2Turn(deck):
    global player2_score
    player2_score = 0
    print("Player 2 turn:")
    for _ in range(2):
        rank = random.choice(deck.ranks)
        suit = random.choice(deck.suits)
        if rank in ['J','Q','K','A']:
            if rank == 'J':
                rank = 11
            if rank == 'Q':
                rank = 12
            if rank == 'K':
                rank = 13
            if rank == 'A':
                rank = 1
        player2_score += int(rank)
        #print(rank, suit)
        print("-"*10)
        if (rank in ['10',11,12,13]):
            print("|{}      |".format(rank))
            print("|{}       |".format(suit))
            print("|        |")
            print("|   {}    |".format(suit))
            print("|        |")
            print("|       {}|".format(suit))
            print("|      {}|".format(rank))
            print("-"*10)
        else:
            print("|{}       |".format(rank))
            print("|{}       |".format(suit))
            print("|        |")
            print("|   {}    |".format(suit))
            print("|        |")
            print("|       {}|".format(suit))
            print("|       {}|".format(rank))
            print("-"*10)
        
    print("Playe 2 score: {}".format(player2_score))

def check_winner():
    global player1_win_num
    global player2_win_num
    
    if player1_score > player2_score:
        player1_win_num += 1
        print("Player 1 is the Winner")
    elif player1_score == player2_score:
        print("It's a tie")
    else:
        player2_win_num += 1
        print("Player 2 is the Winner")
    
    print("Overall results")
    print("Player 1 total wins: {}, Player 2 total wins: {}".format(player1_win_num, player2_win_num))

play_again = 'Y'
number_of_games = 1
while (play_again.lower() == 'y'):
    print("Game Number: {}".format(number_of_games))
    player1Turn(Deck)
    print("\n")
    player2Turn(Deck)
    print("\n")
    check_winner()
    number_of_games += 1
    play_again = input("Play Again? 'Y/N': ")
    print("+==============================+")

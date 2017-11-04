import random
from os import system


class Player(object):
    """
    Player class to keep track of the 'bankroll'. Could probably live in the Hand() class.
    """

    def __init__(self, bankroll=100):
        self.bankroll = bankroll

    def add(self, amount):
        self.bankroll += amount

    def subtract(self, amount):
        self.bankroll -= amount


class Deck(object):
    """
    Deck class instantiated at the start of the round, it basically acts as a shuffle of deck of card.
    The more decks used the higher the probability the dealer has to win.
    """

    suit_names = ['♣', '♦', '♥', '♠']
    rank_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, deck_count=2):
        self.deck_count = deck_count
        self.card_list = [(rank, suit) for rank in self.rank_names for suit in self.suit_names]
        self.deck_list = [card for card in self.card_list for _ in range(self.deck_count)]

    def update(self, card):
        self.deck_list.remove(card)


class Hand(object):
    """
    Hand class instantiated per player, player 1 and the dealer. Is used for keeping track of what the player's
    hand is.
    """

    def __init__(self, player):
        self.player = player
        self.cards = []
        self.score = 0

    def __str__(self):
        hand = self.hand()
        return "%s's hand:\n%sTotal: %s\n" % (self.player, hand, self.score)

    def hand(self):
        hand = ""

        for card in self.cards:
            card_rank = card[0]
            card_suit = card[1]
            hand += card_rank + " of " + card_suit + "\n"
            
        return hand

    def card_add(self, card):
        self.cards.append(card)
        self.hand_score(card)

    def hand_score(self, card):

        if card[0] in ('Jack', 'Queen', 'King'):
            self.score += 10
        elif card[0] == 'Ace':
            if self.score > 10:
                self.score += 1
            else:
                self.score += 11
        else:
            self.score += int(card[0])


class Turn(object):
    """
    Using a class for this, function would probably work fine.
    """

    def deal(self, deck):
        card = random.choice(deck.deck_list)
        deck.update(card)
        return card


def player_round():
    """
    This function accepts an input from the player. Hit will add a card to the player's hand via the
    instantiated Hand class for player 1.
    If player 1 stands, the round is handed over to the dealer.
    """
    
    player_action = input('(h)it or (s)tand: ')

    print(player_action)

    if player_action == 'h':
        player_1.card_add(turn.deal(deck))
        if player_1.score > 21:
            calculate_winner()
        else:
            game()
    elif player_action == 's':
        dealer_round()
    else:
        print("Invalid option...")
        player_round() 


def dealer_round():
    """
    Once the player stands, the dealer will draw a card until the total is 17 or more at which point the dealer
    must stand.
    """

    if dealer.score < 17:
        dealer.card_add(turn.deal(deck))
        dealer_round()
    else:
        system('clear')
        calculate_winner()


def calculate_winner():
    """
    Function to determine a winner.
    """
    
    system('clear')
    print(dealer)
    print(player_1)
    
    if dealer.score < 22 > player_1.score:
        player_1_acc.subtract(10)
        winner = 'The Dealer'
    elif player_1.score > 21:
        print("%s's hand busted." % player)
        player_1_acc.subtract(10)
        winner = 'The Dealer'
    else:
        player_1_acc.add(10)
        winner = player
    
    print('%s is the winner' % winner)
    print('%s has %s units remaining.\n' % (player, player_1_acc.bankroll))
    replay()


def boot():
    """
    Will set some variables and capture the players name as well as set the 'bank roll'.
    """

    '''
    Make the variables global as they will be used later.
    Might pass them to the function in later releases.
    '''

    global player, player_1_acc

    system('clear')

    ''' May move this welcoming to function '''
    print("Black Jack - Let's Play!")
    print("Playing for fun 100 units, automatically betting 10 units.")

    ''' Set some game variables '''
    player = input("Please enter the player name: ")
    
    player_1_acc = Player()

    run()


def run():
    """
    This is the start of the game.
    """

    global deck, turn, player_1, player, dealer 

    ''' Instantiate some classes '''
    deck = Deck()
    turn = Turn()
    
    ''' Instantiate Player one and deal his hand '''
    player_1 = Hand(player)
    player_1.card_add(turn.deal(deck))
    player_1.card_add(turn.deal(deck))

    ''' Instantiate the Dealer and deal his one card '''
    dealer = Hand('The Dealer')
    dealer.card_add(turn.deal(deck))

    game()


def game():
    """
    The name of the function does not do the really describe what this is about. :)
    Basically, this will print out the game information as it stands, i.e. players scores and 'hands'.

    But I wanted to split this up as sometime I just want to refresh the game data and not instantiate the
    classes again. At first it was part of boot().
    """

    system('clear')
    print(dealer)
    print(player_1)
    player_round()


def replay():
    """
    Just an input which will 'restart' the game, will keep the same bankroll and player name.
    :return:
    """
    
    rply = input('Would you like to play again? (y)es or (n)o: ').lower()

    if rply == 'y':
        run()
    elif rply == 'n':
        print('Thanks for playing')
        exit()
    else:
        print('Please enter a valid option')
        replay()


boot()


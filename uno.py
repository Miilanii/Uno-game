import random

color = ["Green", "Yellow", "Red", "Blue"]
action_cards = ["Skip", "Reverse", "DrawTwo"]
wild_cards = ["Draw Four", "Wild"]
discard_pile = []
deck = []

top_card = ['Green', '6']

computer_skipped = False

# Creating the deck
def my_deck():
    for i in range(4):
        # Add number cards
        for num in range(10):
            card = [color[i], str(num)]
            if num == 0:
                deck.append(card)
            else:
                deck.append(card)
                deck.append(card)
        
        # Add action cards
        for action in action_cards:
            action_card = [color[i], action]
            deck.append(action_card)
            deck.append(action_card)
    
    # Add wild cards
    for wild in wild_cards:
        for _ in range(4):
            deck.append([wild])
    
    return deck

# Shuffling the deck
def shuffling(deck):
    random.shuffle(deck)
    return deck

card_deck = my_deck()
card_deck = shuffling(card_deck)
# Distributing the cards
player_hand = []
computer_hand = []
def distribute_cards():
    for i in range(7):
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())
    
    discard_pile.append(deck.pop())  #First card on the discard pile
    return player_hand, computer_hand

# Checking Playable cards
def check_playable(card, top_card):
    global top_color
    # Wild cards (can always be played)
    if card[0] == "Wild" or card[0] == "Draw Four":
        return True
    
    #Cheking Numbers and colors
    if len(card) == 2:  
        card_color, card_value = card
        try:
            top_color, top_value = top_card[:2]
        except:
            top_value = top_card[0]

        if card_color == top_color or card_value == top_value:
            return True

    return False

def get_playable_cards(player_hand, top_card):
    playable_cards = [] 

    for card in player_hand:
        if check_playable(card, top_card):
            playable_cards.append(card) 
    
    return playable_cards

#Players Turn, 
def player_turn(player_hand, top_card):
    print("Your turn!")
    print("Top card:", top_card)
    print("Your hand:", player_hand)
    
    playable_cards = get_playable_cards(player_hand, top_card)
    if playable_cards:
        print("Your playable cards are: ")
        for i in range(len(playable_cards)):
            print(f"{i + 1}: {playable_cards[i]}")
        
        choice = int(input("Choose a card to play, or 0 to draw: ")) - 1
        if choice == -1: #When the player chooses zero
            if card_deck:  
                drawn_card = card_deck.pop()
                player_hand.append(drawn_card)
                print("You drew:", drawn_card)
            else:
                print("No more cards left to draw.")
        elif choice in range(len(playable_cards)):
            played_card = playable_cards[choice]
            player_hand.remove(played_card)
            print("You played:", played_card)
            top_card = played_card  
       
            global computer_skipped

            if len(top_card) == 1:
                computer_skipped = True
                computer_hand.append(card_deck.pop())
                computer_hand.append(card_deck.pop())
                computer_hand.append(card_deck.pop())
                computer_hand.append(card_deck.pop())
                print("Draw Four Cards")
               
            elif top_card [0] == "Skip" or top_card [1] == "Skip":
                computer_skipped = True 
                print("Turn Skipped")
                player_turn(player_hand, top_card)
            elif top_card [0] == "Reverse" or top_card [1] == "Reverse":
                computer_skipped = True
                print("Turn Reversed")
                player_turn(player_hand, top_card)
            elif top_card [0] == "DrawTwo" or top_card [1] == "DrawTwo":
                computer_skipped = True
                computer_hand.append(card_deck.pop())
                computer_hand.append(card_deck.pop())
                print("DrawTwo Cards")

        else:
            print("Invalid choice, The game skips you")
    else:
        print("No playable cards, one card will be drawn from the deck.")
        if card_deck:
            drawn_card = card_deck.pop()
            player_hand.append(drawn_card)
            print("You drew:", drawn_card)
        else:
            print("No more cards left to draw.")

    return top_card

#Computer's turn
def computer_turn(computer_hand, top_card):
    print("\nComputer's turn!")
    print(f'Comps hand {computer_hand}')
    print(f'Comps len {len(computer_hand)}')

    playable_cards = get_playable_cards(computer_hand, top_card)

    if playable_cards:
        played_card = playable_cards[0] 

        computer_hand.remove(played_card)
        print("Computer played:", played_card)
        top_card = played_card
        global player_skipped

        if len(top_card) == 1:
            player_skipped = True
            player_hand.append(card_deck.pop())
            player_hand.append(card_deck.pop())
            player_hand.append(card_deck.pop())
            player_hand.append(card_deck.pop())
            print("Draw Four Cards")
            
        elif top_card [0] == "Skip" or top_card [1] == "Skip":
            player_skipped = True 
            print("Turn Skipped")
            computer_turn(computer_hand, top_card)
        elif top_card [0] == "Reverse" or top_card [1] == "Reverse":
            player_skipped = True
            print("Turn Reversed")
            computer_turn(computer_hand, top_card)
        elif top_card [0] == "DrawTwo" or top_card [1] == "DrawTwo":
            player_skipped = True
            player_hand.append(card_deck.pop())
            player_hand.append(card_deck.pop())
            print("DrawTwo cards")
            
    else:
        print("No playable cards, one card will be drawn from the deck.")
        if deck:
            drawn_card = deck.pop()
            player_hand.append(drawn_card)
            print("Computer drew a card.")
        else:
            print("No more cards left to draw.")

    return top_card

#Chceks winner
def check_game_end(player_hand, computer_hand):
    if not player_hand:
        print("Congratulations! You win!")
        return True
    elif not computer_hand:
        print("The computer wins!")
        return True
    return False

# Main Game Loop
def play_game():
    global deck
    # Initialize the game
    deck = my_deck()
    deck = shuffling(deck)
    player_hand, computer_hand = distribute_cards()
    top_card = discard_pile[-1]  # Get the first top card

    while True:
        top_card = player_turn(player_hand, top_card)  # Player's turn
        if check_game_end(player_hand, computer_hand):
            break
        
        top_card = computer_turn(computer_hand, top_card)  # Computer's turn
        if check_game_end(player_hand, computer_hand):
            break


play_game()

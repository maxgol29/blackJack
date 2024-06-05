import random as r

cards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': [2, 10],
    'queen': [3, 10],
    'king': [4, 10],
    'ace': [1, 10]
}
players = {}
def get_deck_index(deck, index):
    return deck[index]
def shuffle_deck():
    deck = []
    for i in range(4):
        for card in cards.keys():
            deck.append(card)
    for i in range(52):
        random_number = r.randrange(52)
        deck[i], deck[random_number] = deck[random_number], deck[i]
    return deck
def identification_of_player(player):
    if player not in players.keys():
        players[player] = 1000
        return False
    return True
def converting_cards(side_cards, card_with_picture = False):
    sum_of_cards = 0
    for i in side_cards:
        if i in ['jack', 'queen', 'king', 'ace']:
            if card_with_picture:
                sum_of_cards += cards[i][1]
            else:
                sum_of_cards += cards[i][0]
        else:
            sum_of_cards += cards[i]
    return sum_of_cards
def blackJack_game():
    checker = input("This is a BlackJack Game, have you ever played this before? yes or no?: ")
    name = input("What is your name?: ").capitalize()
    identification = identification_of_player(player=name)
    if checker == 'yes' and identification:
        print('great')
        print(players)
    else:
        print("I added you into the system!")
        print(f"Your initial amount {players[name]}")
    print("Game was started!")
    deck = shuffle_deck()
    index_of_deck = 0
    computer_winner = False
    player_winner = False
    player_cards = []
    computer_cards = []
    # First cards player & computer
    for i in range(2):
        player_cards.append(get_deck_index(deck=deck, index=index_of_deck))
        index_of_deck += 1
    computer_cards.append(get_deck_index(deck, index_of_deck))
    index_of_deck += 1
    print(f'Your cards: {player_cards} which is equal to {converting_cards(player_cards)}', f'Computer\'s first card: {computer_cards}, which is equal to {converting_cards(computer_cards)}', sep='\n')
    # -------------------------------
    for card in player_cards:
        if card in ['jack', 'queen', 'king', 'ace']:
            update_player_cards = input(f"Do you want to keep {cards[card][0]} or to add 10? Type 'y' or 'n': ")
            if update_player_cards == 'y':
                sum_updated_player_cards = converting_cards(player_cards, True)
            else:
                sum_updated_player_cards = converting_cards(player_cards)
    sum_updated_player_cards = converting_cards(player_cards)
    stopper_deck = input("Type 'y' to get another card, type 'n' to pass: ")
    while stopper_deck == 'y':
        player_cards.append(get_deck_index(deck, index_of_deck))
        index_of_deck += 1
        print(sum_updated_player_cards)
        if sum_updated_player_cards > 21:
            computer_winner = True
            print("Computer won!")
            break
        stopper_deck = input("Type 'y' to get another card, type 'n' to pass: ")
    if computer_winner:
        return "Computer won!"
    while converting_cards(computer_cards) <= 16:
        computer_cards.append(get_deck_index(deck, index_of_deck))
        index_of_deck += 1
        if converting_cards(computer_cards) > 21:
            print(computer_cards)
            print("Player won!")
            break
        print(computer_cards)
    if computer_winner or converting_cards(computer_cards) > sum_updated_player_cards:
        print(computer_cards)
        return "Computer won!"
    print(update_player_cards)
    return "Player won!"



print(blackJack_game())

import random

cards = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
    }

suits = ["Heart", "Diamond", "Spade", "Club"]

# bet function
def bet():
    return input("Place a bet: ")

# deal function
def deal(amount):
    count = 0
    dealt = []
    while count != amount:
        random_card = random.choice(list(cards.keys()))
        random_suit = random.choice(suits)
        result = random_card + " of " + random_suit + "s"
        dealt.append(result)
        count += 1
    return dealt

def calculate_points(card_list):
    total = 0
    for card in card_list:
        card_name = card.split(" ")[0]
        total += cards.get(card_name)
    return total
    
def determine_winner(p1_points, p2_points):
    winner = ""
    if p1_points == 21 and p2_points != 21:
        winner = "Player 1"
        
    elif p2_points == 21 and p1_points != 21:
        winner = "Player 2"
        
    elif p1_points == 21 and p2_points == 21:
        winner = "Tie"
    
    elif p1_points > 21 and p2_points > 21:
        winner = "Tie"
        
    elif p1_points > 21:
        winner = "Player 2"
    
    elif p2_points > 21:
        winner = "Player 1"
        
    return winner

def main():
    money_made = 0
    while True:
        p1_points = 0
        p2_points = 0
        p1_cards = []
        p2_cards = []
        bet = int(input("Place a bet: "))
        print("Drawing 2 cards to player and host...")
        print("--- Your Cards ---")
            
        # cards get dealt
        p1_cards.extend(deal(2))
        p2_cards.extend(deal(2))
            
        # cards points get added up
        p1_points = calculate_points(p1_cards)
        p2_points = calculate_points(p2_cards)
        print(f"{p1_cards} = {p1_points} points")
        
        # determine if someone got 21 off first two cards         
        if determine_winner(p1_points, p2_points) == "Player 1":
            money_made += bet
            print(f"Player 1 Wins! You just won ${bet}\n{money_made}")
            continue
        elif determine_winner(p1_points, p2_points) == "Player 2":
            money_made -= bet
            print(f"Player 2 Wins! You just lost ${bet}\n{money_made}")
            continue
        elif determine_winner(p1_points, p2_points) == "Tie":
            print("Tie Game")
            continue
        
        while True:
            deal_another = input("Do you want to another card? Y/N ")
            if deal_another == "y":
                p1_cards.extend(deal(1))
                p1_points = calculate_points(p1_cards)
                print(f"{p1_cards} = {p1_points} points")
            if deal_another != "y" and deal_another != "n":
                continue
            else:
                break
            
        
        print("hi")
        print(f"You have made ${money_made}.")
                
            
            
            
main()
#print(deal(2))


# Testing Block
"""test = deal(2)
print(test)
print(calculate_points(test))"""

#determine_winner(22, 21)